#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Brandywine is cool. It allows you to fetch movie reviews right from the command
line.

To register for the Rotten Tomatoes API, visit
http://developer.rottentomates.com/.  Be sure to set a local environment variable called ROTTEN_API_KEY to the application key generated for you after regstering.
"""
import os
import urllib2, json
import argparse

class BrandyWine(object):
    """
    Class definition for BrandyWine
    """
    BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/lists/'
    MOVIE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/movies/'
    SEARCH_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'

    def __init__(self, options):
        """ Constructor """
        self.key = os.environ.get('ROTTEN_API_KEY')
        self.options = options

        if options['boxoffice'] == True:
            self.fetch_box_office_titles()

        if options['intheaters'] == True:
            self.fetch_intheaters_titles()

        if options['search'] != None:
            self.movie_search(options['search'])

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
        passes json data about box office movies
        """
        jsondata = self.fetch_data(category='box_office')
        self.format_json_response(jsondata, infotype='title')

    def fetch_intheaters_titles(self):
        """
        passes json data about in theaters movies
        """
        jsondata = self.fetch_data(category='in_theaters')
        self.format_json_response(jsondata, infotype='title')

    def movie_search(self, title):
        """
        performs a search for movies by name
        """
        results = []
        jsondata = self.fetch_data(category='search', query=title)
        self.format_json_response(jsondata, infotype='all')

        """ for movie in jsondata['movies']:
          for entry in movie:
              print entry.encode('utf-8') + ': ' + str(movie[entry]) """

    def fetch_movie_data(self, movie_id):
        """
        returns all information about the requested movie
        """
        url = self.MOVIE_URL + '%s.json?apikey=%s' % (movie_id, str(self.key))

        return json.load(urllib2.urlopen(url))

    def fetch_data(self, **kwargs):
        """
        a better way to fetch the json data from rotten tomatoes api
        """
        for key in kwargs.keys():
            if kwargs['category'] == 'movies':
                url = self.BASE_URL + '%s.json?apikey=%s' % \
                ('movies', str(self.key))
            elif kwargs['category'] == 'search':
                url = self.SEARCH_URL + '%s.json?apikey=%s&q=%s' % \
                ('movies', str(self.key), kwargs['query'])
            else:
                url = self.BASE_URL + 'movies/%s.json?apikey=%s' % \
                (kwargs['category'], str(self.key))

        return json.load(urllib2.urlopen(url))

    def format_json_response(self, response, infotype):
        """
        format the json response from the Rotten Tomatoes API call
        """
        if infotype == 'title':
            movies = []
            for movie in response['movies']:
                movies.append('==> ' + movie['title'] + \
                    ', ID: ' + str(movie['id']) + \
                    ', Rating: ' + str(movie['ratings']['critics_rating']) + \
                    ', Score: ' + str(movie['ratings']['critics_score']))

            # Remove unicode
            movie_titles = [title.encode('utf-8') for title in movies]
            for movie in movie_titles: print movie
        elif infotype == 'score':
            movies = []
            for movie in response['movies']:
                movies.append('==>' + movie['title'])
            print movies
        else:
            for movie in response['movies']:
                for entry in movie:
                    print entry + ': ' + str(movie[entry])



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rotten Tomatoes cli')
    parser.add_argument('-b', '--boxoffice', \
        action='store_true', help='lists current box office movies.')
    parser.add_argument('-t', '--intheaters', \
        action='store_true', help='lists movies currently in theaters.')
    parser.add_argument('-s', '--search', \
        metavar='movie', help='query the movie database')
    args = parser.parse_args()
    brw = BrandyWine(vars(args))
