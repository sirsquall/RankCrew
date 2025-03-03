from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
import requests

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "already_exist"
    description: str = (
        "Retrieve all the blog post that already exist, to avoir create duplicate blog post."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        r = requests.get("https://www.apolline.art/sitemap.xml")
        xml = r.text
        
        soup = BeautifulSoup(xml, "lxml")
        sitemap_tags = soup.find_all("sitemap")
        for sitemap in sitemap_tags:
            xml_dict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

        return xml_dict

