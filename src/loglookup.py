#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  callsign-lookup-0_2.py
#  
#  Copyright 2017 Bill Hammond <ka1ssr@ernie>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#	Revision History:
#
#	20170113 - WSH - initial code
#	20170121 - WSH - added better comments
#       20170528 - WSH - ported to NetBeans


from qrz import QRZ

def print_keys(key_names, query_result): # define the print_keys function
	info = ""
	for key_name in key_names:
		if key_name in query_result:
			info += query_result[key_name] + " "
	print info
		
# Open the log file for read access
fhand = open('/home/ka1ssr/NetBeansProjects/LogLookup/DStarRepeater-2017-01-07.log')

for line in fhand:
	key = line[42:45] # extract characters 42 through 45
	if key == 'My:':
		callsign = line[46:52] # callsign is characters 46 through 52
		qrz = QRZ('/home/ka1ssr/pyQRZ/settings.cfg')
		result = qrz.callsign(callsign) # pass callsign to qrz
		print callsign
		print_keys(['fname', 'name'], result) # print first & last name
		print_keys(['addr2', 'state'], result) # print City & State
		print_keys(['country'], result) # print country
		print '\n' # newline
	continue # grab the next line in the log file