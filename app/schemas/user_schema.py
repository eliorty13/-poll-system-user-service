


from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    address: str


class UserResponse(UserCreate):
    user_id: int
    joining_date: date
    is_registered: bool
