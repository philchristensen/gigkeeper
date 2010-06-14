# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import urllib2, datetime
from xml.dom import minidom

from modu.editable import util
from gigkeeper.model import event, company

feed_url = 'http://feeds.artistdata.com/xml.shows/artist/AR-4AV8NOZRG715CYIN/xml'

def parse_feed(feed_url):
	feed = urllib2.urlopen(feed_url)
	doc = minidom.parse(feed)
	
	def _text(nodelist):
		rc = ""
		for node in nodelist:
			if node.nodeType in (node.TEXT_NODE, node.CDATA_SECTION_NODE):
				rc = rc + node.data
		return rc
	
	def _snatch(element, name):
		element = element.getElementsByTagName(name)[0]
		return _text(element.childNodes)
	
	result = []
	for show in doc.getElementsByTagName('show'):
		result.append(dict(
			recordKey			= _snatch(show, 'recordKey'),
			name				= _snatch(show, 'name'),
			city				= _snatch(show, 'city'),
			venueName			= _snatch(show, 'venueName'),
			venueZip			= _snatch(show, 'venueZip'),
			venuePhone			= _snatch(show, 'venuePhone'),
			venueAddress		= _snatch(show, 'venueAddress'),
			ticketURI			= _snatch(show, 'ticketURI'),
			description			= _snatch(show, 'description'),
			ageLimit			= _snatch(show, 'ageLimit'),
			venueURI			= _snatch(show, 'venueURI'),
			ticketPrice			= _snatch(show, 'ticketPrice'),
			date				= _snatch(show, 'date'),
			timeSet				= _snatch(show, 'timeSet'),
			timeDoors			= _snatch(show, 'timeDoors'),
			stateAbbreviation	= _snatch(show, 'stateAbbreviation'),
			state				= _snatch(show, 'state'),
			countryAbbreviation	= _snatch(show, 'countryAbbreviation'),
			country				= _snatch(show, 'country'),
			artistname			= _snatch(show, 'artistname'),
			artistKey			= _snatch(show, 'artistKey'),
		))
	
	return result

def update_show(store, show):
	store.ensure_factory('event', model_class=event.Event)
	store.ensure_factory('company', model_class=company.Company)
	
	evt = store.load_one('event', artistdata_id=show['recordKey'])
	if(evt is None):
		evt = event.Event()
		evt.artistdata_id = show['recordKey']
		evt.type = 'performance'
	
	date_parts = [int(x) for x in show['date'].split('-') + show['timeSet'].split(':')]
	
	evt.name = '%s @ %s' % (show['name'] or 'seaflux live', show['venueName'])
	evt.url_code = util.create_url_code(evt.name, 'event', store.pool, origin_id=evt.get_id())
	
	# only set the description if there isn't one
	if(show['description']):
		evt.description = show['description']
	
	evt.scheduled_date = datetime.datetime(*date_parts)
	try:
		evt.cover_fee = int(show['ticketPrice'])
	except ValueError:
		evt.cover_fee = None
	
	# only set the venue if we haven't already
	venue = store.load_one('company', type='venue', name=show['venueName'])
	if(venue and getattr(evt, 'company_id', None) == None):
		evt.company_id = venue.get_id()
	
	#print evt.get_data()
	store.save(evt)

def sync_shows(store):
	for show in parse_feed(feed_url):
		update_show(store, show)
