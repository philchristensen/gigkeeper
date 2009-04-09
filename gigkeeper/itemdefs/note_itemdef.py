# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean
from modu.editable.datatypes import date, fck, select

from gigkeeper import editable
from gigkeeper.model import note

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'note',
		label			= 'notes',
		acl				= 'access admin',
		category		='relationships',
		weight			= 2,
		model_class		= note.Note,
		hidden			= True,
	),
	
	note_for			= editable.ItemTitleField(
		column			= 'item_id',
		label			= 'Note for:',
		flabel			= 'name',
		weight			= -4,
		listing			= True
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= note.NOTE_TYPES,
		weight			= 1,
		search			= True,
		listing			= True,
	),
	
	summary				= string.StringField(
		label			= 'summary:',
		size			= 60,
		maxlength 		= 255,
		weight			= 2,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	description			= fck.FCKEditorField(
		label			= 'description:',
		rows			= 8,
		cols			= 70,
		weight			= 3,
	),
	
	created_date		= date.CurrentDateField(
		label			= 'created date:',
		save_format		= 'datetime',
		default_checked	= True,
		weight			= 3.5,
	),
	
	item_id				= string.HiddenField(
		weight			= 100,
	),
	
	item_table			= string.HiddenField(
		weight			= 101,
	),
)
