import requests
import json
import webbrowser
import tree as tree
import scraping as wiki
import map as map

YELP_URL = 'https://api.yelp.com/v3/businesses/search?'
API_KEY = 'HQ7Go0_7-vDPcwa63d5oaB8XXVHwXD-KezcwgBpagP-E25Aa7nUk6f8htxpapC5Gp_5eGdHGw11v4YKLosV_1_Z1RHNsSV6Y-4r4LNx2_eGJDv_cyrsPGw_bQKdAZHYx'
headers = {'authorization': "Bearer " + API_KEY}
CACHE_f = 'yelp.json'
CACHE_dict = {}

# write and read json
def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

def read_json(filepath, encoding='utf-8'):
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)

# save and open cache
def save_cache(cache_dict):
    write_json(CACHE_f, cache_dict)

def open_cache():
    try:
        cache_dict = read_json(CACHE_f)
    except:
        cache_dict = {}
    return cache_dict

# check if the data is already stored in cache
def check_data(url, params):
    param_list=[]
    for i in params.keys():
        param_list.append(f"{i}_{params[i]}")
    param_list.sort()
    uniq_idx = url + '+'.join(param_list)
    check_idx=uniq_idx
    if check_idx in CACHE_dict.keys():
        print("Retrieved data from cache")
        return CACHE_dict[check_idx]
    else:
        print("Fetched data from API")
        CACHE_dict[check_idx]=requests.get(url, params=params, headers=headers).json()
        save_cache(CACHE_dict)
        return CACHE_dict[check_idx]

def openweb(url):
    webbrowser.open(url, new = 0)

