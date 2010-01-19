# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import urllib

from modu.persist import sql
from modu.util import form, tags
from modu.editable import define

from gigkeeper.model import history, event

class GenericHistoryListField(define.definition):
	"""
	Display a list of URLs for this record.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		
		req.store.ensure_factory('history', model_class=history.History)
		histories = req.store.load('history', item_id=storable.get_id(),
					item_table=storable.get_table(), __order_by='type') or []
		
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


class CompanyHistoryListField(define.definition):
	"""
	Display a list of shows played at this venue,
	or shows booked with this agency.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		company_id = storable.get_id()
		
		if not(company_id):
			frm['event'](
				type	= 'label',
				value	= "This company has no history yet.",
			)
			return frm
		
		req.store.ensure_factory('event', model_class=event.Event)
		
		if(storable.type == 'venue'):
			events = req.store.load('event', company_id=company_id, __order_by='scheduled_date DESC') or []
		elif(storable.type == 'agency'):
			events = req.store.load('event', 
						sql.interp("""SELECT e.*
										FROM event e
										INNER JOIN (contact c
											INNER JOIN company a ON c.company_id = a.id)
										ON c.id = e.contact_id
										WHERE a.type = 'agency'
										  AND a.id = %s
										ORDER BY e.scheduled_date DESC
									""", company_id)) or []
		else:
			events = []
		
		if not(events):
			frm['event'](
				type	= 'label',
				value	= "This company has no history yet.",
			)
			return frm
		
		for e in events:
			event_url = req.get_path(req.prepath, 'detail/event', e.get_id())
			frm['event'][e.get_id()](
				prefix = '<ul>',
				suffix = '</ul>',
			)
			frm['event'][e.get_id()]['name'](
				type 	= 'label',
				value	= tags.a(href=event_url)[e.name],
				prefix	= '<li>',
			)
			frm['event'][e.get_id()]['type'](
				type 	= 'label',
				value	= e.type,
				prefix	= '&nbsp;&nbsp;',
				suffix	= '</li>',
			)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass


class ContactHistoryListField(define.definition):
	"""
	Display a list of shows booked with this contact.
	"""
	def get_element(self, req, style, storable):
		frm = form.FormNode(self.name)
		
		if not(storable.get_id() and storable.company_id):
			frm['event'](
				type	= 'label',
				value	= "This contact has no history yet.",
			)
			return frm
		
		req.store.ensure_factory('event', model_class=event.Event)
		
		events = req.store.load('event', 
					sql.interp("""SELECT e.*, c.name AS contact_name
									FROM event e
										INNER JOIN contact c ON c.id = e.contact_id
									WHERE e.contact_id IN (
										SELECT id FROM contact WHERE company_id = %s
									)
									ORDER BY e.scheduled_date DESC
								""", storable.company_id)) or []
		
		if not(events):
			frm['event'](
				type	= 'label',
				value	= "This contact has no history yet.",
			)
			return frm
		
		for e in events:
			event_url = req.get_path(req.prepath, 'detail/event', e.get_id())
			
			is_related_contact = (e.contact_id != storable.get_id())
			related_class = (' class="related-contact"', '')[not is_related_contact]
			related_contact_url = req.get_path(req.prepath, 'detail/contact', e.contact_id)
			
			frm['event'][e.get_id()](
				prefix = '<ul>',
				suffix = '</ul>',
			)
			frm['event'][e.get_id()]['name'](
				type 	= 'label',
				value	= tags.a(href=event_url)[e.name],
				prefix	= '<li%s>' % related_class,
			)
			if(is_related_contact):
				frm['event'][e.get_id()]['related_contact'](
					type 	= 'label',
					value	= '(' + tags.a(href=related_contact_url)[e.contact_name] + ')',
					prefix	= '&nbsp;&nbsp;',
				)
				
			frm['event'][e.get_id()]['type'](
				type 	= 'label',
				value	= e.type,
				prefix	= '&nbsp;&nbsp;',
				suffix	= '</li>',
			)
		
		return frm
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass
