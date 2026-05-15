### Yup, I'm that bad at this. And AI doesn't help

```
# SQL AI Agent

A Python project that uses **LangChain**, **Google Gemini AI**, and **SQLite** to build an intelligent agent capable of querying a SQL database in natural language.

The agent is interactive and can approve queries before execution, making it safe to explore your data.

## Features

- Natural language querying of a SQL database.
- Uses **Google Gemini 1.5** model for reasoning and query generation.
- Human-in-the-loop approval for all database queries.
- Supports multiple database tables with schema introspection.
- Fast local testing with **Uvicorn**.
- Easily extendable to other SQL databases or AI models.

## Project Structure
```

```
my_sql_agent/
│
├── main.py # Entry point to run the agent
├── config.py # Configuration and environment setup
├── database.py # Database connection & toolkit setup
├── agent_setup.py # Agent creation, middleware, and execution logic
├── prompts.py # System prompt templates
└── README.md

```

## Requirements

- Python 3.11+
- [uv](https://uv.pypa.io/) (or pip/poetry)
- [LangChain](https://www.langchain.com/)
- [Google Generative AI API Key](https://developers.generativeai.google/)

## Installation

```bash
git clone https://github.com/yourusername/sql-ai-agent.git
cd sql-ai-agent

uv install
```

## Setup

1. Set your **Google API key**:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

or let the program prompt you on first run.

2. Configure database URI in `config.py` if using a database other than `Chinook.db`.

## Usage

### Run locally

```bash
uv run main.py
```

This will:

1. Initialize the AI model.
2. Connect to the database.
3. Display available tables and tools.
4. Allow you to ask questions in natural language (example included: _“Which genre on average has the longest tracks?”_).
5. Ask for approval before executing SQL queries.

### Example

```text
> Which genre on average has the longest tracks?
INTERRUPTED:
Tool execution pending approval: SQL query generated
Result:
Genre: Jazz
Average Track Length: 6:12
```

## Notes

- **Never executes DML statements**: INSERT, UPDATE, DELETE, DROP are blocked.
- **Schema-aware**: The agent inspects tables before querying.
- **Top-k results**: By default, queries are limited to the top 5 most relevant results.
- Safe for experimentation with sensitive databases.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

## License

## MIT License © 2026
