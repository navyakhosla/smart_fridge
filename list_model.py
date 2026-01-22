from google import genai

client = genai.Client(api_key="AIzaSyBuBw2LML6N4Q7SS3V9_iDfryollp8y-No")

models = client.models.list()

print("Models available to your API key:\n")
for m in models:
    print(m.name)
