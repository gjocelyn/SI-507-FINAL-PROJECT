## analyze and process data by creating a tree

def tree(info):
    tree = []
    _dict = {}

    for item in info['businesses']:
        _dict = {'name': item["name"], 'attributes': {}}
        _dict['attributes']['url'] = item["url"]
        _dict['attributes']['category'] = item["categories"][0]["alias"]
        _dict['attributes']['rating'] = item["rating"]
        _dict['attributes']['latitude'] = item["coordinates"]["latitude"]
        _dict['attributes']['longitude'] = item["coordinates"]["longitude"]
        try:
            _dict['attributes']['price'] = item["price"]
        except:
            _dict['attributes']['price'] = None
        _dict['attributes']['location'] = item["location"]
        _dict['attributes']['phone'] = item["display_phone"]
        tree.append(_dict)
    return tree

def price_tree(tr):
    price_tree = {'$': [], '$$': [], '$$$': [], '$$$$': [], 'No price': []}
    for item in tr:
        if item['attributes']['price'] == '$$$$':
            price_tree['$$$$'].append(item)
        elif item['attributes']['price'] == '$$$':
            price_tree['$$$'].append(item)
        elif item['attributes']['price'] == '$$':
            price_tree['$$'].append(item)
        elif item['attributes']['price'] == '$':
            price_tree['$'].append(item)
        else:
            price_tree['No price'].append(item)
    return price_tree

def rate_tree (price_tree):
    final_tree = {}
    for key in price_tree.keys():
        final_tree[key] = {'above 4': [], 'above 3': [], 'above 2': [], 'under 2':[]}
        for item in price_tree[key]:
            if  4.0 <= item['attributes']['rating'] and item['attributes']['rating'] <= 5.0:
                final_tree[key]['above 4'].append(item)
            elif 3.0 <= item['attributes']['rating'] and item['attributes']['rating'] < 4.0:
                final_tree[key]['above 3'].append(item)
            elif 2.0 <= item['attributes']['rating'] and item['attributes']['rating'] < 3.0:
                final_tree[key]['above 2'].append(item)
            else:
                final_tree[key]['under 2'].append(item)
    return final_tree

