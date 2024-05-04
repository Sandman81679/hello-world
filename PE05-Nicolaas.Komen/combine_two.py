from collections import Counter

#create two dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 ={'a': 300, 'b': 200, 'd': 400}
#create empty dictionary to store added values for common keys
dic3 = {}

#use counter
dic3 = Counter(d1) + Counter(d2)

#print results into new dictionary(dic3)
print(dic3)