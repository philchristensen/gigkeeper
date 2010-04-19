# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select

from gigkeeper.model import company
from gigkeeper.editable import url, note, address, history, contact

def address_name_callback(req, frm, storable):
	return storable.name

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'company',
		label			= 'companies',
		acl				= 'access admin',
		category		='relationships',
		weight			= 2,
		model_class		= company.Company,
		title_column	= 'name',
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= company.COMPANY_TYPES,
		search			= True,
		listing			= True,
		weight			= 1,
		required		= True,
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
	
	phone				= string.StringField(
		label			= 'phone:',
		size			= 60,
		maxlength 		= 255,
		weight			= 2,
		listing			= True,
	),
	
	contacts			= contact.CompanyContactListField(
		label			= 'Contacts:',
		weight			= 2.1,
	),
	
	history				= history.GenericHistoryListField(
		label			= 'History:',
		weight			= 2.2,
	),
	
	event_history		= history.EventHistoryListField(
		label			= 'Event History:',
		weight			= 2.3,
	),
	
	addresses			= address.AddressListField(
		label			= 'Addresses:',
		weight			= 2.5,
		address_name_callback = address_name_callback,
	),
	
	urls				= url.URLListField(
		label			= 'URLs:',
		weight			= 3,
	),
	
	notes				= note.NoteListField(
		label			= 'notes:',
		weight			= 4,
	),
)
