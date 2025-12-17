import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
from src.tools import get_current_time, explain_business_term # Імпорт тулів

def get_agent(df: pd.DataFrame, api_key: str):
    """
    Створює агента, який бачить Pandas DF і має додаткові інструменти.
    """
    
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        api_key=api_key,
        temperature=0
    )

    tools = [get_current_time, explain_business_term]


    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        agent_type="tool-calling", 
        extra_tools=tools,         
        verbose=True,
        allow_dangerous_code=True,
        handle_parsing_errors=True 
    )
    
    return agent