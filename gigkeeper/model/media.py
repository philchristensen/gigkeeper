# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

"""
Media model.
"""

import os

from modu.persist import storable

from gigkeeper.util.media import get_media_details, get_checksum

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
	
	def populate_from(self, path, md5_path=None):
		self.type, self.format, self.quality = get_media_details(path)
		
		if not(self.type and self.format and self.quality):
			raise ValueError("Sorry, %s is not a supported file type." % path)
		
		kwargs = {}
		if(md5_path):
			kwargs['md5_path'] = md5_path
		self.md5 = get_checksum(path, **kwargs)
			
		st_info = os.stat(path)
		self.filesize = st_info.st_size
