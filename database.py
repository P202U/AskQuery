from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from config import DB_URI


def init_db(llm):
    db = SQLDatabase.from_uri(DB_URI)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return db, toolkit


def print_db_info(db):
    print(f"Dialect: {db.dialect}")
    print(f"Available tables: {db.get_usable_table_names()}")
