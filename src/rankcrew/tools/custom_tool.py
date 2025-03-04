from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


class AlreadyExistInput(BaseModel):
    """Input schema for AlreadyExistInput."""
    argument: str = Field(..., description="the dictionnary of all the ideas.")

class AlreadyExist(BaseTool):
    name: str = "Already exists"
    description: str = (
        "This tool will check if the dictionnary ideas passsed as argument already exist or not, and will remove from the dictionnary the idea that already exist."
    )
    args_schema: Type[BaseModel] = AlreadyExistInput

    def _run(self, argument: str) -> str:
        eq = Request('https://www.apolline.art/sitemap.xml', headers={'User-Agent': 'Mozilla/5.0'})
        html_page = urlopen(req).read()
        
        soup = BeautifulSoup(html_page, 'html.parser')
        links = [loc.text for loc in soup.find_all('loc')]

        print(links)
        return links
