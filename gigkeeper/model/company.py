# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

COMPANY_TYPES = odict([
	('venue',	'venue'),
	('agency',	'agency'),
	('artist',	'artist'),
])

class Company(storable.Storable):
	def __init__(self):
		super(Company, self).__init__('company')
