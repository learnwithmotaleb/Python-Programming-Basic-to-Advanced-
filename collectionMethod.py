# # List method
# names = ["Sonia Akter","Lipon","Ripon","Motaleb"]

# print(names)
# print(names.append("Nila Akter"))
# print(names.insert(4, "Emon Khan"))
# print(names.extend(["Emon","Munna"]))
# print(names)
# print(names.remove("Munna"))
# print(names)

# print(names.pop())
# print(names)

# # print(names.clear())
# # print(names)

# print(names.index(2))
# print(names)

# print(names)
# print(names.count("Nila Akter"))
# print(names)

# print(names.sort())
# print(names)

# print(names.sort(reverse=True))
# print(names)

# print(names.reverse())
# print(names)

# print(names.copy())

# numbers_set = {1, 2, 3, 4}

# numbers_set.add(5)  
# print(numbers_set)           # Add element
# numbers_set.remove(2)   
# print(numbers_set)           # Remove element (error if not exist)
# numbers_set.discard(3)  
# print(numbers_set)           # Remove element (no error if not exist)
# numbers_set.pop()  
# print(numbers_set)                # Remove arbitrary element
# numbers_set.clear()   
# print(numbers_set)             # Empty set
# numbers_set.copy()  
# print(numbers_set)               # Shallow copy
# numbers_set.union({4, 5, 6}) 
# print(numbers_set)      # Union of sets
# numbers_set.intersection({2,3,4}) 
# print(numbers_set)    # Common elements
# numbers_set.difference({1,2})  
# print(numbers_set)    # Elements in first set not in second
# numbers_set.symmetric_difference({3,4,5}) # Elements in either set but not both


# student = {"name": "Rahim", "age": 21, "grade": "A"}

# student.get("name")           # Access value safely
# student.keys()                # Returns all keys
# student.values()              # Returns all values
# student.items()               # Returns key-value pairs
# student.update({"age": 22})   # Update or add new key
# student.pop("grade")          # Remove key
# student.popitem()             # Remove last inserted key-value
# student.clear()               # Empty dictionary
# student.copy()     
# 
#            # Returns shallow copy


s = "hello world"

s.upper()   
print(s)    # HELLO WORLD
s.lower()   
print(s)       # hello world
s.title()   
print(s)       # Hello World
s.strip()
print(s)          # Remove leading/trailing spaces
s.replace("o", "0")
print(s)   
s.split()      
print(s)    # Split by spaces
s.join(["a","b","c"])
print(s)   
s.find("l") 
print(s)       # Index of first 'l'
s.startswith("he")
print(s)   
s.endswith("ld")
print(s)   
