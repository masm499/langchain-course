from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()  # Load environment variables from .env file


def main():

    information = """Imran Ahmed Khan Niazi is a Pakistani former cricketer, philanthropist, and politician who served as the 19th prime minister of Pakistan from August 2018 until April 2022. As a cricketer, he captained the Pakistan national cricket team to victory in the 1992 Cricket World Cup."""

    prompt_template = """ given the information {information} about a person, i want you to create:
     1. A short summary of the person in 2-3 sentences.
     2. Two interesting facts about the person."""
    # notice every prompt part is referring the context, more specific, better i.e. "about a person -> cricketer","of the person ->cricketer"

    prompt = PromptTemplate(input_variables=["information"], template=prompt_template)
    # Breaking down prompts this way saves from prompt injection attacks , reusable
    # also makes it easier to debug the prompts.

    # picks key from .env named GOOGLE_API_KEY
    # temperature controls random vs strict (deterministic) vs creative outcome is
    # 0- 0.5 deterministic
    # 0.5 to 1.0 poetry fiction creative ideas.

    # max_output_tokens controls the length of the output, None means no limit
    #llm = ChatGoogleGenerativeAI(
    #    model="gemini-3.5-flash", temperature=1.0, max_output_tokens=None
    #)
    llm = ChatOllama(model="gemma3:270m", temperature=0.0, max_output_tokens=None);

    # building the chain with llm and prompt template using langchain expression language
    # this is chain of two components and we read it left to right.
    chain = prompt | llm
    response = chain.invoke(input={"information": information})
    # We need something to parse the text and thats where NLP will shine.
    print(response)


if __name__ == "__main__":
    main()
