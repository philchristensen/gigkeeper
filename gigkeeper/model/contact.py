# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.persist import storable

class Contact(storable.Storable):
	def __init__(self):
		super(Contact, self).__init__('contact')
