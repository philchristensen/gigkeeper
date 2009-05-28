# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

"""
Media model.
"""

from modu.persist import storable

class Media(storable.Storable):
	"""
	Media model class
	"""
	def __init__(self):
		"""
		Create a new media object.
		"""
		super(Media, self).__init__('media')
	
	def get_url(self, req):
		return req.get_path('uploads', self.filename)