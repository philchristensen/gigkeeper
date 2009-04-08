# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

EVENT_TYPES = odict([
	('performance',		'Performance'),
])

class Event(storable.Storable):
	def __init__(self):
		super(Event, self).__init__('event')
