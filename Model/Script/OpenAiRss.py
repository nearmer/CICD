import feedparser
from openai import OpenAI

# Initialize OpenAI client with your API keyopenai.api_key = 'sk-aiHCyzPrDBhhjuYQnEdipZvPvfWpgd0yfFRCzZ7083ONWHId'  # Replace with your OpenAI API key

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-aiHCyzPrDBhhjuYQnEdipZvPvfWpgd0yfFRCzZ7083ONWHId",
    base_url="https://api.chatanywhere.tech/v1"
)

def fetch_rss_feed(url):
    """Fetch and parse RSS feed from the given URL."""
    feed = feedparser.parse(url)
    return feed.entries

# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(completion['choices'][0]['message']['content'])

# 流式响应
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
            print(chunk.choices[0].delta.content, end="")




def summarize_entry(entry, use_stream=False):
    """Generate a summary for a given RSS feed entry using OpenAI."""
    # Create a prompt for the entry
    prompt = f"如何看待这个问题:\n\n标题: {entry.title}\n描述: {entry.description}"
    
    messages = [{"role": "user", "content": prompt}]
    
    if use_stream:
        gpt_35_api_stream(messages)
    else:
        gpt_35_api_stream(messages)
    print("\n" + "-" * 50)

if __name__ == '__main__':
    # RSS feed URL
    rss_feed_url = "https://rsshub.baitry.com/weibo/search/hot"
    
    # Fetch RSS feed entries
    entries = fetch_rss_feed(rss_feed_url)
    
    # Loop through each entry and generate a summary
    for entry in entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        
        # Set use_stream to True for streaming responses, False for non-streaming
        summarize_entry(entry, use_stream=False)
