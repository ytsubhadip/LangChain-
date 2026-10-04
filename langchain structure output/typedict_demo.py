from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

new_person : person={"name": "subhadip bar", "age": 42}
print(new_person)