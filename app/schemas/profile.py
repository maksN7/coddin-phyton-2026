from pydantic import BaseModel, ConfigDict, Field


class ProfileBase(BaseModel):
    user_id: int
    full_name: str = Field(min_length=2, max_length=160)
    phone: str | None = Field(default=None, max_length=40)
    address: str | None = Field(default=None, max_length=255)


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=2, max_length=160)
    phone: str | None = Field(default=None, max_length=40)
    address: str | None = Field(default=None, max_length=255)


class ProfileRead(ProfileBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
