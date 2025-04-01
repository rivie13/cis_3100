# News Summarizer Agent

This is an LLM-based agent that summarizes news on specific topics. It uses LangChain, Google's Gemini models, and Tavily Search to find and summarize relevant news articles.

## Setup

1. Make sure you have Python 3.8+ installed

  a. Go to virtual environment

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```
   
   - Get a Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Get a Tavily API key from [Tavily's website](https://tavily.com)

## Usage

Run the script:
```
python news_summarizer_agent.py
```

When prompted, enter a news topic you want to summarize. For example:
- "tariff increases for Canada"
- "climate change legislation in the EU"
- "recent developments in AI regulation"

The agent will search for relevant news articles, analyze them, and provide a concise summary.

## Example

Input:
```
Enter a news topic to summarize: tariff increases for Canada
```

Output:
```
Summary:
[A concise summary of recent news about tariff increases for Canada will appear here]
```

## How It Works

1. The agent takes your query and formulates appropriate search terms
2. It searches the web using Tavily Search API to find recent and relevant news articles
3. It processes the search results and generates a comprehensive summary using Google's Gemini model
4. The summary focuses on key facts, dates, figures, and presents multiple perspectives when relevant
