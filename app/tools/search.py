from langchain_core.tools import tool
from langchain_tavily import TavilySearch


@tool
def search_web(query: str) -> str:
    """Search the web for current music marketing or industry trends."""
    print(f"Searching the web for: {query}")
    search = TavilySearch(max_results=3)
    result = search.invoke({"query": query})
    print(f"Result: {result}")
    snippets: list[str] = []
    for item in result.get("results", []):
        snippets.append(f"- {item['title']}: {item['content']}")

    return "\n".join(snippets) if snippets else "No results found."