def main():
    CACHE_dict = open_cache()
    print('\nHi! Welcome to the fun resturant search engine!')
    while True:
        print("\nEnter 1 to see the information of large cities or 2 directly search the city")
        input_1 = input("Enter the number or exit: ")
        if input_1.lower() == 'exit':
            exit()
        elif int(input_1) == 1:
                    number_input = int(input("Please choose the number of cities you want to see:"))
                    city_list = wiki.city(number_input)
                    for city in city_list:
                        print(f"[{city['rank']}] name: {city['name']}, state: {city['state']}, population: {city['population']}, area: {city['area']}")
                    number_input_2 = int(input("Please choose the city you want to see (input number):"))
                    if (1 <= number_input_2 and number_input_2 <= number_input):
                        location = city_list[number_input_2-1]["name"]
                        url = YELP_URL + location
                        param = {
                            'location': location,
                            'term': "food",
                            'limit': 50
                        }
                        data = check_data(url, param)
                        tree_information = tree.tree(data)
                        while True:
                            choice_1 = input("Do you want to see the map of this city and the locations of resturants(y or n)?")
                            if choice_1.lower() == 'yes' or choice_1.lower() == 'y':
                                fig = map.city_map(tree_information)
                                break
                            elif choice_1.lower() == 'no' or choice_1.lower() == 'n':
                                break
                            else:
                                print("Please try again")
                        while True:
                            choice_2 = input("Do you want search the resturants based on PRICE and  RATE?(y or n)")
                            if choice_2.lower() == 'yes' or choice_2.lower() == 'y':
                                rest_chosen = []
                                tree_final = tree.rate_tree(tree.price_tree(tree_information))
                                choice_3 = input("Which price level do you wnat to see? ($, $$, $$$, $$$$ or No price)")
                                if choice_3 == '$':
                                    choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                                    if choice_4 == 'above 4' or '1' or '1.above 4':
                                        for i in tree_final['$']['above 4']:
                                           rest_chosen.append(i)
                                    elif choice_4 == '2.above 3' or '2' or 'above 3':
                                        for i in tree_final['$']['above 3']:
                                            rest_chosen.append(i)
                                    elif choice_4 == 'above 2' or '3' or '3.above 2':
                                        for i in tree_final['$']['above 2']:
                                            rest_chosen.append(i)
                                    else:
                                        for i in tree_final['$']['under 2']:
                                            rest_chosen.append(i)
                                elif choice_3 == '$$':
                                    choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                                    if choice_4 == 'above 4' or '1' or '1.above 4':
                                        for i in tree_final['$$']['above 4']:
                                            rest_chosen.append(i)
                                    elif choice_4 == '2.above 3' or '2' or 'above 3':
                                        for i in tree_final['$$']['above 3']:
                                            rest_chosen.append(i)
                                    elif choice_4 == 'above 2' or '3' or '3.above 2':
                                        for i in tree_final['$$']['above 2']:
                                            rest_chosen.append(i)
                                    else:
                                        for i in tree_final['$$']['below 2']:
                                            rest_chosen.append(i)
                                elif choice_3 == '$$$':
                                    choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                                    if choice_4 == 'above 4' or '1' or '1.above 4':
                                        for i in tree_final['$$$']['above 4']:
                                           rest_chosen.append(i)
                                    elif choice_4 == '2.above 3' or '2' or 'above 3':
                                        for i in tree_final['$$$']['above 3']:
                                          rest_chosen.append(i)
                                    elif choice_4 == 'above 2' or '3' or '3.above 2':
                                        for i in tree_final['$$$']['above 2']:
                                           rest_chosen.append(i)
                                    else:
                                        for i in tree_final['$$$']['under 2']:
                                            rest_chosen.append(i)
                                elif choice_3 == '$$$$':
                                    choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                                    if choice_4 == 'above 4' or '1' or '1.above 4':
                                        for i in tree_final['$$$$']['above 4']:
                                            rest_chosen.append(i)
                                    elif choice_4 == '2.above 3' or '2' or 'above 3':
                                        for i in tree_final['$$$$']['above 3']:
                                            rest_chosen.append(i)
                                    elif choice_4 == 'above 2' or '3' or '3.above 2':
                                        for i in tree_final['$$$$']['above 2']:
                                            rest_chosen.append(i)
                                    else:
                                        for i in tree_final['$$$$']['under 2']:
                                            rest_chosen.append(i)
                                elif choice_3.lower() == 'no price':
                                    choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                                    if choice_4 == 'above 4' or '1' or '1.above 4':
                                        for i in tree_final['no price']['above 4']:
                                            rest_chosen.append(i)
                                    elif choice_4 == '2.above 3' or '2' or 'above 3':
                                        for i in tree_final['no price']['above 3']:
                                            rest_chosen.append(i)
                                    elif choice_4 == 'above 2' or '3' or '3.above 2':
                                        for i in tree_final['no price']['above 2']:
                                            rest_chosen.append(i)
                                    else:
                                        for i in tree_final['no price']['under 2']:
                                            rest_chosen.append(i)
                                else:
                                    print('invalid, try again')
                                for i in range(len(rest_chosen)):
                                    print(f"{i+1}. {rest_chosen[i]['name']}: {rest_chosen[i]['attributes']['category']} - rate:{rest_chosen[i]['attributes']['rating']} - phone:{rest_chosen[i]['attributes']['phone']}")
                                if(len(rest_chosen) > 0):
                                    choice_5 = int(input('Enter the serial number of resturant to go to the yelp website')-1)
                                    openweb(rest_chosen[choice_5]['attributes']['url'])
                                else:
                                    print('There is no resualt')
                            elif choice_2.lower() == 'no' or choice_2.lower() == 'n':
                                break
                            else:
                                print("Please try again")
                    else:
                        print("Invalid, please try again")
        elif int(input_1) == 2:
            location = input("Enter the name of the city:") # NYU
            url = YELP_URL + location
            param = {
                        'location': location,
                        'term': "food",
                        'limit': 50
                    }
            data = check_data(url, param)
            tree_information = tree.tree(data)
            while True:
                choice_1 = input("Do you want to see the locations of resturants on the map(y or n)?")
                if choice_1.lower() == 'yes' or choice_1.lower() == 'y':
                    fig = map.city_map(tree_information)
                    break
                elif choice_1.lower() == 'no' or choice_1.lower() == 'n':
                    break
                else:
                    print("Please enter y or n")

            while True:
                choice_2 = input("2 Do you want search the resturants based PRICE and RATE?(y or n)")
                if choice_2.lower() == 'yes' or choice_2.lower() == 'y':
                    rest_chosen = []
                    tree_final = tree.rate_tree(tree.price_tree(tree_information))
                    choice_3 = input("Which price level do you wnat to see? ($, $$, $$$, $$$$ or No price)")
                    if choice_3 == '$':
                        choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                        if choice_4 == 'above 4' or '1' or '1.above 4':
                            for i in tree_final['$']['above 4']:
                                rest_chosen.append(i)
                        elif choice_4 == '2.above 3' or '2' or 'above 3':
                            for i in tree_final['$']['above 3']:
                                rest_chosen.append(i)
                        elif choice_4 == 'above 2' or '3' or '3.above 2':
                            for i in tree_final['$']['above 2']:
                                rest_chosen.append(i)
                        else:
                            for i in tree_final['$']['under 2']:
                                rest_chosen.append(i)
                    elif choice_3 == '$$':
                        choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                        if choice_4 == 'above 4' or '1' or '1.above 4':
                            for i in tree_final['$$']['above 4']:
                                rest_chosen.append(i)
                        elif choice_4 == '2.above 3' or '2' or 'above 3':
                            for i in tree_final['$$']['above 3']:
                                rest_chosen.append(i)
                        elif choice_4 == 'above 2' or '3' or '3.above 2':
                            for i in tree_final['$$']['above 2']:
                                rest_chosen.append(i)
                        else:
                            for i in tree_final['$$']['below 2']:
                                rest_chosen.append(i)
                    elif choice_3 == '$$$':
                        choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                        if choice_4 == 'above 4' or '1' or '1.above 4':
                            for i in tree_final['$$$']['above 4']:
                                rest_chosen.append(i)
                        elif choice_4 == '2.above 3' or '2' or 'above 3':
                            for i in tree_final['$$$']['above 3']:
                                rest_chosen.append(i)
                        elif choice_4 == 'above 2' or '3' or '3.above 2':
                            for i in tree_final['$$$']['above 2']:
                                rest_chosen.append(i)
                        else:
                            for i in tree_final['$$$']['under 2']:
                                rest_chosen.append(i)
                    elif choice_3 == '$$$$':
                        choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                        if choice_4 == 'above 4' or '1' or '1.above 4':
                            for i in tree_final['$$$$']['above 4']:
                                rest_chosen.append(i)
                        elif choice_4 == '2.above 3' or '2' or 'above 3':
                            for i in tree_final['$$$$']['above 3']:
                                rest_chosen.append(i)
                        elif choice_4 == 'above 2' or '3' or '3.above 2':
                            for i in tree_final['$$$$']['above 2']:
                                rest_chosen.append(i)
                        else:
                            for i in tree_final['$$$$']['under 2']:
                                rest_chosen.append(i)
                    elif choice_3.lower() == 'no price':
                        choice_4 = input("Enter rate level( 1.above 4, 2.above 3, 3.above 2, 4.under 2):")
                        if choice_4 == 'above 4' or '1' or '1.above 4':
                            for i in tree_final['no price']['above 4']:
                                rest_chosen.append(i)
                        elif choice_4 == '2.above 3' or '2' or 'above 3':
                            for i in tree_final['no price']['above 3']:
                                rest_chosen.append(i)
                        elif choice_4 == 'above 2' or '3' or '3.above 2':
                            for i in tree_final['no price']['above 2']:
                                rest_chosen.append(i)
                        else:
                            for i in tree_final['no price']['under 2']:
                                rest_chosen.append(i)
                    else:
                        print('invalid, try again')
                    for i in range(len(rest_chosen)):
                        print(f"{i+1}. {rest_chosen[i]['name']} - {rest_chosen[i]['attributes']['category']} - rate:{rest_chosen[i]['attributes']['rating']} - price:{rest_chosen[i]['attributes']['price']}")
                    if(len(rest_chosen) > 0):
                        choice_5 = int(input('Enter the serial number of resturant to go to the yelp website')-1)
                        openweb(rest_chosen[choice_5]['attributes']['url'])
                    else:
                        print('There is no resualt')
                elif choice_2.lower() == 'no' or choice_2.lower() == 'n':
                    break
                else:
                    print("Please try again")
        else:
            print("Please input a number or exit")

if __name__ == '__main__':
    main()