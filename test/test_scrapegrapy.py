from scrapegraph_py import Client
from scrapegraph_py.logger import sgai_logger

sgai_logger.set_logging(level="INFO")

# Initialize the client
sgai_client = Client(api_key="sgai-61d399c1-0e33-4622-b7c3-3add27ffb635")
# SmartScraper request
response = sgai_client.smartscraper(
    website_url="https://www.cnblogs.com/wevolf/p/18900728",
    user_prompt="Extract the main information of this articale, including the title, author, date, and main content. Provide the result in JSON format.",
)

# Print the response
print(response)
print(f"Request ID: {response['request_id']}")
print(f"Result: {response['result']}")
if response.get('reference_urls'):
    print(f"Reference URLs: {response['reference_urls']}")

sgai_client.close()