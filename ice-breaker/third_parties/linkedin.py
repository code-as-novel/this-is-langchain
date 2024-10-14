import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
  """scrap information from LinkedIn profiles,
  Manually scrape the information from the LinkedIn profile"""

  if mock:
    linkedin_profile_url = "https://gist.githubusercontent.com/code-as-novel/09b909677c778e586ee6ebab426cd933/raw/58bfb724038f5a9be6500c3ac8af813d33fdd941/soo.json"
    response = requests.get(
      linkedin_profile_url,
      timeout = 10,
    )
  else:
    api_endpoint = "https://nubela.com/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}"}
    response = requests.get(
      api_endpoint,
      params = {"url": linkedin_profile_url},
      headers = header_dic,
      timeout = 10,
    )

  data = response.json()
  data = {
    k: v
    for k, v in data.items()
    if v not in ([], "", "", None)
    and k not in ["people_also_viewed", "certifications", "profile_pic_url"]
  }
  if data.get("groups"):
    for group_dict in data.get("groups"):
      group_dict.pop("profile_pic_url")

  return data


if __name__ == "__main__":
  print(
    scrape_linkedin_profile(
      linkedin_profile_url = "https://www.linkedin.com/in/sangsoo-kim-16515bba/", mock = True
    )
  )
