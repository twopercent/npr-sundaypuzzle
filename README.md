# npr-sundaypuzzle

Here are some solutions to the June 26 2016 [Sunday Puzzle from NPR](http://www.npr.org/series/4473090/sunday-puzzle).

A couple resources I used:

[GeoNames](http://geonames.usgs.gov/domestic/download_data.htm), 'Populated Places' A text file with city and states.

[Natural Earth](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/), 'Populated Places' A dbf (DBase 3) file with cities, countries, and population.

The GeoNames happend to include a lot more cities and thus a lot more pairs.

The Natural Earth database had fewer U.S. cities and included populations. I intended to sort by population to get to the "well known" answer, but there was only one match in this data set.

The program requires 'wget' and 'unzip' to download and extract both data sources.
