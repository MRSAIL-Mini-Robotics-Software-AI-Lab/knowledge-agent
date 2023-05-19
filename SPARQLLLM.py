"""
A LLM to generate sparql queries from natural language questions
"""
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

API_KEY = open(".env", "r", encoding="utf8").read().split("=")[1]
os.environ["OPENAI_API_KEY"] = API_KEY


class SPARQLLLM:
    """
    A LLM to generate sparql queries from natural language questions

    Parameters
    ----------
    prompt_path : str
        The path to the prompt file
    """

    def __init__(self, prompt_path: str):
        prompt_str = open(prompt_path, "rb").read()
        self.prompt = PromptTemplate(
            input_variables=["prompt"],
            template=prompt_str,
            template_format="jinja2",
        )
        self.llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    def generate_query(self, question: str) -> str:
        """
        Generate a sparql query from a natural language question

        Parameters
        ----------
        question : str
            The natural language question

        Returns
        -------
        str
            The sparql query
        """
        return self.llm(self.prompt.format(prompt=question)).replace("```", "")
