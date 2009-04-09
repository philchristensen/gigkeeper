# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import os.path

from zope.interface import classProvides

from twisted import plugin

from modu import assets
from modu.web import app, static
from modu.editable import resource
from modu.editable.datatypes import fck

from gigkeeper.resource import index

def admin_site_stylesheet_callback(req):
	return req.get_path('gigkeeper-assets/admin-styles.css')

class Site(object):
	classProvides(plugin.IPlugin, app.ISite)
	
	def configure_request(self, req):
		compiled_template_root = os.path.join(req.approot, 'var')
		if(os.path.exists(compiled_template_root)):
			req.app.config['compiled_template_root'] = compiled_template_root
	
	def initialize(self, application):
		application.base_domain = 'localhost'
		application.db_url = 'MySQLdb://gigkeeper:Mekdeap7@localhost/gigkeeper'
		
		application.activate('/assets', static.FileResource, os.path.dirname(assets.__file__))
		
		import gigkeeper
		compiled_template_root = os.path.abspath(os.path.join(os.path.dirname(gigkeeper.__file__), '../var'))
		if(os.path.exists(compiled_template_root)):
			application.compiled_template_root = compiled_template_root
		
		gigkeeper_assets_root = os.path.abspath(os.path.join(os.path.dirname(gigkeeper.__file__), 'assets'))
		application.activate('/gigkeeper-assets', static.FileResource, gigkeeper_assets_root)
		
		import gigkeeper.itemdefs
		application.activate('/admin', resource.AdminResource, default_path='admin/listing/page', itemdef_module=gigkeeper.itemdefs)
		application.admin_site_stylesheet = admin_site_stylesheet_callback
		
		application.activate('/fck', fck.FCKEditorResource)
		application.activate('/', index.Resource)
