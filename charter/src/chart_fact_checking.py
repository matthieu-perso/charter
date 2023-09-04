"""Assertion validation based on iterative agents"""

from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd


"""OVERVIEW

"""

def initialize_agent(df, model="gpt-3.5-turbo-0613", temperature=0, verbose=True):
    """
    Initialize the Langchain agent for querying the DataFrame.
    """

    print(df)

    agent = agent = create_pandas_dataframe_agent(
            ChatOpenAI(temperature=0, model_name="gpt-4"),
            df,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            max_iterations=2,
            early_stopping_method="generate"
        )
    return agent

def run_assertion(agent, assertion_query):
    """
    Run an assertion query against the DataFrame and return the result.
    """
    result = agent.run(f"Determine to what extent this assertion is supported by the data from the dataframe: {assertion_query}")
    return result

def fact_check(df, assertions):
    """
    Perform fact-checking on a list of assertions.
    """
    # Initialize the agent
    agent = initialize_agent(df)

    # Initialize report
    report = {}

    for assertion, query in assertions.items():
        # Run the assertion query
        result = run_assertion(agent, query)

        report[assertion] = result

    return report


