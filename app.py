"""
Main Flask Server
"""
from flask_cors import CORS
from flask import Flask, request, render_template

from SPARQLLLM import SPARQLLLM
from SPARQLEngine import SPARQLEngine

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query")
def query_page():
    return render_template("query.html")


@app.route("/text_query")
def text_query_page():
    return render_template("text_query.html")


@app.route("/run_query", methods=["POST"])
def run_query():
    data = request.get_json()
    headers, results = sparql_engine.run_query(data["query"])
    return {"headers": headers, "results": results}


@app.route("/generate_query", methods=["POST"])
def generate_query():
    data = request.get_json()
    question = data["query"]

    query = sparql_llm.generate_query(question)
    headers, results = sparql_engine.run_query(query)
    return {"query": query, "headers": headers, "results": results}


if __name__ == "__main__":
    sparql_engine = SPARQLEngine("./food.xml")
    sparql_llm = SPARQLLLM("./prompt.txt")
    app.run(host="0.0.0.0", port=80, debug=True)
