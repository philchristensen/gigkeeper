# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import urllib

from modu.persist import sql
from modu.util import form, tags
from modu.editable import define

from gigkeeper.model import history, contact

class CompanyContactListField(define.definition):
	"""
	Display a list of contacts at this company.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		company_id = storable.get_id()
		
		params = {
			'__init__[company_id]'		: company_id
		}
		
		add_contact_url = req.get_path(req.prepath, 'detail/contact/new?') + urllib.urlencode(params)
		if(company_id):
			frm['add_contact'](
				type	= 'markup',
				value	= tags.a(href=add_contact_url)['Add Contact'] 
			)
		else:
			frm['add_contact'](
				type	= 'label',
				value	= "This item has no contacts yet.",
			)
		
		
		req.store.ensure_factory('contact', model_class=contact.Contact)
		
		contacts = req.store.load('contact', company_id=company_id) or []
		
		if not(contacts):
			frm['contact'](
				type	= 'label',
				value	= "This company has no contacts yet.",
			)
			return frm
		
		for c in contacts:
			contact_url = req.get_path(req.prepath, 'detail/contact', c.get_id())
			frm['contact'][c.get_id()](
				prefix = '<ul>',
				suffix = '</ul>',
			)
			frm['contact'][c.get_id()]['name'](
				type 	= 'label',
				value	= tags.a(href=contact_url)[c.name],
				prefix	= '<li>',
				suffix	= '</li>',
			)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass

