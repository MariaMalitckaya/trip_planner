from transformers import pipeline
import torch
import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    """Fetches the content from a given URL and returns it as text."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text, you might need to adjust this based on the website structure
        paragraphs = soup.find_all('p')  
        text = ' '.join([p.text for p in paragraphs])
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""
    except Exception as e:
        print(f"Error parsing content: {e}")
        return ""

# Check if PyTorch is available and can use a GPU
if torch.cuda.is_available():
    device = 0  # Use the first GPU
else:
    device = 'cpu'  # Use the CPU

# Specify the model you want to use.
# For question-answering, a good choice is a model like
# "distilbert-base-cased-distilled-squad".
# You can find suitable models on Hugging Face Model Hub
# (https://huggingface.co/models) by filtering for the
# "question-answering" task.
generator = pipeline(
    'question-answering',
    model='distilbert-base-cased-distilled-squad',
    device=device
)

# 1. Get context from a URL
context_url = "https://www.lonelyplanet.com/articles/best-places-to-visit-europe"  # Example URL
context_url2 = "https://www.forbes.com/sites/ceciliarodriguez/2024/02/07/best-places-to-visit-in-europe-in-2024-marbella-tops-list-by-european-best-destinations/"
context = get_page_content(context_url)+get_page_content(context_url2)

# 2.  Define the question
question = "what was the exact places has been mentioned in the text, output in form of the list. for example [Paris, Monaco]?"

# 3.  Get the answer
if context:  # Only proceed if context was successfully retrieved
    results = generator(question=question, context=context)
    print(results)
    answer = results['answer']
    print(f"The answer is: {answer}")
else:
    print("Could not retrieve context from the URL.")