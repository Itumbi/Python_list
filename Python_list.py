#Create empty list as my first assignment
my_list=[]
#Add numbers to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#print out the out put to see if empty list is filled
print(my_list)
#insert the value 15 at second position in the list
my_list.insert(1,15)
print(my_list)
#Extend my_list with another list
numbers=(50,60,70)
my_list.extend(numbers)
print(my_list)
#removing the last element
last_index=-1
my_list.remove(my_list[last_index])  #You can a;lso use only -1 instead of last index
print(my_list)
#Sort my_list in ascending order
my_list.sort()
print(my_list)
#print index of value 30 in my_list
index_of_30 = my_list.index(30)
print('Index value of 30:',index_of_30)