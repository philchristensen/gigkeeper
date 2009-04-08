# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck
from modu.editable.datatypes import date, select, relational

from gigkeeper.model import event
from gigkeeper.editable import url, note

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'event',
		label			= 'events',
		acl				= 'access admin',
		category		= 'booking',
		weight			= 1,
		model_class		= event.Event,
		title_column	= 'summary',
	),
	
	summary				= string.StringField(
		label			= 'summary:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	description			= string.TextAreaField(
		label			= 'description:',
		weight			= 2,
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= event.EVENT_TYPES,
		weight			= 3,
		search			= True,
		listing			= True,
	),
	
	scheduled_date		= date.DateField(
		label			= 'scheduled date:',
		style			= 'date',
		save_format		= 'datetime',
		listing			= True,
		weight			= 3.5,
	),
	
	created_date		= date.DateField(
		label			= 'created date:',
		style			= 'date',
		save_format		= 'datetime',
		default_now		= True,
		weight			= 3.7,
		help			= 'This field will automatically be set when the record is saved for the first time.',
	),
	
	company_id			= relational.ForeignSelectField(
		label			= 'venue:',
		weight			= 4,
		listing			= True,
		ftable			= 'company',
		flabel			= 'name',
		fvalue			= 'id',
		fwhere			= dict(type='venue'),
		order_by		= 'name'
	),
	
	contact_id			= relational.ForeignSelectField(
		label			= 'booking contact:',
		weight			= 5,
		listing			= True,
		ftable			= 'contact',
		flabel			= 'name',
		fvalue			= 'id',
		order_by		= 'name'
	),
	
)
