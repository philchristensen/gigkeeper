# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean
from modu.editable.datatypes import date, fck, select

import gigkeeper
from gigkeeper import editable
from gigkeeper.model import address

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'address',
		label			= 'addresses',
		acl				= 'access admin',
		category		='relationships',
		weight			= 2,
		model_class		= address.Address,
		hidden			= True,
	),
	
	address_for			= editable.ItemTitleField(
		column			= 'item_id',
		label			= 'Address for:',
		flabel			= 'name',
		weight			= -4,
		listing			= True
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= address.ADDRESS_TYPES,
		weight			= 1,
		search			= True,
		listing			= True,
	),
	
	name				= string.StringField(
		label			= 'name:',
		size			= 60,
		maxlength 		= 255,
		weight			= 2,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	address1			= string.StringField(
		label			= 'address 1:',
		size			= 60,
		maxlength 		= 255,
		weight			= 3,
		listing			= True,
		link			= True,
	),
	
	address2			= string.StringField(
		label			= 'address 2:',
		size			= 60,
		maxlength 		= 255,
		weight			= 4,
	),
	
	city				= string.StringField(
		label			= 'city:',
		size			= 60,
		maxlength 		= 255,
		weight			= 5,
		listing			= True,
	),
	
	region				= select.SelectField(
		label			= 'state:',
		options			= gigkeeper.states,
		weight			= 6,
		listing			= True,
	),
	
	zip				= string.StringField(
		label			= 'zip:',
		size			= 60,
		maxlength 		= 255,
		weight			= 7,
		listing			= True,
	),
	
	country				= select.SelectField(
		label			= 'country:',
		options			= gigkeeper.countries,
		default_value	= 'US',
		weight			= 8,
	),
	
	item_id				= string.HiddenField(
		weight			= 100,
	),
	
	item_table			= string.HiddenField(
		weight			= 101,
	),
)
