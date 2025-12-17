## AI Data Agent (Business Intelligence & Analysis)

An intelligent data assistant powered by **LangChain**, **Groq (Llama 3.1)**, and **Streamlit**. This agent allows users to interact with CSV data using natural language, perform complex analysis, and get business insights instantly.

## Key Features

- **Natural Language Data Querying**: Ask questions about your CSV files without writing a single line of Python code.
- **Dynamic Visualizations**: Automatically generates charts and plots (bars, lines, etc.) based on your requests.
- **Business Intelligence Tools**: Built-in tools to explain financial terms (ROI, LTV, etc.) and fetch real-time dates.
- **Interactive Chat Interface**: A seamless Streamlit-based chat history that tracks your conversation and data insights.

## Quick Start

### 1. Prerequisites

Make sure you have a **Groq API Key**. You can get one at [console.groq.com](https://console.groq.com/).

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/vibabi/agent
cd ai-data-agent

# Install dependencies
pip install -r requirements.txt

```

## 3. Run the App

```bash
streamlit run app.py
```

## 4. Usage Example

The Setup: Upload a file (sales_data.csv).

User Query: > "What was the total revenue today? Also, explain what ROI means and show me a bar chart of sales by product category."

You can ask to plot charts

## 5. The Agent's Workflow:

Context Awareness: Calls get_current_time to identify the current date.

Data Processing: Filters the Pandas DataFrame to calculate revenue for that date.

Knowledge Retrieval: Calls explain_business_term("ROI") to provide a business definition.

Visualization: Generates Matplotlib code to render the requested bar chart.

Response: Delivers a combined text and visual answer directly in the chat.

## 6. Tech Stack

LLM: Llama-3.1-8b-instant (via Groq)

Orchestration: LangChain & LangChain Experimental

Frontend: Streamlit

Data Stack: Pandas, Matplotlib
