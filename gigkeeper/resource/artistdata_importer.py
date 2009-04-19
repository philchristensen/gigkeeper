# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.web import resource, app
from modu.util import form, csv

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
		Setup the upload form, and process RSS feed for import.
		
		@see: L{modu.web.resource.IContent.prepare_content()}
		"""
		import_form = form.FormNode('import-form')
		import_form(enctype='multipart/form-data')
		import_form['upload'](type = 'file', label='upload datafile:')
		import_form['submit'](type='submit')
		import_form.validate = self.validate_import
		import_form.submit = self.submit_import
		
		self.set_slot('csv_file', '')
		
		if not(import_form.execute(req)):
			import_form.escalate_errors(req)
		
		self.set_slot('import_form', import_form.render(req))
	
	def validate_import(self, req, frm):
		"""
		Upload form validation callback.
		
		Validate the CSV upload form.
		"""
		if not(req.data[frm.name].get('upload', None)):
			frm.set_error('upload', 'You must select the datafile to upload.')
			return False
		return True
	
	def submit_import(self, req, frm):
		upload_file = req.data['import-form']['upload'].file
		upload_file.readline()
		csv_file = csv.parse(upload_file, column_names=csv_header_list)
		self.set_slot('csv_file', str(csv_file))
		
		return True
	
	def get_template(self, req):
		"""
		@see: L{modu.web.resource.ITemplate.get_template()}
		"""
		return 'artistdata-importer.html.tmpl'
