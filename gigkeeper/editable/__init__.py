# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import sql
from modu.util import form, tags
from modu.editable.datatypes import relational

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
			frm(type='label', value=label)
		else:
			if not(label):
				label = '(no label available)'
			
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