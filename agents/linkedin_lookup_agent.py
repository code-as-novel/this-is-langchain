import sys
import os

# 프로젝트의 루트 디렉토리를 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    # llm = ChatOpenAI(
    #     temperature=0,
    #     model_name="gpt-4o-mini"
    # )

    llm = ChatOllama(model="llama3.2")
    
    template = """given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
                    Your answer should contain only a URL"""
                    
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin Page URL"  # 아주 중요. 명확해야 함. 명확해야 LLM에서 이것을 사용할지를 판단함
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react") # 유명한 react prompt
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)  # Agent
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True) # Orchestrator
    
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    
    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == '__main__':
    linkedin_url = lookup("Eden Marco")
    print(linkedin_url)
