# Live News Scraper and Sentiment Analyzer

This project is a live news scraper and sentiment analysis tool. It scrapes news articles from popular live-news sites, categorizes them based on their content, and provides sentiment analysis for the scraped pages.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Machine Learning Models](#machine-learning-models)
  - [Categorization](#categorization)
  - [Sentiment Analysis](#sentiment-analysis)
- [Installation and Setup](#installation-and-setup)
  - [Start Docker Engine](#1-start-docker-engine)
  - [Clone the Repository](#2-clone-the-repository)
  - [Build and Run the Project](#3-build-and-run-the-project)
  - [Shut Down the Application](#4-shut-down-the-application)
- [Endpoints](#endpoints)
  - [Backend (localhost:5000)](#backend-running-on-localhost5000)
  - [Frontend (localhost:8080)](#frontend-running-on-localhost8080)
- [Local Development](#local-development)
- [License](#license)

---

## Features
- **Live News Scraping**: Automatically collects news articles from predefined news websites.
- **Categorization**: Uses a pre-trained machine learning model for accurate topic categorization of articles.
- **Sentiment Analysis**: Analyzes the sentiment of scraped news pages and summarizes them.
- **Frontend Integration**: User-friendly interface for viewing and interacting with results.
- **Easy Deployment**: Dockerized for seamless setup and deployment.

---

## Requirements
Ensure the following dependencies are installed before running the project:
- **Docker**: To containerize and run the application.

---

## Machine Learning Models

### Categorization
- Utilizes a pre-trained **cardiffnlp/twitter-roberta-base-topic-latest** model for topic categorization.
- This model is implemented using the transformers library.
- Categorizes articles into meaningful topics based on their textual content.

### Sentiment Analysis
- Employs a **RoBERTa-based** sentiment analysis model.
- Evaluates the sentiment of news articles as positive, negative, or neutral.

Both models are loaded in the backend for high accuracy and scalability.

---

## Installation and Setup

### 1. Start Docker Engine
Ensure your Docker Engine is running on your machine.

### 2. Clone the Repository
```bash
git clone <https://github.com/hanimalnad/news-analysis>
cd <LiveNews>
