# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import sql
from modu.util import form, tags
from modu.editable import define

from gigkeeper.model import note

class NoteListField(define.definition):
	"""
	Display a list of URLs for this record.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		
		req.store.ensure_factory('note', model_class=note.Note)
		notes = req.store.load('note', item_id=storable.get_id(),
					item_table=storable.get_table(), __order_by='type')
		
		if(notes):
			for n in notes:
				note_url = req.get_path(req.prepath, 'detail/note', n.get_id())
				frm['notes'][n.get_id()](
					prefix = '<div>',
					suffix = '</div>',
				)
				frm['notes'][n.get_id()]['select'](
					type 	= 'checkbox',
				)
				frm['notes'][n.get_id()]['title'](
					type 	= 'label',
					value	= tags.a(href=note_url)[n.summary],
					prefix	= '&nbsp;&nbsp;',
				)
				frm['notes'][n.get_id()]['type'](
					type 	= 'label',
					value	= n.type,
					prefix	= '&nbsp;&nbsp;',
				)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass
