from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver


def init_model(model_name: str):
    return ChatGoogleGenerativeAI(model=model_name)


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

    for step in agent.stream(
        {"messages": [{"role": "user", "content": question}]},
        config=config,
        stream_mode="values",
    ):
        if "__interrupt__" in step:
            print("INTERRUPTED:")
            interrupt = step["__interrupt__"][0]
            for request in interrupt.value["action_requests"]:
                print(request["description"])
        elif "messages" in step:
            step["messages"][-1].pretty_print()
        else:
            pass
