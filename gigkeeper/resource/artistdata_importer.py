# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.web import resource, app
from modu.util import form, csv
from modu.persist import sql

from gigkeeper.editable import AdminTemplateResourceMixin

csv_header_list = [
	'date',
	'time',
	'showname',
	'doors_time',
	'city',
	'state',
	'country',
	'venue_name',
	'venue_address',
	'venue_url',
	'venue_zip',
	'venue_phone',
	'age_limit',
	'ticket_price',
	'ticket_url',
	'description',
	'other_artist_1',
	'other_artist_1_time',
	'other_artist_1_url',
	'other_artist_1_settype',
	'other_artist_2',
	'other_artist_2_time',
	'other_artist_2_url',
	'other_artist_2_settype',
	'other_artist_3',
	'other_artist_3_time',
	'other_artist_3_url',
	'other_artist_3_settype',
]

class Resource(AdminTemplateResourceMixin, resource.CheetahTemplateResource):
	"""
	Allow for importing event data from ArtistData RSS feeds.
	
	Sample Itemdef::
		from modu.editable import define
		
		from gigkeeper.resource import artistdata_importer
		
		__itemdef__ = define.itemdef(
		    __config            = dict(
		        name            = 'artistdata-importer',
		        label           = 'access control',
		        category        = 'relationships',
		        acl             = 'access admin',
		        weight          = -10,
		        resource        = artistdata_importer.Resource
		    )
		)
	
	
	"""
	def prepare_content(self, req):
		"""
		@see: L{modu.web.resource.IContent.prepare_content()}
		"""
		self.set_slot('current_form', '')
		
		if(self.is_import_in_progress(req)):
			self.prepare_reconcilliation(req)
		else:
			self.prepare_upload(req)
		
	def is_import_in_progress(self, req):
		result = req.store.pool.runQuery("SELECT COUNT(*) AS total FROM artist_data_import_temp")
		if(result and result[0]['total']):
			return True
		return False
	
	def prepare_upload(self, req):
		"""
		Setup the upload form, and process RSS feed for import.
		"""
		upload_form = self.get_upload_form(req)
		if(upload_form.execute(req)):
			app.redirect(req.get_path(req.path))
		else:
			upload_form.escalate_errors(req)
		
		self.set_slot('current_form', upload_form.render(req))
	
	def get_upload_form(self, req):
		upload_form = form.FormNode('import-form')

		upload_form(enctype='multipart/form-data')
		upload_form['upload'](
			type	= 'file',
			label	= 'upload datafile:'
		)
		upload_form['submit'](
			type	= 'submit',
			value	= 'upload',
		)
		upload_form.validate = self.validate_upload
		upload_form.submit = self.submit_upload
		
		return upload_form
	
	def validate_upload(self, req, frm):
		"""
		Upload form validation callback.
		
		Validate the CSV upload form.
		"""
		if not(req.data[frm.name].get('upload', None)):
			frm.set_error('upload', 'You must select the datafile to upload.')
			return False
		return True
	
	def submit_upload(self, req, frm):
		upload_file = req.data['import-form']['upload'].file
		upload_file.readline()
		csv_data = csv.parse(upload_file, column_names=csv_header_list)
		for record in csv_data:
			insert_query = sql.build_insert('artist_data_import_temp', record)
			req.store.pool.runOperation(insert_query)
		
		return True
	
	def prepare_reconcilliation(self, req):
		req.store.ensure_factory('artist_data_import_temp', guid_table=None)
		import_record = req.store.load_one('artist_data_import_temp', __limit='1', __order_by='id ASC')
		
		reconcilliation_form = self.get_reconcilliation_form(req, import_record)
		if not(reconcilliation_form.execute(req)):
			reconcilliation_form.escalate_errors(req)
		
		self.set_slot('current_form', reconcilliation_form.render(req))
	
	def get_reconcilliation_form(self, req, import_record):
		reconcilliation_form = form.FormNode('reconcilliation-form')
		
		for column in csv_header_list:
			reconcilliation_form[column](
				type		= 'textfield',
				label		= column.replace('_', ' '),
				value		= getattr(import_record, column, 'n/a'),
			)
		
		return reconcilliation_form
	
	def get_template(self, req):
		"""
		@see: L{modu.web.resource.ITemplate.get_template()}
		"""
		return 'artistdata-importer.html.tmpl'
