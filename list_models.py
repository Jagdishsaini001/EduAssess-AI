from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_keys = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

for index, api_key in enumerate(api_keys, start=1):

    if not api_key:
        continue

    print("=" * 70)
    print(f"API KEY {index}")
    print("=" * 70)

    try:

        client = genai.Client(api_key=api_key)

        models = client.models.list()

        for model in models:
            print(model.name)

    except Exception as e:

        print(e)

    print()
