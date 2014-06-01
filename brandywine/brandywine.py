#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Brandywine is cool.

To register for the Rotten Tomatoes API, visit
http://developer.rottentomates.com/.  Be sure to set the ROTTEN_API_KEY as a
local environment variable.
"""
import urllib2

class BrandyWine(object):
    """
    Class definition for BrandyWine
    """
    API_URL = 'http://api.rottentomatoes.com/api/public/v1.0/lists/' \
               + 'movies.json?apikey='

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

    def get_api_url(self):
        """
        return the full URL used with the ROTTEN TOMATOES API
        """
        return str(self.API_URL) + str(self.key)

    def movie_search(self, title):
        """
        performs a search for movies by name
        """
        pass

    def get_lists(self):
        """
        returns the URLs in JSON for the list directories
        """
        pass

    def get_movie_lists(self):
        """
        returns the URLs in JSON for the movie list directories
        """
        pass
