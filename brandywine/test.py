#!/usr/bin/env python
# -*- coding: utf8 -*-
""" test.py - Tests for brandywine """
import os
from brandywine import *

# create the brandywine object
brw = BrandyWine(os.environ.get('ROTTEN_API_KEY'))


# fetch endpoint urls
#print brw.get_listdir_url()
#print brw.get_boxoffice_url()
#print brw.get_intheatres_url()
#print brw.get_opening_url()
#print brw.get_upcoming_url()

# fetch box office titles
boxOfficeTitles = brw.fetch_box_office_titles()
print boxOfficeTitles

# fetch in theatres titles
inTheatresTitles = brw.fetch_intheatres_titles()
print inTheatresTitles

# return the list directory json
#jsonlist = brw.return_list_directory_json()
#print jsonlist

#movieslist = brw.return_movies_list_json()

#for movie in movieslist['movies']:
#    print movie['title']
