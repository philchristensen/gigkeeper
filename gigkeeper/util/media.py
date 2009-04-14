# gigkeeper
# Copyright (C) 2008 gigkeeper
#
# $Id$
#

import os

from modu.util import OrderedDict as odict

extension_map = odict([
	('.jpg'		, ('image', 'jpeg', 'master')),
])

def get_checksum(filepath, md5_path='md5sum'):
	handle = os.popen(md5_path + ' ' + filepath.replace(r';', r'\;'))
	filehash = handle.read()
	handle.close()
	
	if(filehash.find('=') == -1):
		filehash = [output.strip() for output in filehash.split(' ')][0]
	else:
		filehash = [output.strip() for output in filehash.split('=')][1]
	
	return filehash

def get_media_details(filename):
	media_type, format, quality = ('', '', '')
	for ext, settings in extension_map.items():
		if(filename.endswith(ext)):
			media_type, format, quality = settings
			break
	return media_type, format, quality

###############################################################
# formatbytes takes a filesize (as returned by os.getsize() )
# and formats it for display in one of two ways !!
# Stolen from http://www.voidspace.org.uk/python/pathutils.html

def formatbytes(sizeint, configdict=None, **configs):
	"""
	Given a file size as an integer, return a nicely formatted string that
	represents the size. Has various options to control it's output.
	
	You can pass in a dictionary of arguments or keyword arguments. Keyword
	arguments override the dictionary and there are sensible defaults for options
	you don't set.
	
	Options and defaults are as follows :
	
	*	 ``forcekb = False`` -		   If set this forces the output to be in terms
	of kilobytes and bytes only.
	
	*	 ``largestonly = True`` -	 If set, instead of outputting 
		``1 Mbytes, 307 Kbytes, 478 bytes`` it outputs using only the largest 
		denominator - e.g. ``1.3 Mbytes`` or ``17.2 Kbytes``
	
	*	 ``kiloname = 'Kbytes'`` -	  The string to use for kilobytes
	
	*	 ``meganame = 'Mbytes'`` - The string to use for Megabytes
	
	*	 ``bytename = 'bytes'`` -	  The string to use for bytes
	
	*	 ``nospace = True`` -		 If set it outputs ``1Mbytes, 307Kbytes``, 
		notice there is no space.
	
	Example outputs : ::
	
		19Mbytes, 75Kbytes, 255bytes
		2Kbytes, 0bytes
		23.8Mbytes
	
	.. note::
	
		It currently uses the plural form even for singular.
	"""
	defaultconfigs = {	'forcekb' : False,
						'largestonly' : True,
						'kiloname' : 'KB',
						'meganame' : 'MB',
						'bytename' : 'B',
						'nospace' : True}
	if configdict is None:
		configdict = {}
	for entry in configs:
		# keyword parameters override the dictionary passed in
		configdict[entry] = configs[entry]
	#
	for keyword in defaultconfigs:
		if not configdict.has_key(keyword):
			configdict[keyword] = defaultconfigs[keyword]
	#
	if configdict['nospace']:
		space = ''
	else:
		space = ' '
	#
	if(sizeint is None):
		sizeint = 0
	mb, kb, rb = bytedivider(sizeint)
	if configdict['largestonly']:
		if mb and not configdict['forcekb']:
			return stringround(mb, kb)+ space + configdict['meganame']
		elif kb or configdict['forcekb']:
			if mb and configdict['forcekb']:
				kb += 1024*mb
			return stringround(kb, rb) + space+ configdict['kiloname']
		else:
			return str(rb) + space + configdict['bytename']
	else:
		outstr = ''
		if mb and not configdict['forcekb']:
			outstr = str(mb) + space + configdict['meganame'] +', '
		if kb or configdict['forcekb'] or mb:
			if configdict['forcekb']:
				kb += 1024*mb
			outstr += str(kb) + space + configdict['kiloname'] +', '
		return outstr + str(rb) + space + configdict['bytename']

def stringround(main, rest):
	"""
	Given a file size in either (mb, kb) or (kb, bytes) - round it
	appropriately.
	"""
	# divide an int by a float... get a float
	value = main + rest/1024.0
	return str(round(value, 1))

def bytedivider(nbytes):
	"""
	Given an integer (probably a long integer returned by os.getsize() )
	it returns a tuple of (megabytes, kilobytes, bytes).
	
	This can be more easily converted into a formatted string to display the
	size of the file.
	"""
	mb, remainder = divmod(nbytes, 1048576)
	kb, rb = divmod(remainder, 1024)
	return (mb, kb, rb)

########################################
