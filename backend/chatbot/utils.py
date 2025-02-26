import os
import time
import logging
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Import custom modules
from chatbot.helpers.build_query import build_query
from chatbot.helpers.get_llm_model import get_llm_model
from chatbot.tools.checkTime import get_system_time
from chatbot.tools.get_plant_data import get_plant_data
from chatbot.tools.weather import get_weather



# Load environment variables
load_dotenv()


def setup_logging():
    """Configures logging settings."""
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'query_log.log')
    logging.basicConfig(
        filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s'
    )


def process_query(user_query: str) -> str:
    """Processes the user query using an AI agent and vector database."""
    setup_logging()
    start_time = time.time()

    # Initialize embeddings and vector database
    # vector_db = get_vector_db()

    # Initialize AI model and tools
    llm = get_llm_model()
    tools = [get_system_time, get_weather, get_plant_data]
    agent_prompt_template = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, agent_prompt_template)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Process query
    refined_query = build_query(user_query)
    # refined_query = retrieve_from_vector_db(refined_query, vector_db)
    result = agent_executor.invoke({"input": refined_query})

    execution_time = time.time() - start_time
    logging.info(
        f"Execution time: {execution_time} seconds\n"
        f"Query: {refined_query}\n"
        f"Output: {result['output']}\n"
    )

    return result['output']
