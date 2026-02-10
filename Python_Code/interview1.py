val1 = [1,2,3]
val2 = ['a','b','c']

#zip function creates a series of tuples, and the comprehension unpacks them into keys and values: 

res_dict = dict(zip(val1,val2))

# comprehension + Zip
res_dict = {i: j for i, j in zip(val1, val2)}

res_dict = {val1[i]: val2[i] for i in range(len(val1))}

print(res_dict)