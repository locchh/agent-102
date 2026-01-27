# DeepAgent

## Setup

## Run local server
```bash
langgraph dev --no-browser
```

## Run UI

```bash
$ git clone https://github.com/langchain-ai/deep-agents-ui.git
$ cd deep-agents-ui
$ yarn install
$ yarn dev
```

**Note**:  If get trouble with TLS certificate, please set environment variable `NEXT_TURBOPACK_EXPERIMENTAL_USE_SYSTEM_TLS_CERTS=1`:

```bash
NEXT_TURBOPACK_EXPERIMENTAL_USE_SYSTEM_TLS_CERTS=1 yarn dev
```

You can get the Deployment URL and Assistant ID from the terminal output and langgraph.json file, respectively:

- Deployment URL: `http://127.0.1:2024`
- Assistant ID: `research`


## References

[DeepAgents Examples](https://github.com/langchain-ai/deepagents/tree/master/examples)

[DeepAgents UI](https://github.com/langchain-ai/deep-agents-ui)

[DeepAgents CLI](https://docs.langchain.com/oss/python/deepagents/cli)