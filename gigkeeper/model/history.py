# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

HISTORY_TYPES = odict([
	('phone',		'Phone Call'),
	('email',		'Email'),
	('in_person',	'In Person'),
])

class History(storable.Storable):
	def __init__(self):
		super(History, self).__init__('history')
