"""
Write a Guitar class (what should the name of the file be?) that allows you to store one guitar with those ** fields** (attributes):

name (we could split this into make and model, but one name field will do us for now)
year
cost
Define the following methods:

__init__ - with defaults name="", year=0, cost=0

__str__ - which uses {} string formatting to return something like (using the values from above):
Gibson L-5 CES (1922) : $16,035.40
(check here https://www.google.com/search?q=python+__str__+docs&rlz=1C1CHBF_enVN973VN973&sxsrf=AJOqlzVMtmC9kvn3_1ay9gO0DTeab2xaMg%3A1674290898889&ei=0qbLY7LxNZWghwPjtJOoCg&ved=0ahUKEwiyop3So9j8AhUV0GEKHWPaBKUQ4dUDCA8&oq=python+__str__+docs&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQDDIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwA0oECEEYAEoECEYYAFAAWABgkwVoAXAAeACAAQCIAQCSAQCYAQDIAQjAAQE&sclient=gws-wiz-serp)

get_age() - which returns how old the guitar is in years (e.g. the L-5 is 2020 - 1922 = 98) (unless the year has changed since the last time this page was updated :)

is_vintage() - which returns True if the guitar is 50 or more years old, False otherwise
Hint:
- try using get_age() to simplify the implementation of this method!
- use a class attribute to store the age that is considered old of the guitar

Remember that methods should not take in any data that the object already knows (like age, year, etc.).
"""
