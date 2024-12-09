# NEWS ANALYSIS

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
  

---

## Features
- **Live News Scraping**: Automatically collects news articles from predefined news websites.
- **Categorization**: Uses a pre-trained machine learning model for accurate topic categorization of articles.
- **Sentiment Analysis**: Analyzes the sentiment of scraped news pages.
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

```

### 3. Build and Run the Project
To build and start the application, use the following command:
```bash
docker-compose up --build
```

### 4. Shut Down the Application
To stop the application and clean up the running containers, use the following command:
```bash
docker-compose down
```

## Endpoints

### Backend Endpoints (Running on `localhost:5000`)

#### 1. `GET /scrape_and_categorize`
- **Description**: Scrapes live news sites, categorizes the articles into topics, and saves the results to a CSV file.
- **Output**:
  - Saves the scraped data as a file named `my_scraped_articles.csv` in the `/app` directory.
  - Returns:
    - The number of articles scraped.
    - A list of unique categories identified in the scraped data.

#### 2. `GET /senti`
- **Description**: Performs sentiment analysis on the scraped articles.
- **Output**:
  - Provides:
    - Sentiment scores (positive, negative, or neutral) for each article.

---

### Frontend Access (Running on `localhost:8080`)
- **Interface**: Displays the scraped articles, their categories, and sentiment scores in a user-friendly format.
- **How to Access**: Open your browser and navigate to:  
  ```text
  http://localhost:8080

## Local Development

To run the application locally, the components are configured as follows:

- **Backend**: Accessible at `http://localhost:5000`.
- **Frontend**: Accessible at `http://localhost:8080`.

### Testing and Interaction
- Use tools like **Postman** or similar API clients to test the backend endpoints:
  - `GET /scrape_and_categorize` for scraping and categorizing news articles.
  - `GET /senti` for sentiment analysis and summarization.
- Use the provided frontend interface by navigating to `http://localhost:8080` in your browser for visualization and interaction.

### Development Workflow
1. Modify the backend code located in the `backend/` directory to add features or fix bugs.
2. Update the frontend code in the `frontend/` directory to improve the user interface or functionality.
3. Rebuild and restart the application using Docker:
   ```bash
   docker-compose up --build


