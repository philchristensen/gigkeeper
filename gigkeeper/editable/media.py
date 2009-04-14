# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

"""
Display a list of media associated with the current item.
"""

import os.path, urllib

from modu.util import tags, form
from modu.persist import sql
from modu.editable import define
from modu.editable.datatypes import string

from gigkeeper.model.media import Media
from gigkeeper.util import media


class MediaListField(define.definition):
	"""
	Generally for detail view only, display a list of associated media.
	
	The files on disk will be checked for filesize, but can also have their
	MD5 checksums verified on a case-by-case basis.
	"""
	def get_element(self, req, style, storable):
		"""
		@see: L{modu.editable.define.definition.get_element()}
		"""
		store = storable.get_store()
		
		foreign_query = """
			SELECT m.*
			FROM media m
			WHERE m.item_id = %s
			ORDER BY m.type
			""" % (storable.get_id())
		
		results = store.pool.runQuery(foreign_query)
		
		content = self.get('formatter', self.default_formatter)(req, results, storable)
		
		frm = form.FormNode(self.name)
		frm(type='markup', value=content)
		return frm
	
	
	def default_formatter(self, req, results, storable):
		"""
		The default way to format the output of this field.
		"""
		query = {'__init__[item_id]':storable.get_id(),
				 '__init__[item_table]':storable.get_table(),
				}
		new_media_link = tags.a(href=req.get_path(req.prepath, 'detail/media/new?' + urllib.urlencode(query)))['Add Media']
		
		if(len(results) == 0):
			return tags.span()[new_media_link]
		
		def format_type(item):
			filesize = media.formatbytes(item.get('filesize', 0))
			return '%s %s %s (%s)' % (filesize, item['format'], item['type'], item['quality'])
		
		def format_status(item):
			full_path = os.path.join(req.app.upload_path, item['filename'])
			status = []
			try:
				finfo = os.stat(full_path)
				if(finfo.st_size != item['filesize']):
					status.append("wrong filesize")
				
				if(req.postpath[-1] == 'check-md5'):
					filehash = media.get_checksum(full_path, md5_path=req.app.md5_path)
				
					if(filehash != item['md5']):
						status.append("incorrect hash")
			except OSError, e:
				status.append(e.strerror)
			
			if(status):
				return tags.span(_class='error')[str(tags.br()).join(status)]
			else:
				return tags.span(_class='message')['OK']
		
		checksum_link = tags.a(href=req.get_path(req.prepath, 'detail', self.itemdef.name, storable.get_id(), 'check-md5') + "#media")['Verify Checksums']
		
		def _filename_na(filename):
			if not(filename):
				filename = 'n/a'
			return filename
		
		return checksum_link + " | " + new_media_link + tags.table(_class="listing-table")[
			[tags.tr()[[
				tags.th()['media id'],
				tags.th()['type'],
				tags.th()['filename'],
				tags.th()['status']
			]]] + [
			tags.tr()[[
				tags.td()[
					item['id']
				],
				tags.td()[
					format_type(item)
				],
				tags.td()[
					tags.a(href=req.get_path(req.prepath, 'detail/media', item['id']))[_filename_na(item['filename'])]
				],
				tags.td()[
					format_status(item)
				]
			]] for item in results
		]]
	
	
	def update_storable(self, req, form, storable):
		"""
		No operation.
		
		@see: L{modu.editable.define.definition.update_storable()}
		"""
		pass

