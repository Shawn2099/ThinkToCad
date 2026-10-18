# Open-Source AI Agent Toolkit Design Patterns

## How does LangChain define tools (BaseTool, @tool decorator, StructuredTool, ToolNode)?

### Takeaway
LangChain treats tools as callable objects with a name, description, and Pydantic args_schema; plain functions/callables are auto-converted, and ToolNode handles execution in LangGraph.

### Cited Findings
- Tools are defined as callable functions with well-defined inputs/outputs passed to a chat model; the model decides when to invoke them — [LangChain Tools docs](https://docs.langchain.com/oss/python/langchain/tools).
- The simplest creation path is the `@tool` decorator; type hints define the input schema and the docstring becomes the description — [LangChain Tools docs](https://docs.langchain.com/oss/python/langchain/tools).
- `create_agent` accepts `tools: Sequence[BaseTool | Callable | dict]`, mixing BaseTool instances, plain callables, and provider built-in tools (dicts) — [create_agent reference](https://reference.langchain.com/python/langchain/agents/create_agent).
- ToolNode is the LangGraph node that executes tools; it supports parallel execution, error handling, state injection, and Command-based state updates; inputs can be graph state with a messages key, a message list, or direct tool calls — [ToolNode reference](https://reference.langchain.com/python/langgraph.prebuilt/tool_node/ToolNode).
- ToolNode constructor: `tools`, `handle_tool_errors` (bool/str/callable/type/tuple, default catches invocation errors), `messages_key`, `wrap_tool_call`/`awrap_tool_call` — [ToolNode reference](https://reference.langchain.com/python/langgraph.prebuilt/tool_node/ToolNode).
- StructuredTool represents an action wrapping any function; defined by `name`, `description`, `args_schema` (Pydantic BaseModel), and `_run`/`_arun` methods; older string-input `Tool` shares the same BaseTool base class (forwards compatible) — [LangChain Structured Tools blog](https://www.langchain.com/blog/structured-tools).
- In `create_agent` factory, tools are split into built-in provider tools (dicts) and regular tools; a ToolNode is created from available_tools + middleware tools, and its `tools_by_name` becomes the default tool set — [factory.py](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py).

### Inferences
- LangChain's design favors a single BaseTool abstraction with multiple construction paths (subclass, decorator, StructuredTool, plain function), letting the same tool work across agents and graphs.

### Gaps
- Exact current BaseTool class hierarchy in langchain-core (e.g., whether `Tool` still exists as a separate subclass) not verified from primary source beyond the 2023 blog; APIs may have evolved.

## How does LlamaIndex define tools (FunctionTool, QueryEngineTool)?

### Takeaway
LlamaIndex centers on `AsyncBaseTool` with metadata; FunctionTool wraps arbitrary sync/async functions with auto-inferred schemas and optional context injection, while QueryEngineTool wraps a query engine and supports `return_direct`.

### Cited Findings
- A Tool is a generic interface implementing `__call__` plus metadata (name, description, function schema); `FunctionTool` converts any function, `QueryEngineTool` wraps a query engine (agents inherit BaseQueryEngine so tools can wrap agents), plus community ToolSpecs and utility tools — [LlamaIndex Tools docs](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/).
- FunctionTool created via `FunctionTool.from_defaults(fn, name=..., description=...)`; type hints and docstrings drive schema; `Annotated` types specify arg descriptions; async functions supported via `async_fn` — [LlamaIndex Tools docs](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/).
- FunctionTool inspects signature to detect a context parameter (`requires_context`, `ctx_param_name`) and supports callbacks (`callback`/`async_callback`) and `partial_params` — [FunctionTool API](https://developers.llamaindex.ai/python/framework-api-reference/tools/function/).
- FunctionTool and QueryEngineTool both subclass `AsyncBaseTool` and expose `call`/`acall` returning `ToolOutput` (content, tool_name, raw_input, raw_output) — [FunctionTool API](https://developers.llamaindex.ai/python/framework-api-reference/tools/function/); [QueryEngineTool API](https://developers.llamaindex.ai/python/framework-api-reference/tools/query_engine/).
- QueryEngineTool.from_defaults takes `query_engine`, `name`, `description`, `return_direct`, `resolve_input_errors`; `return_direct=True` ends the agent loop and returns the tool result directly — [LlamaIndex Tools docs](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/).
- LlamaIndex supports tool retrieval at query time via `ObjectIndex`/`ObjectRetriever` passed as `tool_retriever` to agents, to handle large tool catalogs — [Retrieval-Augmented Agents](https://developers.llamaindex.ai/python/examples/agent/openai_agent_retrieval/).

### Inferences
- The `return_direct` flag is a distinctive pattern for terminal tools (e.g., query engines) that should bypass further LLM rewriting.

### Gaps
- Exact `AsyncBaseTool`/`ToolMetadata` base definitions and `BaseTool` (sync) hierarchy not fully verified; `ToolSpec` internals not covered.

## How does CrewAI define tools (@tool, BaseTool, tool delegation)?

### Takeaway
CrewAI offers two construction paths (BaseTool subclass with `_run`/`_arun` and `@tool` decorator) built on Pydantic args schemas, plus tool-level controls (result_as_answer, max_usage_count, caching) and agent-level delegation hooks.

### Cited Findings
- Subclass `BaseTool` with `name`, `description`, `args_schema: Type[BaseModel]`, and `_run` (sync) / `_arun` (async) methods; the decorator `@tool("Name")` builds a `Tool` from a function's type annotations and docstring, generating a Pydantic args schema via `create_model` — [Create Custom Tools](https://docs.crewai.com/edge/en/learn/create-custom-tools); [base_tool.py](https://github.com/crewAIInc/crewAI/blob/c0fa66d1/lib/crewai/src/crewai/tools/base_tool.py).
- `@tool` supports `result_as_answer` (tool result becomes final answer) and `max_usage_count` (usage cap) — [base_tool.py](https://github.com/crewAIInc/crewAI/blob/c0fa66d1/lib/crewai/src/crewai/tools/base_tool.py).
- Typed outputs: CrewAI infers an output schema when a BaseTool has a Pydantic return annotation; the agent receives JSON based on the output model — [Create Custom Tools](https://docs.crewai.com/edge/en/learn/create-custom-tools).
- Custom caching via `cache_function` assigned per tool; async tools supported; framework handles sync/async execution automatically — [Tools concepts](https://docs.crewai.com/edge/en/concepts/tools).
- Tool delegation: agents can delegate work to coworkers via injected `Delegate work to coworker` / `Ask question to coworker` tools; hooks (`before_tool_call`/`after_tool_call`) gate execution; authority can narrow monotonically across delegation — [Attenu recipe](https://attenu.io/docs/example-crewai/).
- `to_langchain` converts CrewAI tools to `CrewStructuredTool` for LangChain interop — [base_tool.py](https://github.com/crewAIInc/crewAI/blob/c0fa66d1/lib/crewai/src/crewai/tools/base_tool.py).

### Inferences
- CrewAI's tool model is the most "policy-aware" of the surveyed frameworks, with built-in usage caps and delegation hooks.

### Gaps
- Exact BaseTool base class (whether it wraps LangChain's BaseTool) and internal execution loop details not fully verified from source beyond snippets.

## How does AutoGen/AG2 define tools (FunctionTool, tool registration)?

### Takeaway
AutoGen wraps any function in `FunctionTool`, which auto-generates a JSON schema from type annotations/descriptions; tools subclass `BaseTool` and are passed directly to model clients; execution is explicit via `run_json` with cancellation tokens.

### Cited Findings
- `FunctionTool(func, description=...)` wraps a function; type annotations (with `Annotated` descriptions) generate the schema; every tool subclasses `BaseTool` exposing `.schema`, `.run_json(args, cancellation_token)`, `.return_value_as_string(result)` — [AutoGen Tools guide](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html).
- Tools are passed to `model_client.create(messages=..., tools=[...])`; the client returns `FunctionCall` objects; the caller executes tools (example uses `asyncio.gather` for parallel calls) and feeds `FunctionExecutionResult` back — [AutoGen Tools guide](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html).
- Built-in tools include code execution, GraphRAG search, MCP server tools, HTTP tool, LangChain adapter — [AutoGen Tools guide](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html).
- Tool-equipped agents implement their own loop; AgentChat provides pre-built agents — [AutoGen Tools guide](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html).

### Inferences
- AutoGen's design separates tool definition, model calling, and execution orchestration, leaving parallelism to user code (e.g., asyncio.gather).

### Gaps
- AG2 (community fork) specifics not separately verified; assumed largely compatible with AutoGen core tool API. Built-in tool list and MCP adapter internals not deeply inspected.

## How does Pydantic AI define tools (@agent.tool, RunContext, tool schemas)?

### Takeaway
Pydantic AI registers tools via decorators or a `tools` list; `RunContext` injects dependencies; schemas are auto-generated from signatures + Pydantic, with rich docstring extraction and advanced toolsets.

### Cited Findings
- Registration paths: `@agent.tool` (needs context), `@agent.tool_plain` (no context), or `tools=[fn, Tool(fn, takes_ctx=...)]` in Agent constructor — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).
- `RunContext` provides `ctx.deps` (dependencies) and `ctx.enqueue` for injecting follow-up messages; tools can return any Pydantic-serializable value — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).
- Schema: function parameters (except RunContext) build the JSON schema; docstrings (google/numpy/sphinx styles) are parsed via griffe for parameter descriptions; `require_parameter_descriptions=True` enforces docs — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).
- Toolsets manage collections of tools and can be combined; tools/toolsets gathered into a single combined toolset available to the model; supports MCP servers and third-party tools — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).
- Native tools, common tools, deferred tools (approval/external execution), and advanced features (custom schemas, dynamic tools, retries) documented separately — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).

### Inferences
- Pydantic AI's context-injection pattern (`RunContext`) is a clean way to give tools access to per-run dependencies without global state.

### Gaps
- Advanced tool execution/retry behavior and toolset internals not fetched; deferred tools details not covered.

## How does smolagents define tools (Tool class, @tool decorator, CodeAgent tools)?

### Takeaway
smolagents models a tool as a class wrapping a `forward` method with explicit `name`, `description`, `inputs` (JSON-schema-ish types), and `output_type`; a `@tool` decorator exists for simple functions, and CodeAgent executes tools by generating Python code.

### Cited Findings
- A tool subclasses `Tool` and defines `name`, `description`, `inputs` (dict with type/description), `output_type`, and `forward(...)` method; types are Pydantic JSON-schema formats — [smolagents Tools tutorial](https://huggingface.co/docs/smolagents/en/tutorials/tools).
- `@tool` decorator is the recommended way for simple tools; subclassing `Tool` is for complex/multi-method tools — [smolagents Tools tutorial](https://huggingface.co/docs/smolagents/en/tutorials/tools).
- Tools can be shared/loaded from the Hub (`push_to_hub`, `load_tool`, `from_hub`), imported from MCP servers (`MCPClient`, `ToolCollection.from_mcp`), LangChain (`Tool.from_langchain`), and Gradio Spaces (`Tool.from_space`) — [smolagents Tools tutorial](https://huggingface.co/docs/smolagents/en/tutorials/tools).
- `structured_output=True` on MCPClient enables JSON-schema-aware tool outputs; toolbox is a standard dict (`agent.tools[name] = tool`) — [smolagents Tools tutorial](https://huggingface.co/docs/smolagents/en/tutorials/tools).
- CodeAgent writes actions as Python code (function nesting, loops, conditionals) to invoke tools; ToolCallingAgent uses JSON/text tool-calling — [smolagents index](https://huggingface.co/docs/smolagents/en/index).

### Inferences
- smolagents' explicit `inputs`/`output_type` metadata (rather than inferring from Python signatures) makes tools self-describing and shareable across runtimes.

### Gaps
- `@tool` decorator signature and `Tool.forward` execution/error-handling details not fully verified; default tool execution parallelism in CodeAgent not confirmed.

## How do these frameworks handle tool execution (parallel, sequential, error handling)?

### Takeaway
Execution models vary: LangGraph's ToolNode handles parallel execution + configurable error handling; Pydantic AI and AutoGen leave orchestration to user/agent code (often asyncio.gather); CrewAI auto-handles sync/async; LlamaIndex agents execute all calls then loop.

### Cited Findings
- LangGraph ToolNode "handles parallel tool execution, error handling, and state injection automatically"; `handle_tool_errors` supports True/str/callable/type/tuple/False with default catching invocation errors only — [ToolNode reference](https://reference.langchain.com/python/langgraph.prebuilt/tool_node/ToolNode).
- LangChain `create_agent` runs the tool loop until no tool_calls remain; tools node adds ToolMessage objects — [create_agent reference](https://reference.langchain.com/python/langchain/agents/create_agent).
- LlamaIndex agents: tool schemas + history sent to LLM; every tool call executed; results added to history; agent re-invoked until done — [LlamaIndex Agents docs](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/).
- AutoGen example executes tool calls with `asyncio.gather(...)` (parallel) and wraps exceptions into `FunctionExecutionResult(is_error=True)` — [AutoGen Tools guide](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html).
- CrewAI "automatically handles execution of both synchronous and asynchronous tools"; hooks gate pre/post execution — [Tools concepts](https://docs.crewai.com/edge/en/concepts/tools); [Attenu recipe](https://attenu.io/docs/example-crewai/).
- Pydantic AI tool retries and execution details documented under advanced tool features (not fetched in depth) — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).

### Inferences
- A common pattern: execute all tool calls from one LLM turn (often in parallel), then feed results back in a single batched message.

### Gaps
- Whether LlamaIndex executes multiple calls in parallel vs sequentially not confirmed. Pydantic AI retry/parallelism specifics not verified.

## How do they handle tool discovery and registration?

### Takeaway
Registration ranges from constructor lists/decorators (LangChain, Pydantic AI, CrewAI) to runtime dictionaries (smolagents), plus dynamic discovery via tool retrieval (LlamaIndex) and external sources (MCP, Hub, LangChain adapters).

### Cited Findings
- LangChain: `create_agent(tools=[...])` accepts BaseTool/Callable/dict; middleware can add tools; ToolNode converts to `tools_by_name` — [create_agent](https://reference.langchain.com/python/langchain/agents/create_agent); [factory.py](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py).
- LlamaIndex: agent constructor `tools=[...]` or `tool_retriever=...` for query-time retrieval; `ToolSpec.to_tool_list()` for bundles — [LlamaIndex Tools docs](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/tools/).
- CrewAI: tools passed to Agent; `@tool` decorator methods can be referenced in YAML config; delegation tools injected by framework — [Using Annotations](https://docs.crewai.com/edge/en/learn/using-annotations); [Attenu recipe](https://attenu.io/docs/example-crewai/).
- AutoGen: tools passed to `model_client.create(tools=...)` or agent constructor; no central registry beyond lists — [AutoGen Tools guide](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/tools.html).
- Pydantic AI: decorators or `tools=`/`toolsets=`; toolsets combine tools and can wrap MCP/third-party — [Pydantic AI Tools](https://ai.pydantic.dev/tools/).
- smolagents: `agent.tools` is a dict keyed by tool name; `ToolCollection` loads from MCP/Hub; interop with LangChain/MCP/Spaces — [smolagents Tools tutorial](https://huggingface.co/docs/smolagents/en/tutorials/tools).

### Inferences
- Most frameworks treat the tool list as the source of truth; only LlamaIndex and smolagents emphasize dynamic retrieval/loading at scale.

### Gaps
- Formal "tool registry" or plugin discovery mechanisms (entry points) not covered for any framework.

## What are the common patterns across all frameworks (tool schema, tool result, tool executor)?

### Takeaway
Common core: (1) a tool = name + description + JSON-schema args + callable implementation; (2) results are string/structured payloads returned to the model; (3) an executor runs calls and feeds results back; (4) context/dependency injection and async support are increasingly standard.

### Cited Findings
- Schema: all frameworks derive JSON schemas from type annotations/Pydantic models/docstrings (LangChain args_schema, LlamaIndex ToolMetadata, CrewAI args_schema, AutoGen BaseTool.schema, Pydantic AI parameters_json_schema, smolagents inputs) — sources above.
- Result: LangChain ToolMessage; LlamaIndex ToolOutput (content/raw_output); AutoGen FunctionExecutionResult (content, is_error); Pydantic AI ToolReturnPart; CrewAI returns tool output (typed via Pydantic); smolagents forward return — sources above.
- Executor: LangChain ToolNode; LlamaIndex agent loop; AutoGen explicit user orchestration; CrewAI framework-managed; Pydantic AI agent run loop; smolagents CodeAgent/ToolCallingAgent — sources above.
- Context injection: LlamaIndex `requires_context`; Pydantic AI `RunContext`; LangChain ToolNode state injection; CrewAI delegation hooks — sources above.
- Async support: LlamaIndex acall; CrewAI `_arun`; AutoGen async functions; Pydantic AI async tools; LangChain `_arun` — sources above.
- Interop: LangChain↔CrewAI (`to_langchain`), LangChain↔smolagents (`from_langchain`), LangChain↔AutoGen adapter, Pydantic AI third-party/MCP toolsets — sources above.

### Inferences
- Convergent design: frameworks are converging on Pydantic/JSON-schema-driven tool definitions, async-first execution, and MCP as the universal tool transport.

### Gaps
- No benchmarks or performance comparisons available; "best" pattern cannot be determined from docs alone.
- Version currency: docs fetched reflect late-2025/2026 versions; APIs may shift.
