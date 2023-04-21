## Astand alone python file that reads the json of your graphs or trees.

import tree
import find

show_tree = {
    '$': {
        'above 4': [],
        'above 3': [],
        'above 2': [],
        'under 2': [],

        },
    '$$': {
        'above 4': [],
        'above 3': [],
        'above 2': [],
        'under 2': [],
        },
    '$$$': {
        'above 4': [],
        'above 3': [],
        'above 2': [],
        'under 2': [],
        },
    '$$$$': {
        'above 4': [],
        'above 3': [],
        'above 2': [],
        'under 2': [],
        }
}

if __name__ == '__main__':
            location = input("Enter the name of the city:")
            url = find.YELP_URL + location
            param = {
                        'location': location,
                        'term': "food",
                        'limit': 50
                    }
            data = find.check_data(url, param)
            tree_information = tree.tree(data)
            rest_chosen = []
            tree_final = tree.rate_tree(tree.price_tree(tree_information))
            print(tree_final)