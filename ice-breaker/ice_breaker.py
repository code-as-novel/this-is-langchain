import os
from typing import Tuple

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from output_parsers import Summary, summary_parser
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile

# from third_parties.linkedin import scrape_linkedin_profile

def ice_break_with(name: str) -> Tuple[Summary, str]:
    # linkedin_profile_url = lookup(name=name)  # API 호출하게 됨
    linkedin_profile_url = "https://www.linkedin.com/in/sangsoo-kim-16515bba/"
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, mock=True)
    
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them

        Use information from LinkedIn
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions}
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt4o-mini")
    llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm | summary_parser
    res:Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("profile_image_url")

if __name__ == '__main__':
    load_dotenv()

    print("Hello, Langchain!")

    ice_break_with("Sangsoo Kim LG CNS")