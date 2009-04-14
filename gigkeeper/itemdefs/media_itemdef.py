# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import os, os.path

from modu.util import tags
from modu.editable import define
from modu.editable.datatypes import string, select, boolean, fck, date

from gigkeeper.model import media
from gigkeeper.util.media import get_media_details, get_checksum
from gigkeeper import editable

def media_prewrite_callback(req, frm, storable):
	filename = getattr(storable, 'filename', '')
	if(filename):
		storable.type, storable.format, storable.quality = get_media_details(filename)
		
		if not(storable.type and storable.format and storable.quality):
			req.messages.report('error', "Sorry, %s is not a supported file type." % filename)
			return False
		
		full_path = os.path.join(req.app.upload_path, filename)
		
		storable.md5 = get_checksum(full_path, md5_path=req.app.md5_path)
		
		st_info = os.stat(full_path)
		storable.filesize = st_info.st_size
	return True

__itemdef__ = define.itemdef(
	__config			= dict(
		name			= 'media',
		acl				= 'access admin',
		weight			= 100,
		model_class		= media.Media,
		prewrite_callback = media_prewrite_callback,
		hidden			= True,
	),
	
	id					= string.LabelField(
		label			= 'id:',
		help			= 'the internal id of this item.',
		weight			= -10,
		listing			= True,
	),
	
	item_title			= editable.ItemTitleField(
		column			= 'item_id',
		label			= 'media for:',
		flabel			= 'name',
		listing			= True,
		weight			= 2,
	),
	
	filename			= fck.FCKFileField(
		label			= 'filename:',
		fck_root		= '/fck/content',
		listing			= True,
		link			= True,
		weight			= 3,
	),
	
	created_date		= date.CurrentDateField(
		label			= 'created date:',
		style			= 'datetime',
		save_format		= 'datetime',
		default_checked	= True,
		weight			= 5,
	),
	
	item_table			= string.LabelValueField(
		label			= 'from table:',
		listing			= True,
		weight			= 6,
	),
	
	type				= string.LabelField(
		label			= 'media type:',
		listing			= True,
		weight			= 6.5,
		help			= 'This field will be updated on save',
	),
	
	format				= string.LabelField(
		label			= 'media format:',
		weight			= 7,
		help			= 'This field will be updated on save',
	),
	
	quality				= string.LabelField(
		label			= 'media quality:',
		weight			= 8,
		help			= 'This field will be updated on save',
	),
	
	filesize			= string.LabelField(
		label			= 'file size:',
		weight			= 9,
		help			= 'This field will be updated on save',
	),
	
	md5					= string.LabelField(
		label			= 'checksum:',
		weight			= 10,
		help			= 'This field will be updated on save',
	),
)
