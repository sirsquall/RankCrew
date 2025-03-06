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
    Expects a dictionary with at least the keys: 'title' and 'body'.
    """
    argument: dict = Field(
        ...,
        description="Dictionary containing 'title' and 'body' for the new blog post."
    )

class DrupalPublishTool(BaseTool):
    """
    Publishes a blog post to Drupal via JSON:API.
    Accepts a single 'argument' dict containing 'title' and 'body'.
    """
    name: str = "DrupalPublishTool"
    description: str = (
        "Publishes a blog post to a Drupal site. "
        "Input requires a dictionary with 'title' and 'body'."
    )
    args_schema: Type[BaseModel] = DrupalPublishToolInput

    def _run(self, argument: dict) -> str:
        """
        Publishes the blog post to Drupal via JSON:API.

        :param argument: Dictionary with keys 'title' and 'body'.
        :return: Status message (success or error details).
        """
        # Extract values from the dictionary
        title = argument.get("title", "")
        body = argument.get("body", "")

        # Optional: Check if title or body is empty
        if not title.strip():
            return "Error: 'title' is missing or empty."
        if not body.strip():
            return "Error: 'body' is missing or empty."

        # Prepare the JSON:API payload
        payload = {
            "data": {
                "type": "node--page",  # Replace with your Drupal content type if different
                "attributes": {
                    "title": title,
                    "body": {
                        "value": body,       # HTML or text is fine here
                        "format": "full_html"
                    }
                }
            }
        }

        # Retrieve environment variables for URL and authorization
        drupal_jsonapi_endpoint = os.environ.get("JSON_API_URL")
        if not drupal_jsonapi_endpoint:
            return "Error: JSON_API_URL environment variable is not set."

        auth_key = os.environ.get("AUTHORIZATION_BASIC_KEY")
        if not auth_key:
            return "Error: AUTHORIZATION_BASIC_KEY environment variable is not set."

        headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"Basic {auth_key}"
        }

        try:
            # requests handles any necessary JSON escaping automatically:
            response = requests.post(
                drupal_jsonapi_endpoint,
                headers=headers,
                json=payload
            )

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
