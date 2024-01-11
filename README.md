# Generative AI Labs

This repository contains code samples for **Generative AI**, including different use cases. 
Some examples can be executed in Colab, while others would require Vertex AI.
Setup and authentication instructions of Vertex SDK are available [here](https://cloud.google.com/vertex-ai/docs/start/client-libraries). Make sure you install [latest version of the Vertex SDK](https://pypi.org/project/google-cloud-aiplatform/): `pip install google-cloud-aiplatform --upgrade`. Other dependencies may be required. Please, complete those steps before trying any of the labs below.


## 01 Prompting

* Lab1: Chain-of-Thought
* Lab2: External tools (RAG)
* Lab3: ReAct
* Lab4: ReAct with LangChain 0.1.0 agents
* LangChain specific labs. [LangChain](https://python.langchain.com/docs/get_started/introduction.html) is an open-source tool that can orchestrate or integrate APIs (databases, documents, apps, ...) with LLMs. LangChain is **not** a tool for tuning models.
* Ask Database labs: Ask BigQuery and [other databases](https://cloud.google.com/blog/products/data-analytics/building-ai-powered-apps-on-google-cloud-databases-using-pgvector-llms-and-langchain) in natural language.

<img src="images/ask-bigquery-gradio.png" alt="ask-bigquery Gradio demo" width="300"/>

Notes:
* [SQLAlchemy](https://www.sqlalchemy.org/) does not work  with `bigquery-public-data` datasets due to permissions, use a custom dataset instead.
* Make sure your query is not empty, otherwise you will get unexpected non-workable behaviour. You need to fill the input prompt.

```sh
pip install langchain==0.0.191 --quiet
pip install google-cloud-core --quiet
pip install gradio --quiet

# Below libraries are required to build a SQL engine for BigQuery and other DBs
pip install SQLAlchemy --quiet
pip install sqlalchemy-bigquery --quiet
pip install clickhouse-sqlalchemy --quiet
```


## 02 Tuning

PENDING


## 03 AI infra

PENDING


## 04 Multimodality

PENDING


## References

`[1]` SDK documentation: [Generative AI client libraries - Vertex AI](https://cloud.google.com/vertex-ai/docs/start/client-libraries)

`[2]` Github repo: [Q&A on unstructured documents with Vertex AI LLM and Document AI OCR](https://github.com/rafaelsf80/genai-vertex-documents-synchronous)

`[3]` Medium post: [Generative AI — Q&A with semantic answering on large scanned documents with Vertex AI, Chroma, LangChain and Document AI OCR](https://medium.com/google-cloud/generative-ai-q-a-with-semantic-answering-on-large-scanned-documents-with-vertex-ai-chroma-7f4806a3cb71) 

`[4]` Google Cloud blog post: [Building AI-powered apps on Google Cloud databases using pgvector, LLMs and LangChain](https://cloud.google.com/blog/products/data-analytics/building-ai-powered-apps-on-google-cloud-databases-using-pgvector-llms-and-langchain)

`[4]` Towards Data Science article: [LangChain: Develop applications powered by Language Models](https://towardsdatascience.com/develop-applications-powered-by-language-models-with-langchain-d2f7a1d1ad1a)     
