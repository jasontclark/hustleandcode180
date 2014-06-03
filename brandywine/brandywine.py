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
    BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/lists/'
    LISTS_URL = BASE_URL + 'movies.json?apikey='
    MOVIES_URL = BASE_URL + 'movies/box_office.json?apikey='

    def __init__(self, key):
        """ Constructor """
        self.key = key

    def __str__(self):
        """ Print method """
        return str(self.key)

    def get_api_key(self):
        """
        returns the value of your ROTTEN TOMATOES API KEY
        """
        return self.key

    def get_list_url(self):
        """
        return the LIST URL used with the ROTTEN TOMATOES API
        """
        return str(self.LISTS_URL) + str(self.key)

    def get_movies_url(self):
        """
        return the MOVIES URL used with the ROTTEN TOMATOES API
        """
        return str(self.MOVIES_URL) + str(self.key)

    def movie_search(self, title):
        """
        performs a search for movies by name
        """
        pass

    def return_list_directory_json(self):
        """
        returns the URLs in JSON for the list directories
        """
        response = urllib2.urlopen(self.get_list_url())
        jsdata = json.load(response)
        return jsdata

    def return_movies_list_json(self):
        """
        returns the movies in JSON for the movie list directories
        """
        response = urllib2.urlopen(self.get_movies_url())
        jsdata = json.load(response)
        return jsdata
