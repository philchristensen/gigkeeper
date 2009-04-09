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
		category		='relationships',
		weight			= 2,
		model_class		= url.URL,
		title_column	= 'url',
		hidden			= True,
	),
	
	url_for				= editable.ItemTitleField(
		column			= 'item_id',
		label			= 'URL for:',
		flabel			= 'name',
		weight			= -4,
		listing			= True
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= url.URL_TYPES,
		default_value	= url.URL_TYPES.keys()[0],
		weight			= 1,
		search			= True,
		listing			= True,
	),
	
	url					= string.StringField(
		label			= 'url:',
		size			= 60,
		maxlength 		= 255,
		weight			= 2,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	item_id				= string.HiddenField(
		weight			= 100,
	),
	
	item_table			= string.HiddenField(
		weight			= 101,
	),
)
