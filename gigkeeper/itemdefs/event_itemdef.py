# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck
from modu.editable.datatypes import date, select, relational

from modu.editable.util import get_url_code_callback

from gigkeeper import editable
from gigkeeper.model import event
from gigkeeper.editable import url, note, history, media

def contact_callback(req, frm, storable):
	return getattr(storable, 'contact_id', None)

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'event',
		label			= 'events',
		acl				= 'access admin',
		category		= 'relationships',
		weight			= 3,
		model_class		= event.Event,
		title_column	= 'name',
		prewrite_callback	= get_url_code_callback('name', 'url_code')
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
	
	url_code			= string.StringField(
		label			= 'url code:',
		weight			= 1.25,
	),
	
	artistdata_id		= string.StringField(
		label			= 'artistdata ident:',
		size			= 60,
		maxlength 		= 255,
		weight			= 1.5,
		help			= "do not set or change this unless you know what you're doing!",
	),
	
	description			= string.TextAreaField(
		label			= 'description:',
		weight			= 2,
	),
	
	cover_fee			= string.StringField(
		label			= 'cover fee:',
		size			= 10,
		weight			= 2.5,
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
		style			= 'datetime',
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
	
	company_link		= editable.ItemTitleField(
		column			= 'company_id',
		label			= 'venue link:',
		flabel			= 'name',
		ftable			= 'company',
		weight			= 3.8,
		listing			= True
	),
	
	company_id			= relational.ForeignSelectField(
		label			= 'venue:',
		weight			= 4,
		ftable			= 'company',
		flabel			= 'name',
		fvalue			= 'id',
		fwhere			= dict(type='venue'),
		order_by		= 'name'
	),
	
	contact_link		= editable.ItemTitleField(
		column			= 'contact_id',
		label			= 'contact link:',
		flabel			= 'name',
		ftable			= 'contact',
		weight			= 4.5,
		listing			= True
	),
	
	contact_id			= relational.ForeignSelectField(
		label			= 'booking contact:',
		weight			= 5,
		ftable			= 'contact',
		flabel			= 'name',
		fvalue			= 'id',
		order_by		= 'name'
	),
	
	media				= media.MediaListField(
		label			= 'media:',
		weight			= 5.1,
	),
	
	history				= history.GenericHistoryListField(
		label			= 'history:',
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
