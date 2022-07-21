from typing import List, Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int
    name: Union[str, None] = None
    sex: Union[str, None] = None
    color: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    
    class Config:
        orm_mode = True

