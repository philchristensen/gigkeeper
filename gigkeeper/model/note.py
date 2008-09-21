# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

NOTE_TYPES = odict([
	('booking',		'Booking Info'),
	('review',		'Review'),
])

class Note(storable.Storable):
	def __init__(self):
		super(Note, self).__init__('note')
