



# A program to calculate total stock using two dictionaries 

# Firstly a list of all the items

menu = ["Bacon","Cookies","Cakes","Sausages"]

# Followed by the two dictionaries using the same keys in each dictionary for the same items in the cafe

stock = {'bacon':30, 'cookies':50, 'cakes': 25, 'sausages':35}

price = {'bacon': 2, 'cookies': 3, 'cakes': 4, 'sausages': 1}

# Finally a sum within a for loop to loop through both dictionaries and times them togther and add the sums
# with the 'sum' function.

total = sum(price[i]*stock[i] for i in price)

# Prints out the total stock value.

print("The total value of stock is: ", total)