# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, fck, select

from gigkeeper import editable
from gigkeeper.model import note

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'note',
		label			= 'notes',
		acl				= 'access admin',
		category		= 'contact info',
		weight			= 2,
		model_class		= note.Note,
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
	
	description			= string.TextAreaField(
		label			= 'description:',
		rows			= 8,
		cols			= 70,
		weight			= 3,
	),
	
	item_id				= string.HiddenField(
		weight			= 100,
	),
	
	item_table			= string.HiddenField(
		weight			= 101,
	),
)