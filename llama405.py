from langchain_nvidia_ai_endpoints import ChatNVIDIA
import json
from dotenv import load_dotenv
import os

load_dotenv()


client = ChatNVIDIA(
  model="meta/llama-3.1-405b-instruct",
  api_key=os.getenv("NVIDEA_API_KEY"), 
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
)

word = "प्रधानमंत्री"
contents = []
for chunk in client.stream([{"role": "user", "content": f"Give me 10 english words that transliterate {word} in JSON. OUTPUT ONLY JSON"}]):
    contents.append(chunk.content)

# Combine all chunks into a single string
full_content = ''.join(contents)

# Prepare the data to be written to JSON
data = {"content": full_content}

# Write the data to a JSON file
with open(f'{word}_json.json', 'w') as json_file:
    json.dump(data, json_file)

print("Chunk content has been saved to output.json")
    