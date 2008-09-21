# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import sql
from modu.util import form, tags
from modu.editable import define

from gigkeeper.model import url

class URLListField(define.definition):
	"""
	Display a list of URLs for this record.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		
		req.store.ensure_factory('url', model_class=url.URL)
		urls = req.store.load('url', item_id=storable.get_id(),
					item_table=storable.get_table(), __order_by='type')
		
		if(urls):
			for u in urls:
				frm['urls'][u.get_id()](
					prefix = '<div>',
					suffix = '</div>',
				)
				frm['urls'][u.get_id()]['select'](
					type 	= 'checkbox',
				)
				frm['urls'][u.get_id()]['url'](
					type 	= 'label',
					value	= tags.a(href=u.url)[u.url],
					prefix	= '&nbsp;&nbsp;',
				)
				frm['urls'][u.get_id()]['type'](
					type 	= 'label',
					value	= u.type,
					prefix	= '&nbsp;&nbsp;',
				)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass
