from dotenv import load_dotenv;
from langchain.agents import create_agent;
from langchain_google_genai import ChatGoogleGenerativeAI;
from langchain.tools import tool;
from langchain.messages import HumanMessage;
from tavily import TavilyClient;

load_dotenv();


@tool #converts a python function into a tool that can be used by the agent
def search(query: str) -> str:
    """Searches for the given query over the internet
    Args:
        query : The search query parameter.
    Returns:
        str: The search results.
    """
    client = TavilyClient()
    response = client.search(query, language="en");
    return response;

def main():
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0.3,max_output_tokens=None);
    tool_list = [search];
    agent = create_agent(model=llm, tools=tool_list);
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 remote job postings for an ai engineer using langchain")});
    print(result);

if __name__ == "__main__":
    main();