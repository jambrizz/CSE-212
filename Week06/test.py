#############
# Problem 5 #
#############

import requests  

def earthquake_daily_summary():
    """
    This function will read JSON (Javascrip Object Notation) data from the 
    United States Geological Service (USGS) consisting of earthquake data.
    The data will include all earthquakes in the current day.
    
    JSON data is organized into a dictionary.  After reading the data using
    the 'requests' library, this function will print out a list of all
    earthquake locations ('place' attribute) and magnitudes ('mag' attribute).
    Additional information about the format of the JSON data can be found 
    at this website:  

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
        
    To install the requests library, run:
       If using virtual environment: pip install requests
       If using Windows: py -m pip install requests
       If using Mac: pip3 install requests
    """ 
    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary
    print(len(data))
    print(data["features"][0]["properties"]["place"])
    # ADD YOUR CODE HERE
    #for key in data:
        #print({each["features"]["properties"]["place"]}+" - Mag "+ {each["features"]["properties"]["mag"]})
        #print({each[2][1][1]}+" - Mag "+ {each[2][1][0]})
        #print(key[0])
    for feature in data["features"]:
        print(feature["properties"]["place"] + " - Mag " + str(feature["properties"]["mag"]))

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 5 TESTS ===========")
earthquake_daily_summary()

# Sample output from the function.  Number of earthquakes, places, and magnitudes will vary.

# 1km NE of Pahala, Hawaii - Mag 2.36
# 58km NW of Kandrian, Papua New Guinea - Mag 4.5
# 16km NNW of Truckee, California - Mag 0.7
# 9km S of Idyllwild, CA - Mag 0.25
# 14km SW of Searles Valley, CA - Mag 0.36
# 4km SW of Volcano, Hawaii - Mag 1.99