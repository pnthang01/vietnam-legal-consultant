from dotenv import load_dotenv

load_dotenv()

from mirascope import llm
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str

@llm.call(provider="openai", model="gpt-4o-mini", response_model=Book)
def extract_book(text: str) -> str:
    return f"Extract {text}"

book = extract_book("The Name of the Wind by Patrick Rothfuss")
assert isinstance(book, Book)
print(book)
# Output: title='The Name of the Wind' author='Patrick Rothfuss'