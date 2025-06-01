import os
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from langchain_core.prompts import PromptTemplate
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import warnings
import streamlit as st


load_dotenv()
warnings.filterwarnings('ignore')
try: 
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    model = ChatGroq(temperature=0, model_name="llama3-8b-8192", groq_api_key=GROQ_API_KEY)
except Exception as e:
    print(e)

# Connect to SQLite Database
#sqllite_db_path = "data/street_db.sqlite"    
#db = SQLDatabase.from_uri(f"sqlite:///{sqllite_db_path}")


# MySQL connection URI format:
# mysql+pymysql://<user>:<password>@<host>:<port>/<database>
try: 
    db = SQLDatabase.from_uri(
        "mysql+pymysql://root:@localhost/x",
        include_tables=['employees'])
except Exception as e:
    print(e)

write_query = create_sql_query_chain(model, db)   
execute_query = QuerySQLDatabaseTool(db=db)
answer_prompt = PromptTemplate.from_template('''
    Given the following user question, corresponding SQL query, and SQL result,
    generate a concise answer.
    
    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    
    Answer:
''')
try: 
    def extract_sql_query(llm_response):
        split_token = "SQLQuery:"
        if split_token in llm_response:
            sql_part = llm_response.split(split_token, 1)[1].strip()
            
            for stop_token in ["Question:", "Answer:", "\n\n"]:
                if stop_token in sql_part:
                    sql_part = sql_part.split(stop_token)[0].strip()
            return sql_part
        return llm_response  
except Exception as e:
    print(e)

try: 
    chain = (
        RunnablePassthrough.assign(
            query=lambda x: write_query.invoke({"question": x["question"]}),
            result=lambda x: execute_query.invoke({"query": extract_sql_query(x["query"])}),
            answer=lambda x: answer_prompt.format(
                question=x["question"],
                query=x["query"],
                result=x["result"]
            )
        )
        | {"response": model | StrOutputParser()}
    )
except Exception as e:
    print(e)
    
try:
        
    def query_database(question: str) -> str:
        try:
        
            llm_output = write_query.invoke({"question": question})
            
        
            sql_query = extract_sql_query(llm_output)
            
        
            sql_result = execute_query.invoke({"query": sql_query})
            
    
            final_answer = answer_prompt.format(
                question=question,
                query=sql_query,
                result=sql_result
            )
            
            response = model.invoke(final_answer)
            
            return response.content
        except Exception as e:
            return f"An error occurred: {str(e)}"
except Exception as e:
    print(e)


st.header('SQL QnA App')
question = st.text_input('Enter your question')

result = query_database(question)

button = st.button('Press to see answer')
if button:

    st.write(result)