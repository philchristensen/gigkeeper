# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select, relational

from gigkeeper import editable
from gigkeeper.model import contact
from gigkeeper.editable import url, note, address, history

def contact_callback(req, frm, storable):
	return storable.get_id()

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'contact',
		label			= 'contacts',
		acl				= 'access admin',
		category		='relationships',
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
		required		= True,
	),
	
	company_link		= editable.ItemTitleField(
		column			= 'company_id',
		label			= 'company link:',
		flabel			= 'name',
		ftable			= 'company',
		weight			= 2.5,
		listing			= True
	),
	
	company_id			= relational.ForeignSelectField(
		label			= 'company:',
		weight			= 3,
		ftable			= 'company',
		flabel			= 'name',
		fvalue			= 'id',
		order_by		= 'name'
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
	
	history				= history.GenericHistoryListField(
		label			= 'History:',
		weight			= 2.2,
		contact_callback= contact_callback,
	),
	
	event_history		= history.EventHistoryListField(
		label			= 'Event History:',
		weight			= 2.3,
	),
	
	addresses			= address.AddressListField(
		label			= 'Addresses:',
		weight			= 6.5,
	),
	
	urls				= url.URLListField(
		label			= 'URLs:',
		weight			= 7,
	),
	
	notes				= note.NoteListField(
		label			= 'notes:',
		weight			= 8,
	),
)
