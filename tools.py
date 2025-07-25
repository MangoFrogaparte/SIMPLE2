from langchain_community import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_text(data: str, filename: str = "answer.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- SIMPLE's ANSWER ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Successfully saved to {filename}"
    
save_tool = Tool(
    name="search",
    func=save_to_text
    description="Search the web for information"
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="save_text_to_file",
    func=save_to_text,
    description="Saves structured research data to a text file.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)