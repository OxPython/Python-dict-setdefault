'''
Created on Jul 2, 2014

@author: viejoemer

How I can get a value for default if that value does not exist 
in the dict in Python?

¿Cómo puedo conseguir un valor predeterminado si ese valor no 
existe en el dict en Python?

The method setdefault() is similar to get(), 
but will set dict[key]=default if key is not already in dict.
'''

#Creating a dict with data
d = {'Name': 'Emerson', 'Sex': "Male"}

print (d["Name"], d["Sex"], d.setdefault('Age', None))
print(d)

d.setdefault('Name', None)
print(d)
