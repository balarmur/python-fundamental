# A simple database

# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone
# number and address, respectively.
people = {

    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

# Descriptive labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}


name = input('Name: ')

print(people.get(name,'Name Not Found'))

# Are we looking for a phone number or an address?
#request = input('Phone number (p) or address (a)? ')

# Use the correct key:
#if request == 'p': key = 'phone'
#if request == 'a': key = 'addr'

# Only try to print information if the name is a valid key in
# our dictionary:
#if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))


# Use get to provide default values:
#print(people.keys())
#person = people.get(name, {})
#label = labels.get(key, key)
#result = person.get(key, 'not available')
#print("{}'s {} is {}.".format(name, label, result))


d={1:"One",2:"Two",3:"Three"}
print(d.get(1,"No Number"))
print(d.get(0,"No Number"))


# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 21:19:08 2018

@author: bala0
"""

myList01=[1,2,3,4,5]
myDict01=dict.fromkeys(myList01)
print(myList01)
print(myDict01)