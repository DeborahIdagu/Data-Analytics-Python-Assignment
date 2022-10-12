#!/usr/bin/env python
# coding: utf-8

# # 1) Print all elements of a list using for loop

# In[1]:


myFamily = ['Mum', 'Dad', 'Daughter', 'Son', 'Uncle', 'Anty', 'Cousin']
for relatives in myFamily:
    print(relatives)


# # 2) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# In[4]:


salary = int(input('Enter your salary : '))

year = int(input('Enter your years of service : '))

if year>5:

   print('Your Net bonus is',0.05*salary)


# # 3) Take input of age of 3 people by user and determine oldest and youngest among them.
# 

# In[8]:


person1 = int(input('Enter age of person 1 : '))
person2 = int(input('Enter age of person 2 : '))
person3 = int(input('Enter age of person 3 : '))

if person1 > person2 and person1 > person3:
    print('Person 1 is oldest')
elif person2 > person1 and person2 > person3:
    print('Person 2 is oldest')
elif person3 > person1 and person3 > person2:
    print('Person 3 is oldest')

if person1 < person2 and person1 < person3:
    print('Person 1 is youngest')
elif person2 < person1 and person2 < person3:
    print('Person 2 is youngest')
elif person3 < person1 and person3 < person2:
    print('Person 3 is youngest')


# # 4) A school has following rules for grading system
# a. Below 25 - F
# 
# b. 25 to 45 - E
# 
# c. 45 to 50 - D
# 
# d. 50 to 60 - C
# 
# e. 60 to 80 - B
# 
# f. Above 80 - A
# 

# # 5) Ask user to enter marks and print the corresponding grade.
# 

# In[10]:


score = int(input('Enter your score: '))
if score < 25:  

   print('F')

elif score >= 25 and score < 45:  

   print('E')

elif score >= 45 and score < 50:  

   print('D')

elif score >= 50 and score < 60:  

   print('C')

elif score >= 60 and score < 80:  

   print('B')

else:  

   print('A')


# # 6) Write a Python script to merge two Python dictionaries

# In[11]:


dict1 = {'Father':60, 'Mother':55, 'Daughter':29, 'Son':30}

dict2 = {'Uncle':44, 'Anty':41, 'Cousin': 21}

dictionary = dict1.copy()

dictionary.update(dict2)

print(dictionary)


# # 7) Write a python program to get the largest number from a list 
# 

# In[12]:


grades = [54,10,12,90,25,43,70]

print('Largest grade is:', max(grades))


# # 8) Write a python program to remove a key from a dictionary

# In[13]:


family = {'Father': 60, 'Mother': 55, 'Daughter': 29, 'Son': 30, 'Uncle': 44, 'Anty': 41, 'Cousin': 21}
print('Dictionary with complete keys: ', family)

del family ['Uncle']
print('Dictionary after removing one key: ', family)


# In[ ]:




