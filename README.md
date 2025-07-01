# ISRO-2

## 🧠 Problem Statement 2: AI Help Bot for Knowledge Retrieval from Web Portal

---

## 📌 1. Project Overview

**MOSDACQueryBot** is a lightweight **AI-driven help assistant** designed to simplify information retrieval from the [MOSDAC Portal](https://www.mosdac.gov.in). The platform hosts a variety of satellite datasets, FAQs, and documentation. Navigating through its layered and scattered content is time-consuming for users.

Our solution uses **Natural Language Processing (NLP)** and **knowledge graph-based reasoning** to intelligently fetch answers from structured and unstructured web content — documents, FAQs, and web pages — with an easy-to-use chatbot interface.

Using **LangChain**, **spaCy**, **OpenAI Embeddings**, and optionally **LLMs**, this project enables contextual, fast, and accurate query answering in a short time.

---

## 🌟 2. Project Objectives

* 🤖 Build an AI-based **virtual assistant** that answers user queries from the MOSDAC portal.
* 🧱 Convert static/dynamic content into a **knowledge graph** (entities and relationships).
* 🧠 Use NLP for **intent classification**, **entity extraction**, and **semantic retrieval**.
* 🗣️ Enable a **conversational interface** that understands context and follows multi-turn dialogs.
* 🔄 Ensure modularity for deployment across similar government portals.

---

## 📦 3. Dataset Overview

| Content Type     | Source                                     | Description                                     |
| ---------------- | ------------------------------------------ | ----------------------------------------------- |
| 📄 Web Pages     | [MOSDAC.gov.in](https://www.mosdac.gov.in) | FAQ, documentation, static content              |
| 📁 Documents     | Download sections                          | PDFs, XLSX, DOCs with technical info            |
| 🧾 Metadata      | HTML + ARIA tags                           | Categories, tags, page sections, menu structure |
| 🌐 Product Pages | Dynamic navigation                         | Real-time product data and mission info         |

📁 **Formats**: HTML, PDF, DOCX, XLSX
🧹 **Preprocessing**: Content scraping, text extraction (using `BeautifulSoup`, `pdfminer`, `docx`, `tabula-py`)

---

## 🛠️ 4. Tools and Technologies

| Tool / Library         | Purpose                                          |
| ---------------------- | ------------------------------------------------ |
| 🐍 Python              | Core development                                 |
| 🧠 spaCy / NLTK        | NLP and entity extraction                        |
| 🧩 LangChain           | Knowledge graph creation + query chain           |
| 📚 OpenAI Embeddings   | Semantic similarity for retrieval                |
| 🔗 NetworkX / Neo4j    | Graph database or in-memory graph representation |
| 💬 Streamlit / Gradio  | Chatbot front-end UI                             |
| 🕸️ BeautifulSoup      | HTML parsing and web scraping                    |
| 📜 pdfminer / docx2txt | PDF and Word document parsing                    |

---

## 🔧 5. Methodology (Simplified Workflow)

```plaintext
       +-----------------------------+
       |    Static + Dynamic Data    |
       |  (HTML, PDF, XLSX, DOCX)    |
       +-----------------------------+
                    |
         +------------------------+
         | Text Extraction Engine |
         +------------------------+
                    |
     +-------------------------------+
     |   Entity & Relationship NLP   |
     +-------------------------------+
                    |
     +-------------------------------+
     |  Knowledge Graph Construction |
     +-------------------------------+
                    |
     +-------------------------------+
     | User Query (via Chatbot UI)  |
     +-------------------------------+
                    |
     +-----------------------------+
     | Semantic Search + Answering |
     +-----------------------------+
                    |
     +-----------------------------+
     |  Final Response (Text/Card) |
     +-----------------------------+
```

---

## 👥 6. Team Task Distribution (Parallel Modules)

### 👩‍💻 Member 1 – Web Scraping & Document Parsing

* Scrape static pages using `requests` + `BeautifulSoup`
* Extract content from PDFs using `pdfminer.six` / `PyMuPDF`
* Parse `.docx`, `.xlsx` using `python-docx`, `openpyxl`
* Preprocess and clean text

📤 Output: `.txt` files + metadata JSON

---

### 👨‍💻 Member 2 – NLP Entity Extraction & Graph Building

* Use **spaCy/NLTK** to identify:

  * Entities (e.g., satellites, products)
  * Relationships (e.g., "belongs to", "used in")
* Build graph using `NetworkX` or `Neo4j`
* Export in `.graphml` or `.json`

📤 Output: Knowledge Graph + embeddings (optional)

---

### 👩‍💻 Member 3 – Chatbot & Retrieval Engine

* Build retrieval chain using **LangChain + OpenAI Embeddings**
* Support context-aware question answering
* Design prompt templates for fallback answers
* Integrate semantic search with knowledge graph

📤 Output: Query → Semantic → Matched Answer

---

### 👨‍💻 Member 4 – Frontend UI + Integration

* Build Streamlit or Gradio chatbot interface
* Integrate backend APIs for question response
* Enable upload of custom files (for testing)
* Add session memory & conversation history

📤 Output: Web-based interactive chatbot UI

---

## 🧪 7. Novelty Statement

Our approach is **simple yet modular** because:

* 🧠 Combines **structured KG reasoning** with **semantic retrieval**
* 🔄 Allows **live interaction** on government data (not static documents alone)
* 🧱 Converts heterogeneous content into a unified knowledge system
* 📦 Packaged for **reuse across other public data portals**

---

## 🗂️ 8. GitHub Folder Structure

```plaintext
mosdac-querybot/
├── data/
│   ├── html_pages/           # Scraped content
│   ├── docs_parsed/          # Parsed PDF/DOCX/XLSX
│   └── kg_data/              # JSON or GraphML files
├── src/
│   ├── extractor/            # Web/document text parsing
│   ├── nlp_graph/            # spaCy-based entity/graph model
│   ├── chatbot_backend/      # LangChain + vector search
│   └── ui_streamlit/         # Frontend chatbot interface
├── notebooks/                # Debug, analysis notebooks
├── results/                  # Logs, screenshots, sample runs
├── requirements.txt
└── README.md
```

---

## 📈 9. Evaluation Metrics

| Component              | Metric                                     |
| ---------------------- | ------------------------------------------ |
| 🔍 Intent Recognition  | Classification Accuracy (%)                |
| 🧠 Entity Extraction   | Precision / Recall of key entity matches   |
| 🔁 Context Consistency | Score of multi-turn dialog retention       |
| 💬 Response Accuracy   | User rating or BLEU-style similarity score |
| ⏱️ Latency & Speed     | Response time (ms) under load              |

---

## 📚 10. References

* [MOSDAC Official Portal](https://www.mosdac.gov.in)
* [LangChain Documentation](https://docs.langchain.com/)
* [spaCy NLP Toolkit](https://spacy.io/)
* [pdfminer for Python](https://github.com/pdfminer/pdfminer.six)
* [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
* [Streamlit](https://streamlit.io/), [Gradio](https://gradio.app/)

