'''
1
list1 = [1, 3, 5, 1, 7, 9, 2, 2, 8, 5, 10, 5]
list2 = [1, 2, 5]
Remove all items from list1 that appear in list2
Print list1 at the end
'''
list1: list[int] = [1, 3, 5, 1, 7, 9, 2, 2, 8, 5, 10, 5]
list2: list[int] = [1, 2, 5]
for item in list2:
    while item in list1:
         list1.remove(item)
print(f"list1 = {list1}")

'''
2
list1 = [1, 2, 9, 88, 0]
list2 = [3, 4, -3]
list3 = [5, 6, 55]
Create list4 that contains all values from list1, list2, and list3
Use loops only (no +)
'''
list1 = [1, 2, 9, 88, 0]
list2 = [3, 4, -3]
list3 = [5, 6, 55]
list4 = []
for item in list1:
    list4.append(item)
for item in list2:
    list4.append(item)
for item in list3:
    list4.append(item)
print(f"list4 {list4}")

'''
3
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]
Create a new list that contains items from list1
that do NOT appear in list2
'''
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4]
list3 = []
for item in list1:
    if not item in list2:
        list3.append(item)
print(f"list3 {list3}")

'''
4
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
Create a list with items that appear in both lists
No duplicates in the result
'''
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
list3 = []
for item in list1:
    if item in list2:
        list3.append(item)
print(f"list3 {list3}")

'''
5
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4]
list3 = [5, 6]
Remove from list1 all items that appear in either list2 or list3
Print list1
'''
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [2, 4]
list3 = [5, 6]
for item in list2:
     while item in list1:
        list1.remove(item)
for item in list3:
     while item in list1:
        list1.remove(item)
print(f"list1 {list1}")

'''
6
list1 = [1, 4, 6] -- sorted
list2 = [2, 5, 7] -- sorted
Create list3 that contains all numbers from both lists but keep them sorted
'''
# [1, 2, 4, 5, 6, 7]
list1 = [1, 4, 6]
list2 = [2, 5, 7]
list3 = []
for i in list1:
     list3.append(i)
for i in list2 :
     list3.append(i)
print(f"not sorted list = {list3}")  
list3.sort()     
print(f" sorted list = {list3}") 

'''
7
list1 = [1, 2, 3, 4, 5, 2, 2]
list2 = [2, 4]
Count how many items in list1 appear in list2
Print the count
'''
list1 = [1, 2, 3, 4, 5, 2, 2]
list2 = [2, 4]
count = 0
for item in list1:
    if item in list2:
        count += 1
print(f"count: {count}")

'''
8
Remove by blacklist
Given:
names = ["danny", "moshe", "suzi", "sharon", "avi"]
blacklist = ["moshe", "avi"]
Remove all blacklisted names from names
'''
names = ["danny", "moshe", "suzi", "sharon", "avi"]
blacklist = ["moshe", "avi"]
for item in blacklist:
    while item in names:
        names.remove(item)
print(f"names: {names}")

'''
9
Given:
list1 = [1, 2, 3, 4, 5, 6, 7]
Create:
list_even → all even numbers
list_odd → all odd numbers
'''
list1 = [1, 2, 3, 4, 5, 6, 7]
list_even = []
list_odd = []
for num in list1:
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)
print(f"lise_even= {list_even}")
print(f"list_odd= {list_odd}")

'''
10
Given:
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
Create list2
Copy into list2 only strings that are ALL uppercase
'''
list1 = ["HELLO", "World", "PYTHON", "code", "TEST"]
list2 = []
for item in list1:
    if item.isupper():
        list2.append(item)
print(f"list2 = {list2}")

'''
11
Copy strings that start with capital letter
Given:
list1 = ["Hello", "world", "Python", "java", "Code"]
Copy to list2 only words that start with uppercase
'''
list1 = ["Hello", "world", "Python", "java", "Code"]
list2 = []
for item in list1:
    if item[0].isupper():
        list2.append(item)
print(f"list2 = {list2}")

'''
12 – Split sentence list into words
Given:
sentences = [
    "Hello world",
    "Python is fun",
    "I love coding"
]
Create words list that contains all words
Use split() and loops
'''
sentences = [
    "Hello world",
    "Python is fun",
    "I love coding"
]
sentences2 = " ".join(sentences)
print(f"sentences2= {sentences2.split()}")

'''
13
trip spaces and copy non-empty strings
Given:
list1 = ["  hello  ", "   ", "python", "  code ", ""]
Create list2 that contains:
stripped strings
ignore empty strings after strip
hint: use isspace
'''
list1 = ["  hello  ", "   ", "python", "  code ", ""]
list2 = []
for item in list1:
    if not item.isspace():
       item = item.strip()
       if item.isalpha():
          list2.append(item)
print(f"list2 = {list2}")

'''
14 – Replace letters in all strings
Given:
list1 = ["hello", "world", "python"]
Create list2 where:
all o letters are replaced with 0
'''
list1 = ["hello", "world", "python"]
list2 =[]
for item in list1:
     item = item.replace("o", "0")
     list2.append(item)
print(f"list2 = {list2}")

'''
15 – Count strings that end with specific word
Given:
list1 = ["good morning", "morning sun", "happy morning", "good night"]
Count how many strings end with "morning"
'''
list1 = ["good morning", "morning sun", "happy morning", "good night"]
_count = 0
for item in list1:
    if item.endswith('morning'):
        _count += 1
print(f"list1 endswith morning {_count} times")

'''
16– Separate numeric strings and text strings
Given:
list1 = ["123", "hello", "42", "F114", "python", "007", "A14"]
Create:
numbers → numeric strings only
texts → non-numeric strings
mixed -> both
'''
list1 = ["123", "hello", "42", "F114", "python", "007", "A14"]
numbers = []
texts = []
mixed = []
for item in list1:
    if item.isalpha():
        texts.append(item)
    elif item.isdigit():
        numbers.append(item)
    else:
        mixed.append(item)
print(f"numbers = {numbers}")
print(f"texts = {texts}")
print(f"mixed = {mixed}")

'''
17 – Reverse only uppercase words
Given:
list1 = ["HELLO", "World", "PYTHON", "code"]
Create list2:
if word is uppercase → reverse it
else → copy as is
'''
list1 = ["HELLO", "World", "PYTHON", "code"]
list2 = []
for item in list1:
    if item.isupper():
        item = item[::-1]
        list2.append(item)
    else:
        list2.append(item)
print(f"list2 = {list2}")
