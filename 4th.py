print("printing the dictionary item:")
dict1 = {"name ": "suma", "regno": 321, "course": "BCA", "age": 19}
print(dict1)
print("accessing the items: ")
print(dict1["age"])
print("using get(): ")
x = dict1.get("regno")
print(x)
print("changing the values in the dictionary: ")
dict2 = {"regno": 286}
dict1.update(dict2)
print(dict1)
print("length of dictionary is: ", len(dict1))
