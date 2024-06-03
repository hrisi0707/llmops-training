import requests

def generate_text(model, prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Accept":"application/json","Content-Type":"application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream":False
    }

    response = requests.post(url, json=data,headers=headers)
    print (response)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Example usage
model = "llama3:8b"
prompt = "Why is the sky blue?"
result = generate_text(model, prompt)
print(result)