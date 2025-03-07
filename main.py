from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from langchain.llms import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
from langchain.agents import AgentType, initialize_agent, Tool
import uvicorn
import os
from typing import List, Optional

app = FastAPI(title = "Gemini-Powered Research Assistant")

class Config:
    API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL: str = "gemini-1.5-pro"
config = Config()

if not config.API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")
    
genai.configure(api_key = config.API_KEY)

llm = GoogleGenerativeAI(model = config.GEMINI_MODEL, google_api_key = config.API_KEY)

class SearchTool(BaseTool):
    name = "web_search"
    description = "Useful for searching the web for information"
    
    def _run(self, query: str) -> str:
        search_prompt = PromptTemplate(
            input_variables = ["query"],
            template="You are a search engine. Please provide relevant information for: {query}"
        )
        search_chain = LLMChain(llm = llm, prompt = search_prompt)
        return search_chain.run(query)
    
    def _arun(self, query: str):
        raise NotImplementedError("Async not implemented")

search_tool = SearchTool()
summarize_prompt = PromptTemplate(
    input_variables = ["text"],
    template="Please summarize the following text concisely: {text}"
)
summarize_chain = LLMChain(llm = llm, prompt = summarize_prompt)

tools = [
    Tool(
        name = "Search",
        func = search_tool._run,
        description = "Useful for searching information on the internet"
    ),
    Tool(
        name = "Summarize",
        func = lambda text: summarize_chain.run(text),
        description = "Useful for summarizing long texts"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)
class QueryRequest(BaseModel):
    query: str
class QueryResponse(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"message": "Gemini-Powered Research Assistant API"}

@app.post("/research", response_model = QueryResponse)
def research(request: QueryRequest):
    try:
        result = agent.run(request.query)
        return QueryResponse(answer = result)
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
