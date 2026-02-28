#This "program" is not intended to be run
#It is just for copy pasting code snippets
from sys import exit
#exit()



#Increase recursion limit (1000 by defualt)
from sys import setrecursionlimit
setrecursionlimit(1500)


#Alphabet
alpha = "abcdefghijklmnopqrstuvwxyz"
#or
import string #Also contains other useful strings
alpha = string.ascii_lowercase


#Convert from unicode characters to integers and vice versa
unicode_int = ord("A") # 65
unicode_char = chr(65) # 'A'


#Switch rows + columns (transpose 2d list)
#Rows and columns must be of same len, otherwise lowest len is used
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
list2 = [list(elem) for elem in list(zip(*list1))]


#Use itertools.zip_longest to take longest len instead of shortest.
from itertools import zip_longest
list3 = [[1, 2], [4, 5, 6], [7, 8], [10, 11, 12]]
list4 = [list(elem) for elem in list(zip_longest(*list3, fillvalue=-1))]


#Convert lists to dicts using zip or comprehension
keys = ["a", "b", "c"]
values = ["one", "two", "three"]
dict1 = dict(zip(keys, values))
dict2 = {keys[i] : values[i] for i in range(len(keys))}


#Custom sorting (ex. sort numeric strings by magnitude)
list1 = ["1", "34", "-100", "900", "5", "-343"]
sorted(list1, key=lambda x: abs(int(x)))


#Converts lists and strings to a dictionary-like counter
from collections import Counter
first = "abcd"
second = "acdb"
#For instance, checking for anagrams (all the same elements + counts)
is_anagram = Counter(first) == Counter(second)


#Date conversion from string to datetime object
# %Y is year, %m is month, %d is day
from datetime import datetime
time_str = "2024-8-20"
time_t = datetime.strptime(time_str, "%Y-%m-%d")

time_str2 = "2025-8-20"
time_t2 = datetime.strptime(time_str2, "%Y-%m-%d")
e = time_t2.strftime(f"%A, the %drd of %B")
#print(e)
time_str3 = "08/20 in 2025"
time_t3 = datetime.strptime(time_str3, "%m/%d in %Y")
#print(time_t3)