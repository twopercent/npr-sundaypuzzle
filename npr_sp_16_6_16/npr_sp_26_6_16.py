#!/bin/env python3

import os
import dbf

STATES_DICT = {
'AK': 'Alaska',
'AL': 'Alabama',
'AR': 'Arkansas',
'AZ': 'Arizona',
'CO': 'Colorado',
'CT': 'Connecticut',
'DE': 'Delaware',
'FL': 'Florida',
'GA': 'Georgia',
'HI': 'Hawaii',
'IA': 'Iowa',
'ID': 'Idaho',
'IL': 'Illinois',
'IN': 'Indiana',
'KS': 'Kansas',
'KY': 'Kentucky',
'LA': 'Louisiana',
'MA': 'Massachusetts',
'MD': 'Maryland',
'ME': 'Maine',
'MI': 'Michigan',
'MN': 'Minnesota',
'MO': 'Missouri',
'MS': 'Mississippi',
'MT': 'Montana',
'NC': 'North Carolina',
'ND': 'North Dakota',
'NE': 'Nebraska',
'NH': 'New Hampshire',
'NJ': 'New Jersey',
'NM': 'New Mexico',
'NV': 'Nevada',
'NY': 'New York',
'OH': 'Ohio',
'OK': 'Oklahoma',
'OR': 'Oregon',
'PA': 'Pennsylvania',
'RI': 'Rhode Island',
'SC': 'South Carolina',
'SD': 'South Dakota',
'TN': 'Tennessee',
'TX': 'Texas',
'UT': 'Utah',
'VA': 'Virginia',
'VI': 'Virgin Islands',
'VT': 'Vermont',
'WA': 'Washington',
'WI': 'Wisconsin',
'WV': 'West Virginia',
'WY': 'Wyoming'
}

#GeoNames files
GEONAMES_ZIP = "POP_PLACES_20160601.zip"
GEONAMES_TXT = "POP_PLACES_20160601.txt"
GEONAMES_URL = "http://geonames.usgs.gov/docs/stategaz/"

#NaturalEarth files
NATURALEARTH_ZIP = "ne_10m_populated_places_simple.zip"
NATURALEARTH_DBF = "ne_10m_populated_places_simple.dbf"
NATURALEARTH_URL = "http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/"


def get_geonames_cities():
    #Check if we already have the Pop_places text file
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
            if line_split[1][0:2].upper() in STATES_DICT:
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
        if record[15] == 'USA' and len(record[4].rstrip(' ')) == 5:
            #This loop searches the State abbreviation:full name pairs
            #to match 'Alaska' with 'AK' it is innefecient because we are
            #finding the key from the value
            for abbr, full in STATES_DICT.items():
                if full == record[18].rstrip(' '):
                    state_abbr = abbr
            if record[4][0:2].upper() in STATES_DICT:
                cities.append([record[4].rstrip(' '), state_abbr])
    t.close()
    return (cities)


def get_pairs(city_array):
    #Array of city pairs
    city_pairs = []
    for left_city in city_array:
        for right_city in city_array:
            if left_city[1] == right_city[0][0:2].upper() and right_city[1] == left_city[0][0:2].upper():
                #This test will only add cityA <-> cityB if cityB <-> cityA is not already in the list
                if [right_city, left_city] not in city_pairs:
                    #This test removes Wypo, Wy <-> Wypo, WY 
                    if len(set(left_city) & set(right_city)) < 2:
                        city_pairs.append([left_city, right_city])
    return (city_pairs)
    
if __name__ == "__main__":
    naturalearth_cities = get_naturalearth_cities()
    naturalearth_pairs = get_pairs(naturalearth_cities)

    geonames_cities = get_geonames_cities()
    geonames_pairs = get_pairs(geonames_cities)


    print('Geonames ' + str(len(geonames_cities)) + ' city candidates found')
    print('Geonames ' + str(len(geonames_pairs)) + ' city pairs found')

    print('')

    print('Natural Earth ' + str(len(naturalearth_cities)) + ' city candidates found')
    print('Natural Earth ' + str(len(naturalearth_pairs)) + ' city pairs found')
   
    print('')
    
    #Uncomment to see all geonames pairs
    #for city in geonames_pairs:
    #    print(city[0][0] + ', ' + city[0][1] + ' <-> ' + city[1][0] + ', ' + city[1][1])
    
    #print('')

    for city in naturalearth_pairs:
        print(city[0][0] + ', ' + city[0][1] + ' <-> ' + city[1][0] + ', ' + city[1][1])

