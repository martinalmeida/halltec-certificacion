from pydantic import BaseModel, Field

class ExampleDTO(BaseModel):
    name: str = Field(..., example="John Doe", min_length=3, max_length=50)
    age: int = Field(..., example=30, ge=0, le=120)
    email: str = Field(..., example="johndoe@example.com")