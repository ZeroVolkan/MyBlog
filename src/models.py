from pydantic import BaseModel
from uuid import UUID
from pathlib import Path


class BlogOut(BaseModel):
    blog_id: UUID
    text: str
