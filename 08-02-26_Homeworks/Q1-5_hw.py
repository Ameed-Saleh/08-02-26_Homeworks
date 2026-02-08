#1
print(f"question 1")
list1 = [1, 2, 3, 4, 5, 6, 7]
list_even = []
list_odd = []
for num in list1:
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)
print(f"list_odd= {list_odd}")
print(f"lise_even= {list_even}")


#2
print("")
print(f"question 2")
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
list2 = []
for item in list1:
    if item.isupper():
        list2.append(item)
print(f"list2= {list2}")


#3
print("")
print(f"question 3")
list1 = ["Hello", "world", "Python", "java", "Code"]
list2 = []
for item in list1:
    if item[0].isupper():
        list2.append(item)
print(f"list2= {list2}")


#4
print("")
print(f"question 4")
sentences= [
    "Hello world",
    "Python is fun",
    "I love coding"
]
sentences2 = " ".join(sentences)
print(f"sentences2= {sentences2.split()}")


#5
print("")
print(f"question 5")
list1 = ["HELLO", "World", "PYTHON", "code"]
list2 = []
for item in list1:
    if item.isupper():
        item = item[::-1]
        list2.append(item)
    else:
        list2.append(item)
print(list2)

