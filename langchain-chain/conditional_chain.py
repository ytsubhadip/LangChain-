from dotenv import load_dotenv
import os

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from operator import itemgetter

load_dotenv()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )

model = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API")
)

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback}\n{formate_instraction}",
    input_variables=["feedback"],
    partial_variables={"formate_instraction": parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write a appropiate simple response to this possetive feedback\n {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write a appropiate simple response to this negative feedback\n {feedback}",
    input_variables=["feedback"]
)

classification_chain = RunnableParallel(
    feedback=itemgetter("feedback"),
    sentiment=prompt1 | model | parser2,
)

# result = classification_chain.invoke({'feedback':'this product is very badly pack but qualy alos mediam'})

branch_chain = RunnableBranch(
    (lambda x: x["sentiment"].sentiment == "positive", prompt2 | model | parser),
    (lambda x: x["sentiment"].sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classification_chain | branch_chain

AI_feedback = chain.invoke({'feedback':'this product is very good'})

print(AI_feedback)









