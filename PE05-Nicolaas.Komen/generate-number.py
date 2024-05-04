#create empty dictionary to hold key-value pairs
dic1 = {}
#get user input between 1 and n
user_input = int(input())
#create a for loop to iterate through ranges
for i in range(1, user_input + 1):
    a = i*i
    dic1[i] = a
#print and generate dictionary in the form (x, x*x)
print(dic1)