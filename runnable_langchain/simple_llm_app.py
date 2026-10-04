from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest catchy blog title about {topic}."
)

topic = input("Enter a topic: ")

formatted_prompt = prompt.format(topic=topic)

blog_title = llm.invoke(formatted_prompt)

# result
print("Generated Blog title: ", blog_title.content)

