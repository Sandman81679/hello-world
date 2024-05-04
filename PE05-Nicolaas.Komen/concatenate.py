#creating 3 dictionaries
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
#create a new empty dictionary to store the key-value pairs from dic1, dic2, dic3

dic4 = {}
#create a for-loop to iterate through all 3 dictionaries to get unique key-value pairs
for dic in (dic1, dic2, dic3):
    #update dic4 which adds all 3 original dictionaries into dic4
    dic4.update(dic)
#print combined dictionaries into new dictionary (dic4)
print(dic4)