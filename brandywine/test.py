#!/usr/bin/env python
# -*- coding: utf8 -*-
""" test.py - Tests for brandywine """
import os
from brandywine import *

# create the brandywine object
brw = BrandyWine(os.environ.get('ROTTEN_API_KEY'))

#brw.fetch_data(category='movies')
#brw.fetch_data(category='box_office')
#brw.fetch_data(category='in_theaters')
#brw.fetch_data(category='opening')
#brw.fetch_data(category='upcoming')

# fetch endpoint urls
#print brw.get_listdir_url()
#print brw.get_boxoffice_url()
#print brw.get_intheatres_url()
#print brw.get_opening_url()
#print brw.get_upcoming_url()

# fetch box office titles
print 'Box Office Titles: '
boxOfficeTitles = brw.fetch_box_office_titles()
for title in boxOfficeTitles:
  print title

print '\n'

# fetch in theatres titles
print 'In Theaters Titles: '
inTheatersTitles = brw.fetch_intheaters_titles()
for title in inTheatersTitles:
  print title

brw.fetch_movie_data('771317257')

# return the list directory json
#jsonlist = brw.return_list_directory_json()
#print jsonlist

#movieslist = brw.return_movies_list_json()

#for movie in movieslist['movies']:
#    print movie['title']
