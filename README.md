# 📄 Intelligent Document RAG Assistant

<p align="center">
  <strong>Ask Questions. Retrieve Knowledge. Get Context-Grounded Answers.</strong>
</p>

<p align="center">
  An AI-powered document question-answering system built using Retrieval-Augmented Generation (RAG).
</p>

---

## 🚀 Project Overview

Intelligent Document RAG Assistant enables users to interact with company leave-policy documents through natural language questions.

Instead of manually searching through lengthy PDF documents, users can simply ask questions and receive relevant, context-based answers.

The system combines semantic search with Google's Gemini API to retrieve relevant document information and generate grounded responses.

### ✨ Key Highlights

- 📑 **PDF Processing:** Extracts text from PDF documents.
- ✂️ **Text Chunking:** Divides extracted text into manageable chunks.
- 🧠 **Semantic Embeddings:** Converts text into numerical vector representations.
- 🔍 **Similarity Search:** Uses FAISS to retrieve relevant document chunks.
- 🤖 **AI-Powered Answers:** Uses Gemini to generate context-grounded responses.
- 🛡️ **Fallback Handling:** Handles questions when relevant information is unavailable.
- 📊 **Interactive Interface:** Provides a user-friendly Streamlit application.

---

**🎯 Goal:** To build a document-based AI assistant that makes information retrieval faster, easier, and more accessible.

## 🎯 Problem Statement

Organizations often maintain important information, such as employee leave policies, in PDF documents. Finding specific information manually can be time-consuming, especially when users need quick answers to particular questions.

Traditional document reading requires users to search through the content themselves.

This project addresses that challenge by providing an AI-powered interface where users can ask questions in natural language and retrieve relevant information directly from the document.

### 💡 Project Objectives

- Simplify information retrieval from PDF documents.
- Implement a Retrieval-Augmented Generation (RAG) pipeline.
- Generate semantic embeddings for document content.
- Store and search vector representations using FAISS.
- Retrieve relevant context before generating an answer.
- Use Gemini to generate context-grounded responses.
- Handle irrelevant questions and missing information gracefully.