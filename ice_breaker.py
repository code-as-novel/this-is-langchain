import os

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# from third_parties.linkedin import scrape_linkedin_profile

information = """
Steven Paul Jobs (February 24, 1955 – October 5, 2011) was an American businessman, inventor, and investor best known for co-founding the technology company Apple Inc. Jobs was also the founder of NeXT and chairman and majority shareholder of Pixar. He was a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak.

Jobs was born in San Francisco in 1955 and adopted shortly afterwards. He attended Reed College in 1972 before withdrawing that same year. In 1974, he traveled through India, seeking enlightenment before later studying Zen Buddhism. He and Wozniak co-founded Apple in 1976 to further develop and sell Wozniak's Apple I personal computer. Together, the duo gained fame and wealth a year later with production and sale of the Apple II, one of the first highly successful mass-produced microcomputers.

Jobs saw the commercial potential of the Xerox Alto in 1979, which was mouse-driven and had a graphical user interface (GUI). This led to the development of the unsuccessful Apple Lisa in 1983, followed by the breakthrough Macintosh in 1984, the first mass-produced computer with a GUI. The Macintosh launched the desktop publishing industry in 1985 (for example, the Aldus Pagemaker) with the addition of the Apple LaserWriter, the first laser printer to feature vector graphics and PostScript.

In 1985, Jobs departed Apple after a long power struggle with the company's board and its then-CEO, John Sculley. That same year, Jobs took some Apple employees with him to found NeXT, a computer platform development company that specialized in computers for higher-education and business markets, serving as its CEO. In 1986, he helped develop the visual effects industry by funding the computer graphics division of Lucasfilm that eventually spun off independently as Pixar, which produced the first 3D computer-animated feature film Toy Story (1995) and became a leading animation studio, producing 28 films since.

In 1997, Jobs returned to Apple as CEO after the company's acquisition of NeXT. He was largely responsible for reviving Apple, which was on the verge of bankruptcy. He worked closely with British designer Jony Ive to develop a line of products and services that had larger cultural ramifications, beginning with the "Think different" advertising campaign, and leading to the iMac, iTunes, Mac OS X, Apple Store, iPod, iTunes Store, iPhone, App Store, and iPad. Jobs was also a board member at Gap Inc. from 1999 to 2002.[3] In 2003, Jobs was diagnosed with a pancreatic neuroendocrine tumor. He died of tumor-related respiratory arrest in 2011; in 2022, he was posthumously awarded the Presidential Medal of Freedom. Since his death, he has won 141 patents; Jobs holds over 450 patents in total.[4]
"""

if __name__ == '__main__':
    load_dotenv()

    print("Hello, Langchain!")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="mistral")
    llm = ChatOllama(model="llama3.2")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True)
    # res = chain.invoke(input={"information": linkedin_data})

    print(res)