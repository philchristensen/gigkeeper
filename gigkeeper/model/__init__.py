# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from gigkeeper.model import url

class ModelURLMixin(object):
	def get_url(self, type='homepage'):
		attribs = dict(
			item_id		= self.get_id(),
			item_table	= self.get_table(),
		)
		
		if(type is not None):
			attribs['type'] = type
		
		store = self.get_store()
		store.ensure_factory('url', model_class=url.URL)
		u = store.load_one('url', attribs)
		
		if(u is None):
			return ''
		
		return u.url