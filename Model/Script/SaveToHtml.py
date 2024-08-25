import feedparser
from openai import OpenAI
import os

# Initialize OpenAI client with your API key
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-aiHCyzPrDBhhjuYQnEdipZvPvfWpgd0yfFRCzZ7083ONWHId",
    base_url="https://api.chatanywhere.tech/v1"
)

def fetch_rss_feed(url):
    """Fetch and parse RSS feed from the given URL."""
    feed = feedparser.parse(url)
    return feed.entries

def gpt_35_api(messages: list):
    """Generate a response for the provided conversation messages using OpenAI.

    Args:
        messages (list): The complete conversation messages.
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion['choices'][0]['message']['content']

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            summary += chunk['choices'][0]['delta']['content']
            print(chunk.choices[0].delta.content, end="")
        return summary


def summarize_entry(entry, use_stream=False):
    """Generate a summary for a given RSS feed entry using OpenAI."""
    # Create a prompt for the entry
    prompt = f"如何看待这个问题:\n\n标题: {entry.title}\n描述: {entry.description}"
    
    messages = [{"role": "user", "content": prompt}]
    
    if use_stream:
        summary=gpt_35_api_stream(messages)
    else:
        summary=gpt_35_api_stream(messages)
    print("\n" + "-" * 50)
    # Save the summary to an HTML file
    save_to_html(entry.title, entry.link, summary)

def save_to_html(title, link, summary):
    """Save the summary to an HTML file."""
    file_path = os.path.join("public", "rss_summary.html")
    with open("rss_summary.html", "a", encoding="utf-8") as f:
        f.write(f"<h2>{title}</h2>\n")
        f.write(f"<p><a href='{link}'>{link}</a></p>\n")
        f.write(f"<p>{summary}</p>\n")
        f.write("<hr>\n")

if __name__ == '__main__':
    # RSS feed URL
    os.makedirs("public", exist_ok=True)
    rss_feed_url = "https://rsshub.baitry.com/weibo/search/hot"
    
    # Fetch RSS feed entries
    entries = fetch_rss_feed(rss_feed_url)
    
    # Start the HTML file with basic headers
    file_path = os.path.join("public", "rss_summary.html")
    with open("rss_summary.html", "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>RSS Summary</title></head><body>\n")

    # Loop through each entry and generate a summary
    for entry in entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        
        # Set use_stream to True for streaming responses, False for non-streaming
        summarize_entry(entry, use_stream=False)
    
    # Close the HTML tags
    with open("rss_summary.html", "a", encoding="utf-8") as f:
        f.write("</body></html>")
