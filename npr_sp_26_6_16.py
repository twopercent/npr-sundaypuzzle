#!/bin/env python3

import os
import dbf

STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


#GeoNames
GEONAMES_ZIP = "POP_PLACES_20160601.zip"
GEONAMES_TXT = "POP_PLACES_20160601.txt"
GEONAMES_URL = "http://geonames.usgs.gov/docs/stategaz/"

#NaturalEarth
NATURALEARTH_ZIP = "ne_10m_populated_places_simple.zip"
NATURALEARTH_DBF = "ne_10m_populated_places_simple.dbf"
NATURALEARTH_URL = "http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/"


def get_geonames_cities():
    #Check if we already have the Pop_places file
    if not os.path.isfile(GEONAMES_ZIP):
        os.system('wget ' + GEONAMES_URL + GEONAMES_ZIP + ' -O ' + GEONAMES_ZIP)
    if not os.path.isfile(GEONAMES_TXT):
        os.system('unzip ' + GEONAMES_ZIP)
    
    #Tuple of 5 letter cities that start with a state abbreviation and their state abbrebiation
    cities = []
    f = open(GEONAMES_TXT, 'r')
    for line in f:
        line_split = line.split('|')
        if len(line_split[1]) == 5:
            for state in STATES:
                if line_split[1][0:2].upper() == state:
                    cities.append([line_split[1], line_split[3]])

    f.close()
    return(cities)

def get_naturalearth_cities():
#Check if we already have the pop places database
    if not os.path.isfile(NATURALEARTH_ZIP):
        os.system('wget ' + NATURALEARTH_URL + NATURALEARTH_ZIP + ' -O ' + NATURALEARTH_ZIP)
    if not os.path.isfile(NATURALEARTH_DBF):
        os.system('unzip ' + NATURALEARTH_ZIP)
    
    cities = []
    t = dbf.Table(NATURALEARTH_DBF)
    t.open()

    for record in t:
        if record[15] == 'USA' and len(record[4]) == 5:
            print(record)
            print('===================================')

    return ()


def get_pairs(city_array):
    #Array of city pairs
    city_pairs = []
    for left_city in city_array:
        for right_city in city_array:
            if left_city[1] == right_city[0][0:2].upper() and right_city[1] == left_city[0][0:2].upper():
                if [right_city, left_city] not in city_pairs:
                    #This test removes Wypo, Wy <-> Wypo, WY 
                    if len(set(left_city) & set(right_city)) < 2:
                        city_pairs.append([left_city, right_city])
    return (city_pairs)
    
if __name__ == "__main__":
    print('ello mate!')
    get_naturalearth_cities()

    #geonames_cities = get_geonames_cities()
    #geonames_cities_pairs = get_pairs(geonames_cities)

    #for city in geonames_cities_pairs:
    #    print(city[0][0] + ', ' + city[0][1] + ' <-> ' + city[1][0] + ', ' + city[1][1])
    
    #print(str(len(geonames_cities)) + ' city candidates found')
    #print(str(len(geonames_cities_pairs)) + ' city pairs found')

#Natural Earth Method
#import dbf
#table = dbf.Table('/home/cmoser/Desktop/ne_10m_populated_places_simple.dbf')
#table.open()
#for record in table:
#    print(record)
