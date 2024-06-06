# Create a dictionary and display its list-keys alphabetically.
# Display both the keys and values, sorted by key in alphabetical order.
# At last, display both the keys and values, sorted by value in alphabetical order.
from collections import OrderedDict

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict_1 = {i: myDict[i] for i in myKeys}

sorted_dict_2 = OrderedDict(sorted(myDict.items()))

print(sorted_dict_1)
print(sorted_dict_2)

