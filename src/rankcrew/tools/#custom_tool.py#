import os
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class DrupalPublishToolInput(BaseModel):
    """
    Input schema for 'DrupalPublishTool'.
    Expects a single dict 'argument' with two keys: 'title' and 'body'.
    """
    argument: dict = Field(
        ...,
        description="Dictionary containing the keys 'title' and 'body' for the blog post."
    )

class DrupalPublishTool(BaseTool):
    """
    Publishes a blog post to a Drupal site via JSON:API.
    Requires 'title' and 'body' at the top-level of 'argument'.
    """
    name: str = "DrupalPublishTool"
    description: str = (
        "Publishes a blog post to Drupal. "
        "Input requires a dict with 'title' and 'body' at the top level."
    )
    args_schema: Type[BaseModel] = DrupalPublishToolInput

    def _run(self, argument: dict) -> str:
        """
        Publishes the blog post to Drupal using JSON:API.

        :param argument: Dict with keys 'title' and 'body'.
        :return: Status message (success or error details).
        """
        # Extract fields directly from argument
        title = argument.get("title", "").strip()
        body = argument.get("body", "").strip()

        # Validate presence of title and body
        if not title:
            return "Error: 'title' is missing or empty."
        if not body:
            return "Error: 'body' is missing or empty."

        # Prepare the JSON:API payload
        payload = {
            "data": {
                "type": "node--page",  # or your Drupal content type
                "attributes": {
                    "title": title,
                    "body": {
                        "value": body,
                        "format": "full_html"
                    }
                }
            }
        }

        # Retrieve endpoint from environment
        drupal_jsonapi_endpoint = os.environ.get("JSON_API_URL")
        if not drupal_jsonapi_endpoint:
            return "Error: JSON_API_URL environment variable not set."

        # Retrieve authorization key
        auth_key = os.environ.get("AUTHORIZATION_BASIC_KEY")
        if not auth_key:
            return "Error: AUTHORIZATION_BASIC_KEY environment variable not set."

        headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"Basic {auth_key}"
        }

        try:
            response = requests.post(
                drupal_jsonapi_endpoint,
                headers=headers,
                json=payload
            )
            # 201 = created successfully
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
