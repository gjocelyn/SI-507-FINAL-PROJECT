# SI-507-FINAL-PROJECT


## INTRODUCTION
This project is a restaurant search program that help people find the desired restaurant. In order to acheve this goal, it need to get access of the restaurant data from the website, then organizes that data into a tree. By asking users questions (about price, rate location, etc.) until it provides a set of recommendations that meet the user options.


## PYTHON PACKAGE
- BeautifulSoup in bs4 
- time
- webbrowser
- plotly

## DATA SOURCE
- Yelp Fusion API: 'https://api.yelp.com/v3/businesses/search?'
Using API to get access to this website, it gives restaurants data including the name, location, rate, categories, price, phone numberand etc.,then save into json file
- Mapbox TOKEN: 'https://www.mapbox.com/'
Using API to get access to this website, using the latitude and longitude information from wikipedia and yelp to locate restaurants in different cities.
- Wikipedia: 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'
From this website,data such as the state, population and areas about the city has been scrapped.


## DATA STRUCTURE
In order to populate the tree for this project with the latest information about restaurants, you might choose to store this data in a cache or retrieve it from an online source, such as a web API, and then dynamically reorganize the data into the appropriate tree structure each time the program is run, allowing users to access the most up-to-date information about restaurants and their attributes. The leaf node will be the information of restaurants, the attribute node will be the restaurants attribution. Every time I run the python code, I will reorganize the data (stored in cache or requested from the web) into a tree.


## INTERACTION AND PRESENTATION

#### STEP 1: Install all the required python packages:
'''
pip install bs4 # BeautifulSoup in bs4 
pip install time # time
pip install webbrowser # webbrowser
pip install plotly #plotly
'''

#### STEP 2: Start running find.py:
'''
python3 find.py
'''

#### STEP 3: Choose the city:
- 'First Question':
    'Enter 1 to see the information of large cities or 2 directly search the city:'
    - If choose 1
        - 'Second Question': 
        'Please choose the number of cities you want to see:'
        - `Third Question`: 
        '''
        Please choose the city you want to see (input number):
        '''
    - If choose 2
        - `Fourth Question`: 
        '''
        Enter the name of the city:
        '''
 From now, we got the city that you choose to find the restaurant!
 
 #### STEP 4: locate of restaurants on map
 - `fifth Question`: 
    '''
    '''Do you want to see the map of this city and the locations of resturants(y or n)? (input Yes, YES, y, Y, YEs, etc. all is okay)
                - If yes, a map figure will pop up, with the marker which contains the information of restaurants distributed in in the map.
                - If no, move to the Fifth Question.
            - `Fifth Question`: Do you want search the resturants through Price and Rate?(y or n)
                - If yes, move to the next question:
                    - `Sixth Question`: Which price level do you wnat to see? ($, $$, $$$, $$$$ or No price) (Input one of string)
                    - `Seventh Question`: Which rate level do you want to see? ('above 4', 'above 3', 'above 2', 'below 2') (Input one of string)
                    - Generate a list contains the information of restaurants under the limitation of sixth and seventh questions.
                        - `Eighth Question`:please input a num of resturant which you want to see the website:(Input the restaurant number, the program will show corresponding website) (If yhe list of restaurant is empty, this question will not pop up)
                - If No, move to the First Question.

    - If exit: exit the program.
    
 ## Demo
https://drive.google.com/file/d/1m6aLTi6g2vnzpMVkZ-75PHfAmXbXKEUn/view
