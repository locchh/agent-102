import sys
import os
from dotenv import load_dotenv

load_dotenv()

import pytest

from langchain_openai import ChatOpenAI

def test_llm():
    """Test LLM initialization with environment variables."""
    llm_client = ChatOpenAI(
        model=os.getenv("MODEL_NAME"),
        api_key=os.getenv("MODEL_API_KEY"),
        base_url=os.getenv("MODEL_BASE_URL"),
    )
    assert llm_client is not None

    # Test that the LLM can generate a simple response
    response = llm_client.invoke("Hello, how are you?")
    assert response.content is not None
    assert len(response.content) > 0

if __name__ == "__main__":
    sys.exit(pytest.main(["-v", __file__]))