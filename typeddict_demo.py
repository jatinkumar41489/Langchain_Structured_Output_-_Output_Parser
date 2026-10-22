"""
TypedDict allows you to define a dictionary with specific keys and their corresponding value types. 
It will not give error even if the value types are not matching with the defined types. 
Like: In class Person, age : int
    but in new1_person, age is given as str. It will not give error. 
"""

from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

# Adding Jatin as a new Person instance
new1_person: Person = {
    "name": "Amy",
    "age": "25",  # You can change the age and email as needed
    "email": "amy@example.com"
}

print(new_person)
print(new1_person)


