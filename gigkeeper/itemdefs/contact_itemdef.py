# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select, relational

from gigkeeper.model import contact
from gigkeeper.editable import url, note

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'contact',
		label			= 'contacts',
		acl				= 'access admin',
		category		= 'contact info',
		weight			= 1,
		model_class		= contact.Contact,
		title_column	= 'name',
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
	
	company_id			= relational.ForeignSelectField(
		label			= 'company:',
		weight			= 3,
		listing			= True,
		ftable			= 'company',
		flabel			= 'name',
		fvalue			= 'id',
		order_by		= 'name'
	),
	
	address_id			= string.LabelField(
		label			= 'address:',
		help			= "Not yet implemented.",
		weight			= 4,
	),
	
	phone				= string.StringField(
		label			= 'phone:',
		size			= 60,
		maxlength 		= 255,
		weight			= 5,
		listing			= True,
	),
	
	email				= string.StringField(
		label			= 'email:',
		size			= 60,
		maxlength 		= 255,
		weight			= 6,
		listing			= True,
	),
)
