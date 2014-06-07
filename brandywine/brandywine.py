#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Brandywine is cool. It allows you to fetch movie reviews right from the command
line.

To register for the Rotten Tomatoes API, visit
http://developer.rottentomates.com/.  Be sure to set the ROTTEN_API_KEY as a
local environment variable.
"""
import urllib2, json

class BrandyWine(object):
    """
    Class definition for BrandyWine
    """
    global RESPONSE

    BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/lists/'

    def __init__(self, key):
        """ Constructor """
        self.key = key

    def get_api_key(self):
        """
        returns the value of your ROTTEN TOMATOES API KEY
        """
        return self.key

    def get_listdir_url(self):
        """
        return the LIST URL used with the ROTTEN TOMATOES API
        """
        return self.BASE_URL + '%s.json' % 'movies' + \
               '?apikey=%s' % str(self.key)

    def get_boxoffice_url(self):
        """
        return the BOX OFFICE URL used with the ROTTEN TOMATOES API
        """
        return self.BASE_URL + 'movies/%s.json' % 'box_office' + \
               '?apikey=%s' % str(self.key)

    def get_intheaters_url(self):
        """
        return the IN theaters URL used with the ROTTEN TOMATOES API
        """
        return self.BASE_URL + 'movies/%s.json' % 'in_theaters' + \
               '?apikey=%s' % str(self.key)

    def get_opening_url(self):
        return self.BASE_URL + 'movies/%s.json' % 'opening' + \
               '?apikey=%s' % str(self.key)

    def get_upcoming_url(self):
        return self.BASE_URL + 'movies/%s.json' % 'upcoming' + \
               '?apikey=%s' % str(self.key)

    def return_list_directory_json(self):
        """
        returns the URLs in JSON for the list directories
        """
        response = urllib2.urlopen(self.get_list_url())
        jsdata = json.load(response)
        return jsdata

    def fetch_box_office_titles(self):
        """
        returns (array) the box office movie titles
        """
        movies = []
        response = urllib2.urlopen(self.get_boxoffice_url())
        jsondata = json.load(response)

        for movie in jsondata['movies']:
            movies.append(movie['title'])

        # Remove unicode
        movieTitles = [title.encode('utf-8') for title in movies]

        return movieTitles

    def fetch_intheaters_titles(self):
        """
        returns (array) the in theaters movie titles
        """
        movies = []
        response = urllib2.urlopen(self.get_intheaters_url())
        jsondata = json.load(response)

        for movie in jsondata['movies']:
            movies.append(movie['title'])

        # Remove unicode
        movieTitles = [title.encode('utf-8') for title in movies]

        return movieTitles

    def movie_search(self, title):
        """
        performs a search for movies by name
        """
        pass

    def fetch_data(self, **kwargs):
        """
        a better way to fetch the json data from rotten tomatoes api
        """
        global RESPONSE

        for key in kwargs.keys():
          if kwargs['category'] == 'movies':
              url = self.BASE_URL + '%s.json?apikey=%s' % \
              ('movies', str(self.key))
          else:
              url = self.BASE_URL + 'movies/%s.json?apikey=%s' % \
              (kwargs['category'], str(self.key))

        RESPONSE = json.load(urllib2.urlopen(url))

        print url
        print RESPONSE
