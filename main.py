from config import get_google_api_key, MODEL_NAME, TOP_K_RESULTS, THREAD_ID
from database import init_db, print_db_info
from prompts import get_system_prompt
from agents_setup import init_model, create_sql_agent, run_agent

# Ensure API key is set
get_google_api_key()

# Initialize model
model = init_model(MODEL_NAME)

# Initialize database and toolkit
db, toolkit = init_db(model)
toolkit.llm = model
print_db_info(db)

# Tools
tools = toolkit.get_tools()
for tool in tools:
    print(f"{tool.name}: {tool.description}\n")

# System prompt
system_prompt = get_system_prompt(dialect=db.dialect, top_k=TOP_K_RESULTS)

# Create agent
agent = create_sql_agent(model, tools, system_prompt)

# Question
question = "Which city has the most users?"
run_agent(agent, question, thread_id=THREAD_ID)
