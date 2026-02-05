# Langchain ecosystem

```text
                                   General Agent

   +-------------+           +-----------------------+          +--------------+
   |  Filesystem |           |         Agent         |          | MCP server 1 |
   |  +-------+  |           |    +-------------+    |          +--------------+
   |  | Skill |  |           |    |     LLM     |    |          | MCP server 2 |
   |  +-------+  | <-------  |    +-------------+    | -------->+--------------+
   |  | Skill |  |           |           ^           |          | MCP server 3 |
   |  +-------+  |           |           |           |          +--------------+
   |  | Skill |  |           |    +-------------+    |
   |  +-------+  |           |    |    Tools    |    |
   |             |           |    +-------------+    |
   +-------------+           +----------+------------+
                                        |
                  +---------------------+---------------------+
                  |                     |                     |
           +------------+        +------------+        +------------+
           |  Subagent  |        |  Subagent  |        |  Subagent  |
           +------------+        +------------+        +------------+
```

*1. What is the use case?* → *Agent design pattern, e.g., general agent, multi-agent, etc.*

*2. What is the input/output?* → *Input: natural language, output: natural language, markdown, PDF, etc.*

*3. What are the characteristics?* → *e.g., stateless, stateful, multi-hop, guardrail, etc.*

*4. How to interact with the agent?* → *Through TUI, Web UI, or API, etc.*

*5. Technical engineering* → *AGENTS.md, skills, tools, MCP servers, memory, etc.*

*6. How to test?* → *Unit tests, integration tests, etc.*

*7. How to evaluate and trace?* → *Token usage, latency, quality, etc.*

*8. How to deploy and scale?* → *LangSmith, AgentCore, etc.*

My appoarch *Tools -> Agent -> AGENTS.md -> Skills*.

## Frameworks

- [langchain](https://github.com/langchain-ai/langchain)

- [langgraph](https://github.com/langchain-ai/langgraph)

- [langgraph-cli](https://docs.langchain.com/langsmith/cli)

- [deepagents](https://github.com/langchain-ai/deepagents)

- [langgraph-sdk](https://pypi.org/project/langgraph-sdk/)

## References

- [Langchain Docs](https://docs.langchain.com/)

- [Langchain Reference](https://reference.langchain.com/python/)

- [LangSmith Platform](https://smith.langchain.com)

- [DeepAgents Documentation](https://docs.langchain.com/oss/python/deepagents/overview)

- [DeepAgents Repository](https://github.com/langchain-ai/deepagents)

- [DeepAgents UI](https://github.com/langchain-ai/deep-agents-ui)

- [DeepAgents CLI](https://docs.langchain.com/oss/python/deepagents/cli)

- [DeepAgents Examples](https://github.com/langchain-ai/deepagents/tree/master/examples)

- [DeepAgents Example Skills](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/skills)

- [AgentSkills](https://github.com/agentskills/agentskills)

- [AGENTS.md](https://agents.md/)

- [Claude Think Tool](https://www.anthropic.com/engineering/claude-think-tool)

- [Tavily Search API](https://docs.tavily.com/documentation/api-reference/endpoint/search)
