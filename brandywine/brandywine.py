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

    def __init__(self, key):
        """ Constructor """
        self.key = key

    def get_api_key(self):
        """
        returns the value of your ROTTEN TOMATOES API KEY
        """
        return self.key

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
        jsondata = self.fetch_data(category='box_office')

        for movie in jsondata['movies']:
            movies.append('==> ' + movie['title'] + \
                ', Rating: ' + str(movie['ratings']['critics_rating']) + \
                ', Score: ' + str(movie['ratings']['critics_score']))

        # Remove unicode
        movie_titles = [title.encode('utf-8') for title in movies]

        return movie_titles

    def fetch_intheaters_titles(self):
        """
        returns (array) the in theaters movie titles
        """
        movies = []
        jsondata = self.fetch_data(category='in_theaters')

        for movie in jsondata['movies']:
            movies.append('==> ' + movie['title'] + \
                ', Rating: ' + str(movie['ratings']['critics_rating']) + \
                ', Score: ' + str(movie['ratings']['critics_score']))

        # Remove unicode
        movie_titles = [title.encode('utf-8') for title in movies]

        return movie_titles

    def movie_search(self, title):
        """
        performs a search for movies by name
        """
        pass

    def fetch_data(self, **kwargs):
        """
        a better way to fetch the json data from rotten tomatoes api
        """
        for key in kwargs.keys():
            if kwargs['category'] == 'movies':
                url = self.BASE_URL + '%s.json?apikey=%s' % \
                ('movies', str(self.key))
            else:
                url = self.BASE_URL + 'movies/%s.json?apikey=%s' % \
                (kwargs['category'], str(self.key))

        return json.load(urllib2.urlopen(url))
