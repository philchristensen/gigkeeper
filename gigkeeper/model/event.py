# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable, sql
from modu.util import OrderedDict as odict

from gigkeeper.model import ModelURLMixin

EVENT_TYPES = odict([
	('performance',		'Performance'),
])

def get_upcoming_events(store):
	store.ensure_factory('event', model_class=Event)
	events = store.load('event', scheduled_date=sql.RAW('%s > CURDATE()'))
	return events or []

def get_prior_events(store):
	store.ensure_factory('event', model_class=Event)
	events = store.load('event', scheduled_date=sql.RAW('%s < CURDATE()'))
	return events or []

class Event(storable.Storable, ModelURLMixin):
	def __init__(self):
		super(Event, self).__init__('event')
	
	def get_html_description(self):
		return self.description.replace("\n", "<br/>")
		
