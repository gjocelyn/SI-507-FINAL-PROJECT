from tree import BusinessTree

# assuming you have already retrieved the data and stored it in a variable called 'business_data'
bt = BusinessTree(business_data)

# calling the methods
bt.show_tree()  # displays the business tree
bt.show_price_tree()  # displays the price tree
bt.show_rate_tree() 