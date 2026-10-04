import os

from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    api_key= os.getenv("MISTRAL_API")
)

# create ctructure output
class Review(TypedDict):
    key_themes: Annotated[list[str],"write down all the key themes in the revier in a list"]
    summery: Annotated[str,"a brief summery of the review"]
    sentiment: Annotated[Literal["POS","NEG"], "give the sentiment with positive or nutral or negative"]
    pros: Annotated[Optional[list[str]],"write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside the list"]

# crate a pydentic object
class PYDENTCI_REVIEW(BaseModel):
    key_themes : list[str] = Field(description="write down all the key themes in the revier in a list")
    summery : str = Field(description="a brief summery of the review")
    sentiment : Literal["POS","NEG"] = Field(description="give the sentiment with positive or nutral or negative")
    pros : Optional[list[str]] = Field(default=None,description="write down all the pros inside the list")
    cons : Optional[list[str]] = Field(default=None,description="write down all the cons inside the list")
    name : Optional[str] = Field(default=None, description="reviewer name ")

structure_model = model.with_structured_output(PYDENTCI_REVIEW)
# user_review_text = """
# The sound is decent but the fitting is not good, it comes out from the ear again and again.
# """

user_review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 

"""

result = structure_model.invoke(user_review_text)
result =dict(result)
print(result)