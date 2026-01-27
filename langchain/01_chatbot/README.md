# simple chatbot

## Setup

### 1.Environment

```bash
# Virtual environment
uv venv .venv

# Activate virtual environment
source .venv/bin/activate

# Init environment variables (Optional)
cp .env.example .env

# Test call LLM
pytest tests/test_llm.py
```

### 2.Local server

#### 2.1. Install the LangGraph CLI

The [LangGraph CLI](https://docs.langchain.com/langsmith/cli) provides a local development server (also called [Agent Server](https://docs.langchain.com/langsmith/agent-server)) that connects your agent to Studio:

```bash
# Python >= 3.11 is required.
uv pip install --upgrade "langgraph-cli[inmem]"
```

#### 2.2. Prepare your agent

#### 2.3. Environment variables (Optional)

Studio requires a LangSmith API key to connect your local agent. Create a `.env` file in the root of your project and add your API key from LangSmith. You will need set `LANGSMITH_API_KEY` environment variable if you want to connect your local agent to Studio. If you just want to start the local server, you can skip this step.

```bash
LANGSMITH_API_KEY=lsv2...
```

#### 2.4. Create a LangGraph config file

The LangGraph CLI uses a configuration file to locate your agent and manage dependencies. Create a `langgraph.json` file in your app’s directory:

```json
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./my_simple_agent/agent.py:agent"
  },
  "env": ".env"
}
```

#### 2.5. View your agent in Studio

Start the development server to connect your agent to Studio: `langgraph dev` or `langgraph dev --no-browser` to disable opening browser. Once the server is running, your agent is accessible both via API at `http://127.0.0.1:2024` and through the Studio UI at `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`

### 3. Agent Chat UI

First, clone the repository:

```bash
git clone https://github.com/langchain-ai/agent-chat-ui.git

cd agent-chat-ui
```

Install dependencies:

```bash
npm install
```

Copy the `.env.example` file to a new file named `.env`:

```bash
cp .env.example .env
```

Run the app:

```bash
npm run dev
```

The UI app will be available at `http://localhost:3000`. and you can connect to your local agent at `http://127.0.0.1:2024`.

## Structure

- LangChain Example Structure:

```
my-app/
├── my_agent
│   ├── utils
│   │   ├── __init__.py
│   │   └── tools.py
│   ├── __init__.py
│   └── agent.py
├── .env
├── requirements.txt
└── langgraph.json
```

- LangGraph Example Structure:

```
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
├── requirements.txt # package dependencies
└── langgraph.json # configuration file for LangGraph
```

## References
- [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui.git)
- [LangChain Documentation](https://docs.langchain.com/oss/python/langchain)
- [LangSmith Studio](https://docs.langchain.com/oss/python/langchain/studio)
- [File structure](https://docs.langchain.com/oss/python/langgraph/application-structure)