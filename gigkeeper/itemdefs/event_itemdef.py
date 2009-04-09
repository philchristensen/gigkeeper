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
from gigkeeper.editable import url, note, history

def contact_callback(req, frm, storable):
	return storable.contact_id

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'event',
		label			= 'events',
		acl				= 'access admin',
		category		= 'relationships',
		weight			= 3,
		model_class		= event.Event,
		title_column	= 'name',
	),
	
	name				= string.StringField(
		label			= 'summary:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1,
		listing			= True,
		link			= True,
		search			= True,
		required		= True,
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
		required		= True,
	),
	
	scheduled_date		= date.DateField(
		label			= 'scheduled date:',
		style			= 'date',
		save_format		= 'datetime',
		listing			= True,
		weight			= 3.5,
		required		= True,
	),
	
	created_date		= date.CurrentDateField(
		label			= 'created date:',
		save_format		= 'datetime',
		default_checked	= True,
		weight			= 3.7,
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
	
	history				= history.HistoryListField(
		label			= 'History:',
		weight			= 5.2,
		contact_callback= contact_callback,
	),
	
	urls				= url.URLListField(
		label			= 'URLs:',
		weight			= 6,
	),
	
	notes				= note.NoteListField(
		label			= 'notes:',
		weight			= 7,
	),
)
