# import random

# string_one = input("Type in your word: ")
# print ("Original String: ", string_one)
# char_list = list(string_one) # convert string inti list
# random.shuffle(char_list) #shuffle the list
# string_one = ''.join(char_list)
# print ("shuffled String is: ", string_one)

import random

# chuyen tu thanh list
string_one = list("pynative")
# dao vitri tu
random.shuffle(string_one)

# in cac tu dc dao
for i in string_one:
    print(i)

# for i in range(len(string_one)):
#     print(string_one[i])