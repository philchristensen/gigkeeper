# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

from gigkeeper.model import address

COMPANY_TYPES = odict([
	('venue',	'venue'),
	('agency',	'agency'),
	('artist',	'artist'),
])

def find_venue(store, details):
	pass

class Company(storable.Storable):
	def __init__(self):
		super(Company, self).__init__('company')
	
	def get_address(self):
		store = self.get_store()
		store.ensure_factory('address', address.Address)
		return store.load_one('address', item_table='company', item_id=self.get_id())