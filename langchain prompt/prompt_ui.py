import os

import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

# model config
llm = ChatMistralAI(
            model="mistral-small-latest",
            api_key=os.getenv("MISTRAL_API"),
            temperature=0.7
        )


# create streamlit ui 

st.header("Research Tool")

# show all input field

paper_input = st.selectbox("Select Research Paper Name", ["Setect....", "Attention Is All You Need", "BERT: Pre-tranning of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Images Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical","Code-Oriented","Mathematical"])

length_input = st.selectbox("Selct Explanation Lenght", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)","Long (detailed explanation)"])

template = load_prompt("template.json")


if st.button("Summarize"):
        chain = template|llm
        # fill the placeholder
        result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input

            })
        
        st.write(result.content)























        