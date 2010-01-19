# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import os.path

from modu.persist import sql
from modu.util import form, tags
from modu.editable.resource import select_template_root
from modu.editable.datatypes import relational

import gigkeeper

def event_autocomplete_callback(req, partial, definition):
	"""
	Do an INSTR match to find the user first, last or username.
	"""
	ac_query = """SELECT e.id, CONCAT(DATE_FORMAT(e.scheduled_date, '%%Y-%%m-%%d @ %%h:%%i%%p'), ' - ', c.name) AS name
					FROM event e
					INNER JOIN company c ON c.id = e.company_id
				   WHERE INSTR(CONCAT(DATE_FORMAT(e.scheduled_date, '%%Y-%%m-%%d @ %%h:%%i%%p'), ' - ', c.name), %s)
				   ORDER BY e.scheduled_date DESC
				   LIMIT 50
				"""
	results = req.store.pool.runQuery(ac_query, [partial])
	content = ''
	for result in results:
		content += "%s|%d\n" % (result['name'], result['id'])
	
	return content

def contact_autocomplete_callback(req, partial, definition):
	"""
	Do an INSTR match to find the user first, last or username.
	"""
	ac_query = "SELECT id, name AS name FROM `contact` WHERE INSTR(name, %s) LIMIT 50"
	results = req.store.pool.runQuery(ac_query, [partial])
	content = ''
	for result in results:
		content += "%s|%d\n" % (result['name'], result['id'])
	
	return content

class AdminTemplateResourceMixin(object):
	def get_template_root(self, req, template=None):
		"""
		@see: L{modu.web.resource.ITemplate.get_template_root()}
		"""
		if(template is None):
			template = self.get_template(req)
		
		template_root = select_template_root(req, template)
		
		if(os.path.exists(os.path.join(template_root, template))):
			return template_root
		
		return os.path.join(os.path.dirname(gigkeeper.__file__), 'assets', 'default-template')


class ItemTitleField(relational.ForeignLabelField):
	"""
	Display the item title for this record.
	
	Given the item_id and item_table fields available in some records,
	this field will display the proper title.
	"""
	def get_element(self, req, style, storable):
		"""
		@see: L{modu.editable.define.definition.get_element()}
		"""
		store = storable.get_store()
		
		label = None
		value = None
		
		label_col = self.get('flabel', 'title')
		value_col = 'id'
		
		table = getattr(storable, 'item_table', None)
		if not(table):
			table = self.get('ftable')
		
		item_value = getattr(storable, self.get_column_name(), None)
		
		if(table is None or item_value is None):
			results = None
		else:
			# We select * in case the particular item doesn't have a title field
			foreign_label_query = "SELECT * FROM %s WHERE %s = %%s" % (table, value_col)
			foreign_label_query = sql.interp(foreign_label_query, [item_value])
			
			results = store.pool.runQuery(foreign_label_query)
			if(results):
				value = results[0][value_col]
				label = results[0].get(label_col, '(label not found)')
		
		frm = form.FormNode(self.name)
		suffix = ''
		prefix = ''
		if(style == 'listing'):
			frm(type='hidden', value=value)
			if(table and value):
				label = tags.a(href=req.get_path(req.prepath, 'detail', table, value))[label]
			frm(type='label', value=label)
		else:
			if not(label):
				label = '(no link available)'
			
			frm(type='hidden', value=value)
			if(table and value):
				prefix = tags.a(href=req.get_path(req.prepath, 'detail', table, value))[label]
			else:
				prefix = label
		
		frm(prefix=prefix, suffix=suffix)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass