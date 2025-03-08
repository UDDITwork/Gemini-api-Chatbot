from google import genai

client = genai.Client(api_key="AIzaSyCquSqs56whS2PFWTlWw1ftQM-Gw75j28g")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is the capital of Germany ?"])
print(response.text)