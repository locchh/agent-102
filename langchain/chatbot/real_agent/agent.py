import os

from dotenv import load_dotenv

load_dotenv()

import textwrap

from dataclasses import dataclass

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy


# Define the system prompt
SYSTEM_PROMPT = textwrap.dedent(
    """
    You are an expert weather forecaster, who speaks in puns.

    You have access to two tools:

    - get_weather_for_location: use this to get the weather for a specific location
    - get_user_location: use this to get the user's location

    If a user asks you for the weather, make sure you know the location.
    If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location.
    """
)


# Define the runtime context
@dataclass
class MyRuntimeContext:
    """Custom runtime context schema."""

    user_id: str = "default"  # Set default user id


# Define the tools
@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


@tool
def get_user_location(runtime: ToolRuntime[MyRuntimeContext]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    if user_id == "1":
        return "Florida"
    elif user_id == "default":
        return "New York"  # Default location
    else:
        return "SF"


# Create llm client
model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("MODEL_API_KEY"),
    base_url=os.getenv("MODEL_BASE_URL"),
    temperature=0.5,
    timeout=10,
    max_completion_tokens=1000,
)


# Define the response format
# We use a dataclass here, but Pydantic models are also supported.
@dataclass
class ResponseFormat:
    """Response schema for the agent."""

    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None


# Create agent with conditional checkpointer
# Only add checkpointer when running directly (not via langgraph dev)
def create_my_agent(use_checkpointer=False, use_response_format=False):
    return create_agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[get_user_location, get_weather_for_location],
        context_schema=MyRuntimeContext,
        response_format=ToolStrategy(ResponseFormat) if use_response_format else None,
        checkpointer=InMemorySaver() if use_checkpointer else None,
    )


# For langgraph dev (no checkpointer)
agent = create_my_agent(use_checkpointer=False, use_response_format=False)

if __name__ == "__main__":
    # For direct Python execution (with checkpointer)
    agent = create_my_agent(use_checkpointer=True, use_response_format=True)

    # `thread_id` is a unique identifier for a given conversation.
    config = {"configurable": {"thread_id": "1"}}

    # Turn 1
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "what is the weather outside?",
                }
            ]
        },
        config=config,
        context=MyRuntimeContext(user_id="1"),
    )

    print(response["structured_response"])
    # ResponseFormat(
    #     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
    #     weather_conditions="It's always sunny in Florida!"
    # )

    # Note that we can continue the conversation using the same `thread_id`.
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "thank you!",
                }
            ]
        },
        config=config,
        context=MyRuntimeContext(user_id="1"),
    )

    print(response["structured_response"])
    # ResponseFormat(
    #     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
    #     weather_conditions=None
    # )
