import requests 
import re
import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class DrupalPublishToolInput(BaseModel):
    """
    Input schema for "DrupalPublishTool".
    """
    argument: dict = Field(...,description="Dictionary containing 'title' and 'body' for the new blog post."
    )

class DrupalPublishTool(BaseTool):
    """
    DrupalPublishTool to publish content to druapl
    Expects 'title' and 'body' as input arguments.
    """
    name: str = "DrupalPublishTool"
    description: str = (
        "Publishes an blog post to a Drupal. "
        "Input requires 'title' and 'body' for the new blog post."
    )

    # Link the tool arguments to your Pydantic model:
    args_schema: Type[BaseModel] = DrupalPublishToolInput

    def _run(self, argument: dict) -> str:
        """
        DrupalPublishTool to publish content to druapl

        :param title: The title of the blog post.
        :param body: The content/body of the blog post.
        :return: Status message (success or error details).
        """
        # Extract values from the dictionary
        title = argument.get("title", "")
        body = argument.get("body", "")

        # Prepare the JSON:API payload
        payload = {
            "data": {
                "type": "node--page",  # or your actual content type
                "attributes": {
                    "title": title,
                    "body": {
                        "value": body,
                        "format": "full_html"  # or "basic_html" if needed
                    }
                }
            }
        }

        # Drupal JSON:API endpoint for creating new articles (replace with your actual path)
        drupal_jsonapi_endpoint = os.environ.get('JSON_API_URL')

        # Adjust headers as needed (authentication tokens, etc.)
        headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": "Basic " + os.environ.get('AUTHORIZATION_BASIC_KEY')
        }

        try:
            response = requests.post(drupal_jsonapi_endpoint, headers=headers, json=payload)

            if response.status_code == 201:
                data = response.json()
                node_id = data["data"]["id"]
                return f"Successfully created new article. Node ID: {node_id}"
            else:
                return (
                    f"Failed to create new article. "
                    f"Status code: {response.status_code}, response: {response.text}"
                )

        except requests.exceptions.RequestException as error:
            return f"Error occurred while publishing to Drupal: {str(error)}"
