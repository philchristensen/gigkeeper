# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import datetime

from modu import util
from modu.editable import define
from modu.editable.datatypes import string, boolean, date
from modu.editable.datatypes import relational, fck, select

from gigkeeper import editable
from gigkeeper.model import history

def history_prewrite_callback(req, frm, storable):
	if(storable.get_id() == 0):
		storable.user_id = req.user.get_id()

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'history',
		label			= 'event log',
		acl				= 'access admin',
		category		= 'relationships',
		weight			= 2,
		model_class		= history.History,
		hidden			= True,
		prewrite_callback = history_prewrite_callback,
	),
	
	history_for			= editable.ItemTitleField(
		column			= 'item_id',
		label			= 'History for:',
		flabel			= 'name',
		weight			= 1,
		listing			= True
	),
	
	user_id				= relational.ForeignLabelField(
		label			= 'created by:',
		ftable			= 'user',
		flabel			= 'username',
		fvalue			= 'id',
		weight			= 2,
	),
	
	contact_id			= relational.ForeignAutocompleteField(
		label			= 'contact:',
		ftable			= 'contact',
		flabel			= 'name',
		fvalue			= 'id',
		weight			= 3,
		autocomplete_callback = editable.contact_autocomplete_callback,
	),
	
	type				= select.SelectField(
		label			= 'type:',
		options			= history.HISTORY_TYPES,
		weight			= 4,
		search			= True,
		listing			= True,
		required		= True,
	),
	
	summary				= string.StringField(
		label			= 'summary:',
		size			= 60,
		maxlength 		= 255,
		weight			= 5,
		listing			= True,
		link			= True,
		search			= True,
	),
	
	description			= string.TextAreaField(
		label			= 'description:',
		rows			= 8,
		cols			= 70,
		weight			= 6,
	),
	
	created_date		= date.CurrentDateField(
		label			= 'created date:',
		save_format		= 'datetime',
		default_checked	= True,
		weight			= 7,
	),
	
	item_id				= string.HiddenField(
		weight			= 100,
	),
	
	item_table			= string.HiddenField(
		weight			= 101,
	),
)
