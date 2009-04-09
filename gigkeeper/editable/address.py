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
from gigkeeper.model import address

class AddressListField(define.definition):
	"""
	Display a list of Addresses for this record.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		frm.theme = theme.GigkeeperTheme
		
		req.store.ensure_factory('address', model_class=address.Address)
		addresses = req.store.load('address', item_id=storable.get_id(),
					item_table=storable.get_table(), __order_by='type')
		
		params = {
			'__init__[item_id]'		: storable.get_id(),
			'__init__[item_table]'	: storable.get_table(),
		}

		address_name_callback = self.get('address_name_callback', None)
		if(callable(address_name_callback)):
			params['__init__[name]'] = address_name_callback(req, frm, storable)
		
		add_address_url = req.get_path(req.prepath, 'detail/address/new?') + urllib.urlencode(params)
		frm['add_address'](
			type	= 'markup',
			value	= tags.a(href=add_address_url)['Add Address'] 
		)
		
		if(addresses):
			for a in addresses:
				address_url = req.get_path(req.prepath, 'detail/address', a.get_id())
				frm['addresses'][a.get_id()](
					prefix = '<div>',
					suffix = '</div>',
				)
				frm['addresses'][a.get_id()]['select'](
					type 	= 'checkbox',
				)
				frm['addresses'][a.get_id()]['address'](
					type 	= 'label',
					value	= tags.a(href=address_url)[a.as_string()],
					prefix	= '&nbsp;&nbsp;',
				)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass
