# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select

from gigkeeper import editable
from gigkeeper.model import url

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'url',
		label			= 'URLs',
		acl				= 'access admin',
		category		= 'contact info',
		weight			= 2,
		model_class		= url.URL,
		title_column	= 'url',
	),
	
	item_id				= editable.ItemTitleField(
		label			= 'URL for:',
		flabel			= 'name',
		weight			= -4,
		listing			= True
	),
	
	url					= string.StringField(
		label			= 'url:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= url.URL_TYPES,
		search			= True,
		listing			= True,
	)
)
