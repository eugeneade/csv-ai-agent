import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"[DEBUG] API Key loaded: {api_key[:5]}...") 
client = OpenAI(api_key=api_key)

# Load CSV data
df = pd.read_csv("sales.csv")

def ask_chatgpt(question):
    system_msg = "You're a helpful assistant that extracts structured query info from natural language."
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": f"From this question: '{question}', extract the store and month."}
        ]
    )
    return response.choices[0].message.content

def parse_and_query(question):
    result = ask_chatgpt(question)
    print(f"[DEBUG] ChatGPT output: {result}")

    lines = result.split("\n")
    store = None
    month = None
    for line in lines:
        if "store" in line.lower():
            store = line.split(":")[1].strip()
        if "month" in line.lower():
            month = line.split(":")[1].strip()

    # Filter dataframe
    filtered = df[(df['store'] == store) & (df['month'] == month)]
    if not filtered.empty:
        revenue = filtered.iloc[0]['revenue']
        return f"The revenue for store {store} in {month} is ${revenue}."
    else:
        return "Sorry, I couldn't find matching data."

if __name__ == "__main__":
    question = input("Ask me a question: ")
    answer = parse_and_query(question)
    print(answer)
