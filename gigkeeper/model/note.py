# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import re

from modu.persist import storable
from modu.util import OrderedDict as odict

NOTE_TYPES = odict([
	('booking',		'Booking Info'),
	('review',		'Review'),
	('backline',	'Backline Info'),
])

class Note(storable.Storable):
	def __init__(self):
		super(Note, self).__init__('note')
	
	def summarize(self, length=200):
		untagged = re.sub(r'<[^>]*?>', '', self.description)
		words = untagged.split()
		return ' '.join(words[:length])
