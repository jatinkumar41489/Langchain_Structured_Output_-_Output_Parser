"""
1) Pydantic provides data validation and type checking, ensuring that the output conforms to the expected types and structure.
2) For Data validation, you can use Pydantic models instead of TypedDict.
3) Pydantic also allows you to apply Contraints.You can also set a default value in Field.
ex: Suppose default=5 and you dont pass the value in cgpa it will show by default cgpa=5.0
4) description :-> it allows you to describe that key or value so that LLM get a easy understanding of that key or value. 
5) Pydantic Objects can be converted into Dictionary or Json.  
"""

from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name:str
    age:Optional[int] = None
    email:EmailStr
    cgpa:float= Field(gt=0, lt=10,default=5,description= 'A decimal value that represent the value of cgpa') 

    """ Apply Constraint with the help of Field Function in Pydantic.You can also set a default value in Field. Suppose default=5 and you dont pass the value in cgpa it will show by default cgpa=5.0"""
    
new_student = {
    "name":"John Doe", 
    "age":"20",
    "email":"abc@gmail.com",
    "cgpa":9
    }
 # if you change the name to int, it will give error. It will not allow to create the instance of Student class with wrong data type.But at the same time , if you give the age as str, it will not give error. It will convert the str to int automatically. But if you give the name as int, it will give error. 


student = Student(**new_student)

print(student)

student_dict = dict(student) # Convert Pydantic ---> Dictionary

print(student_dict['age'])

student_json = student.model_dump_json() # Convert Pydantic ---> JSON


