from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

# Load environment variables from .env file
load_dotenv()

class NewsAgent:
    def __init__(self):
        # Initialize the Google Gemini model
        self.model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Set up search tool
        self.search_tool = TavilySearchResults(max_results=3)
        
        # Create tools list
        self.tools = [
            Tool(
                name="Search",
                func=self.search_tool.invoke,
                description="Useful for searching the web for recent news and information"
            )
        ]
        
        # Custom prompt template for news summarization
        prompt_template = """You are an expert news researcher and summarizer. Your goal is to provide accurate, concise, and well-organized summaries of news on specific topics.

Given the request from the user, search for relevant information, then create a summary that:
1. Covers the main events and developments
2. Includes key facts, figures, and dates where relevant
3. Presents multiple perspectives if there are different viewpoints
4. Is organized in a clear, readable format
5. Is factual and objective
6. Focuses only on the most important and recent information

{tools}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: a concise, well-organized summary of the news on the topic

Question: {input}
{agent_scratchpad}"""

        # Create the prompt
        self.prompt = PromptTemplate.from_template(prompt_template)
        
        # Create the agent
        self.agent = create_react_agent(
            llm=self.model,
            tools=self.tools,
            prompt=self.prompt
        )
        
        # Create the agent executor
        self.agent_executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent, 
            tools=self.tools, 
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )

    def summarize(self, query):
        """
        Summarize news on a specific topic based on the query.
        
        Args:
            query (str): The news topic or question to summarize
            
        Returns:
            str: A concise summary of the news
        """
        result = self.agent_executor.invoke({"input": f"summarize the news about {query}"})
        return result["output"]


if __name__ == "__main__":
    # Check if API keys are set
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set. Please create a .env file with your API key.")
        print("You can get a free API key from https://ai.google.dev/")
        exit(1)
    
    if not os.getenv("TAVILY_API_KEY"):
        print("Error: TAVILY_API_KEY environment variable not set. Please create a .env file with your API key.")
        print("You can get a free API key from https://tavily.com")
        exit(1)
    
    # Create the news agent
    news_agent = NewsAgent()
    
    # Example usage
    topic = input("Enter a news topic to summarize: ")
    summary = news_agent.summarize(topic)
    print("\nSummary:")
    print(summary) 