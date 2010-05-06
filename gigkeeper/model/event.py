# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable, sql
from modu.util import OrderedDict as odict

from gigkeeper.model import ModelURLMixin, media, company, address

EVENT_TYPES = odict([
	('performance',		'Performance'),
])

def get_upcoming_events(store):
	store.ensure_factory('event', model_class=Event)
	events = store.load('event', scheduled_date=sql.RAW('%s > CURDATE()'), __order_by='scheduled_date')
	return events or []

def get_prior_events(store):
	store.ensure_factory('event', model_class=Event)
	events = store.load('event', scheduled_date=sql.RAW('%s < CURDATE()'), __order_by='scheduled_date DESC')
	return events or []

class Event(storable.Storable, ModelURLMixin):
	def __init__(self):
		super(Event, self).__init__('event')
	
	def get_standardized_title(self):
		venue = self.get_venue()
		
		output = [self.scheduled_date.strftime('%Y-%m-%d')]
		if(venue):
			output.extend((' - ', venue.name))
			address = venue.get_address()
			if(address):
				output.extend((' - ', address.city, ', ', address.region))
		
		return ''.join(output)
	
	def get_venue(self):
		store = self.get_store()
		store.ensure_factory('company', model_class=company.Company)
		return store.load_one('company', id=self.company_id)
	
	def get_description(self, html=True):
		if(html):
			return self.description.replace("\n", "<br/>")
		else:
			return self.description
	
	def get_details_url(self, req):
		date = self.scheduled_date.strftime('%Y-%m-%d')
		return req.get_path('events', date, self.url_code)
	
	def get_flyer_url(self, req):
		store = self.get_store()
		store.ensure_factory('media', model_class=media.Media)
		flyer = store.load_one('media', item_id=self.get_id(), item_table=self.get_table(),
								filename=sql.RAW("LEFT(%s, 7) = 'flyers/'"))
		if not(flyer):
			return ''
		else:
			return req.get_path('uploads', flyer.filename)
	
	def get_album(self):
		from seaflux.model import album
		store = self.get_store()
		store.ensure_factory('album', model_class=album.Album)
		return store.load_one('album', event_id=self.get_id())
