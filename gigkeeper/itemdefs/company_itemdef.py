# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select

from gigkeeper.model import company
from gigkeeper.editable import url, note

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
	
	type				= select.SelectField(
		label			= 'type:',
		options			= company.COMPANY_TYPES,
		search			= True,
		listing			= True,
		weight			= 1,
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
	
	urls				= url.URLListField(
		label			= 'URLs:',
		weight			= 3,
	),
	
	notes				= note.NoteListField(
		label			= 'notes:',
		weight			= 3,
	),
)
