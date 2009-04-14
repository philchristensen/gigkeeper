# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import urllib

from modu.persist import sql
from modu.util import form, tags
from modu.editable import define

from gigkeeper import theme
from gigkeeper.model import note

class NoteListField(define.definition):
	"""
	Display a list of notes for this record.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		frm.theme = theme.GigkeeperTheme
		
		req.store.ensure_factory('note', model_class=note.Note)
		notes = req.store.load('note', item_id=storable.get_id(),
					item_table=storable.get_table(), __order_by='type')
		
		params = urllib.urlencode({
			'__init__[item_id]'		: storable.get_id(),
			'__init__[item_table]'	: storable.get_table(),
		})
		add_note_url = req.get_path(req.prepath, 'detail/note/new?') + params
		
		if(storable.get_id()):
			frm['add_note'](
				type	= 'markup',
				value	= tags.a(href=add_note_url)['Add Note'] 
			)
		else:
			frm['add_note'](
				type	= 'label',
				value	= "Please save this record before adding notes.",
			)
		
		if(notes):
			for n in notes:
				note_url = req.get_path(req.prepath, 'detail/note', n.get_id())
				frm['notes'](
					type	= 'note_list',
				)
				frm['notes'][n.get_id()](
					type	= 'note',
				)
				frm['notes'][n.get_id()]['select'](
					type 	= 'checkbox',
				)
				frm['notes'][n.get_id()]['title'](
					type 	= 'label',
					value	= tags.a(href=note_url, _class='note-title')[n.summary],
				)
				frm['notes'][n.get_id()]['created_date'](
					type 	= 'label',
					value	= n.created_date,
					attributes = dict(
						_class = 'note-date',
					),
				)
				frm['notes'][n.get_id()]['type'](
					type 	= 'label',
					value	= '(%s)' % n.type,
					prefix	= '&nbsp;&nbsp;',
					attributes = dict(
						_class = 'note-type',
					),
				)
				frm['notes'][n.get_id()]['body'](
					type 	= 'body_text',
					value	= n.summarize(length=50),
				)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass
