# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

ADDRESS_TYPES = odict([
	('home',		'Home'),
	('work',		'Work'),
])

class Address(storable.Storable):
	def __init__(self):
		super(Address, self).__init__('address')
	
	def as_string(self):
		components = []
		components.append(self.name)
		components.append(self.address1)
		if(self.address2):
			components.append(self.address2)
		components.append(self.city)
		components.append(self.region + '   ' + self.zip + '   ' + self.country)
		return ', '.join(components)
