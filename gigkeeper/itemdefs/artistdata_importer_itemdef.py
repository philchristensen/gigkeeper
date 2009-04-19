# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu.editable import define

from gigkeeper.resource import artistdata_importer

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'artistdata-importer',
		label			= 'artistdata importer',
		category		= 'relationships',
		acl				= 'access admin',
		weight			= -10,
		resource		= artistdata_importer.Resource
	)
)
