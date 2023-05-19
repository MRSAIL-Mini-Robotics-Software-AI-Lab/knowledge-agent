"""
Sparql Engine class to run the queries
"""
import re
from typing import List, Tuple
import owlready2 as owl


class SPARQLEngine:
    """
    Sparql Engine class to run the queries

    Parameters
    ----------
    file_path : str
        The path to the ontology file
    """

    def __init__(self, file_path: str):
        self.world = owl.World()
        self.onto = self.world.get_ontology(file_path).load()
        self.graph = self.world.as_rdflib_graph()

    def run_query(self, query: str) -> Tuple[List[str], List[List[str]]]:
        """
        Run a sparql query

        Parameters
        ----------
        query : str
            The sparql query

        Returns
        -------
        Tuple[List[str], List[List[str]]]
            The headers and results of the query
        """
        results = self.graph.query(query)
        headers = [str(header) for header in results.vars]

        parsed_results = []
        for row in results:
            to_add = []
            for element in row:
                if element is None:
                    parsed = "-"
                else:
                    parsed = element.n3().replace(">", "").replace("<", "")
                    parsed = re.sub("http:.*#", "", parsed)
                to_add.append(parsed)
            parsed_results.append(to_add)
        return headers, parsed_results
