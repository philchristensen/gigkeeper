#!/usr/bin/env python

# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

"""
Gigkeeper Database

This script will update the specified site's database with content from ArtistData.
"""

import sys, os.path, warnings

warnings.simplefilter('ignore', RuntimeWarning)
warnings.simplefilter('ignore', DeprecationWarning)

from twisted.python import usage

from modu.persist import dbapi, Store

sys.path.append('.')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modu.sites import seaflux_site

from gigkeeper.util import artistdata

class Options(usage.Options):
	"""
	Implement usage parsing for the export_ioda.py script.
	"""
	optParameters = []
	
	optFlags = [['debug', 'd', 'Debug queries to the database.'],
				]

if(__name__ == '__main__'):
	config = Options()
	try:
		config.parseOptions()
	except usage.UsageError, e:
		print >>sys.stderr, '%s: %s\nTry --help for usage details.' % (sys.argv[0], e)
		sys.exit(1)
	
	if(config['debug']):
		dbapi.debug = True
	
	pool = dbapi.connect(seaflux_site.db_url)
	store = Store(pool)
	
	artistdata.sync_shows(store)
