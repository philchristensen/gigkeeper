# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select

from gigkeeper.model import company
from gigkeeper.editable import url

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'company',
		label			= 'companies',
		acl				= 'access admin',
		category		= 'contact info',
		weight			= 1,
		model_class		= company.Company,
		title_column	= 'name',
	),
	
	name				= string.StringField(
		label			= 'name:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= company.COMPANY_TYPES,
		search			= True,
		listing			= True,
		weight			= 2,
	),
	
	urls				= url.URLListField(
		label			= 'URLs:',
		weight			= 3,
	),
)
