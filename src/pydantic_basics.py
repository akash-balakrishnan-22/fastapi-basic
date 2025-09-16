from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr

valid_data = Person(name="akash", age="11", email="akash@gmail.com")
print(valid_data)