# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable
from modu.util import OrderedDict as odict

URL_TYPES = odict([
	('homepage',	'Homepage'),
	('myspace',		'MySpace'),
	('facebook',	'Facebook'),
])

class URL(storable.Storable):
	def __init__(self):
		super(URL, self).__init__('url')
