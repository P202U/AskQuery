from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command


def init_model(model_name: str):
    return ChatGoogleGenerativeAI(model=model_name, temperature=0)


def create_sql_agent(model, tools, system_prompt):
    agent = create_agent(
        model,
        tools,
        system_prompt=system_prompt,
        middleware=[
            HumanInTheLoopMiddleware(
                interrupt_on={"sql_db_query": True},
                description_prefix="Tool execution pending approval",
            )
        ],
        checkpointer=InMemorySaver(),
    )
    return agent


def run_agent(agent, question, thread_id="1"):
    config = {"configurable": {"thread_id": thread_id}}

    active_stream = agent.stream(
        {"messages": [{"role": "user", "content": question}]},
        config=config,
        stream_mode="values",
    )

    while True:
        try:
            for step in active_stream:
                if "__interrupt__" in step:
                    print("\n" + "=" * 50)
                    print("INTERRUPTED: APPROVAL REQUIRED")
                    interrupt = step["__interrupt__"][0]

                    # Propose tool calls
                    for request in interrupt.value["action_requests"]:
                        tool = request.get("action") or request.get("tool") or "unknown"
                        args = request.get("args") or {}

                        print(f"Tool: {tool}")
                        print(f"Args: {args}")

                    # Choice
                    choice = (
                        input("\nDo you approve this action? (y/n): ").strip().lower()
                    )

                    if choice == "y":
                        # Command tells the graph to resume with the approval
                        active_stream = agent.stream(
                            Command(resume={"decisions": [{"type": "approve"}]}),
                            config=config,
                            stream_mode="values",
                        )
                        break
                    else:
                        print("Execution denied by user.")
                        return

                elif "messages" in step:
                    step["messages"][-1].pretty_print()

            else:
                break

        except StopIteration:
            break
