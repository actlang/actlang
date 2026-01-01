# actlang
An Action-First Framework to simplify Building Autonomous AI Agents | An early-stage open-source Agentic framework designed to build highly scalable multi-agents system


# ActLang — Core Philosophy

Agents don’t think. Actions do.
Agents only orchestrate actions.

There are many AI Agents development frameworks

They are tool-first, some are graph-first

ActLang is action-first

Users define what happens, not how graph work

# Background & Motivation

Core Concepts
You only need 4 core abstractions:

Agent
Action
Tool
State


Everything else is sugar.

# Core Architecture & patterns


1️⃣ Agent (Orchestrator, not executor)

What an Agent is NOT
❌ Not a prompt
❌ Not a tool caller
❌ Not a workflow

What an Agent IS
✅ A container of Actions
✅ A policy for sequencing
✅ A state owner

Agent Responsibilities

Accept input

Maintain shared state

Decide which action runs next

Return final output



Agent API (User-facing)
from actlang import Agent
```
agent = Agent(
    name="OutfitAdvisor",
    actions=[
        LLMChatAction("What should I wear today? some suggestion...!")
        GetWeather(),
        DecideOutfit(),
        RespondUser()
    ]
)

```

That’s it.
No graphs. No chains. No nodes.


2️⃣ Action (Core Primitive)

Actions are the heart of ActLang.

If an action is clear, the agent is simple.

Action Contract

Each Action must:

Receive state

Optionally call tools

Optionally call LLM

Update state

Return control

Action Interface

```
class Action:
    name: str

    def run(self, state: AgentState) -> ActionResult:
        ...

```

ActionResult
```

class ActionResult:
    next_action: str | None
    state_update: dict
    done: bool = False
```


3️⃣ Tools (Pure Side Effects)

Tools must be dumb and deterministic.

Tools should never know about LLMs or Agents.

Tool Rules

No prompts

No memory

No orchestration logic

Just input → output
```

class WeatherTool(Tool):
    def run(self, city: str) -> dict:
        return {
            "temp": 32,
            "condition": "sunny"
        }
```


4️⃣ State (Shared Memory)

State is the only thing that flows between actions.
```

class AgentState(BaseModel):
    user_query: str
    weather: dict | None = None
    decision: str | None = None
    response: str | None = None
```



How Example Maps Cleanly
User Flow
User → Agent → Actions → Tools → LLM → Response

Concrete Implementation
```

class GetWeather(Action):
    def run(self, state):
        weather = WeatherTool().run(city="London")
        return ActionResult(
            state_update={"weather": weather},
            next_action="DecideOutfit"
        )


class DecideOutfit(Action):
    def run(self, state):
        result = llm.complete(
            f"Weather: {state.weather}. What should I wear?"
        )
        return ActionResult(
            state_update={"decision": result},
            next_action="RespondUser"
        )

class RespondUser(Action):
    def run(self, state):
        return ActionResult(
            state_update={"response": state.decision},
            done=True
        )
```

Internal Architecture (Important)
ActLang Internal Layers
┌──────────────────────────┐
│  User Code (Agent DSL)   │
├──────────────────────────┤
│  Agent Runtime           │
│  - Action registry       │
│  - State manager         │
├──────────────────────────┤
│  Action Graph Compiler   │  ← YOUR SECRET SAUCE
│  - Action → Node         │
│  - Next-action routing   │
├──────────────────────────┤
│  Execution     │
├──────────────────────────┤
│  LangGraph/LangChain/ LlamaIndex / LLM / Tools │ External Tool or Libraries
└──────────────────────────┘


# Patterns

1️⃣ Action-First DSL

Actions should feel like functions, not prompts.

2️⃣ Deterministic Execution

No hidden auto-magic loops.

3️⃣ Explicit State

No magic memory injection.

4️⃣ Compile, Don’t Execute

User defines intent → ActLang compiles it.


ActLang is to agent workflows what FastAPI is to web APIs.

Opinionated

Minimal

Compile-time clarity

Runtime power

My Honest Advice

If you do only one thing right, do this:

Make Actions stupidly simple and deterministic.

Everything else will fall into place.



# ActLang — Core Architecture (Canonical)
Foundational Rules

Agent only knows Actions

Agent has zero knowledge of tools, LLMs, APIs, or LangGraph

Agent is an orchestrator, not an executor

Agent executes Actions sequentially

One action at a time

Order is explicit

No hidden auto-routing

Action is the smallest unit of work

An Action can call one or more tools

An Action may call LLM

Tools never call tools

Tools never call LLMs

Action has only two terminal states

✅ SUCCESS → returns data

❌ FAILURE → returns error

Failure is fatal

Any failed action halts the entire workflow

Error is returned as final output

Underlying execution is LangGraph

Actions → Nodes

Sequence → Edges

ActLang compiles, then executes

## High-Level Runtime Flow

User Input
   ↓
Agent
   ↓
Action 1 ──▶ SUCCESS ──▶ Action 2 ──▶ SUCCESS ──▶ Action N
     │
     └──▶ FAILURE → STOP → Error Output


# Become Part of the Future AI Learning Community
https://actlang.github.io/
