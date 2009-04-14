# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import urllib

from modu.persist import sql
from modu.util import form, tags
from modu.editable import define

from gigkeeper.model import history

class HistoryListField(define.definition):
	"""
	Display a list of URLs for this record.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		
		req.store.ensure_factory('history', model_class=history.History)
		histories = req.store.load('history', item_id=storable.get_id(),
					item_table=storable.get_table(), __order_by='type')
		
		params = {
			'__init__[item_id]'		: storable.get_id(),
			'__init__[item_table]'	: storable.get_table(),
		}
		
		contact_callback = self.get('contact_callback', None)
		if(callable(contact_callback)):
			params['__init__[contact_id]'] = contact_callback(req, frm, storable)
		
		add_history_url = req.get_path(req.prepath, 'detail/history/new?') + urllib.urlencode(params)
		if(storable.get_id()):
			frm['add_history'](
				type	= 'markup',
				value	= tags.a(href=add_history_url)['Add History'] 
			)
		else:
			frm['add_history'](
				type	= 'label',
				value	= "This item has no history yet.",
			)
		
		if(histories):
			for h in histories:
				history_url = req.get_path(req.prepath, 'detail/history', h.get_id())
				frm['history'][h.get_id()](
					prefix = '<div>',
					suffix = '</div>',
				)
				frm['history'][h.get_id()]['select'](
					type 	= 'checkbox',
				)
				frm['history'][h.get_id()]['summary'](
					type 	= 'label',
					value	= tags.a(href=history_url)[h.summary],
					prefix	= '&nbsp;&nbsp;',
				)
				frm['history'][h.get_id()]['type'](
					type 	= 'label',
					value	= h.type,
					prefix	= '&nbsp;&nbsp;',
				)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass
