import os
import urllib3
import requests

from dotenv import load_dotenv

load_dotenv()

import textwrap
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI

# Disable SSL warnings and certificate verification for development
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Monkey patch requests to disable SSL verification globally
original_request = requests.Session.request


def patched_request(self, method, url, **kwargs):
    kwargs.setdefault("verify", False)
    return original_request(self, method, url, **kwargs)


requests.Session.request = patched_request

# Create llm client
model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("MODEL_API_KEY"),
    base_url=os.getenv("MODEL_BASE_URL"),
    temperature=0.5,
    timeout=10,
    max_completion_tokens=1000,
)

# Create a search tool

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# Create a deep agent

# System prompt to steer the agent to be an expert researcher
research_instructions = textwrap.dedent(
    """
    You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

    You have access to an internet search tool as your primary means of gathering information.

    ## `internet_search`

    Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
    """
)

agent = create_deep_agent(
    model=model, tools=[internet_search], system_prompt=research_instructions
)

if __name__ == "__main__":
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is langgraph?"}]}
    )

    # Print the agent's response
    print(result["messages"][-1].content)
