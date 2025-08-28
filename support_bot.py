##!pip install textblob deep-translator transformers langdetect

import torch
from textblob import TextBlob
from deep_translator import GoogleTranslator
from transformers import pipeline
from langdetect import detect

# ------------------------------
# Select device: GPU if available, else CPU
# ------------------------------
device = 0 if torch.cuda.is_available() else -1
print("Using device:", "GPU" if device == 0 else "CPU")

# ------------------------------
# Load Hugging Face models with safe fallback
# ------------------------------
try:
    print("Loading flan-t5-xl...")
    generator = pipeline("text2text-generation", model="google/flan-t5-xl", device=device)
except RuntimeError as e:
    if "out of memory" in str(e).lower():
        print("⚠️ Out of memory on flan-t5-xl. Falling back to flan-t5-large...")
        torch.cuda.empty_cache()
        generator = pipeline("text2text-generation", model="google/flan-t5-large", device=device)
    else:
        raise e

sentiment_model = pipeline("sentiment-analysis", device=device)

# ------------------------------
# Example complaint
# ------------------------------
complaint = "Hey my monitor became a black screen suddenly, tell me how to solve it"

# Step 1: Detect language + sentiment
lang = detect(complaint)
sentiment = sentiment_model(complaint)[0]

print("Detected Language:", lang)
print("Sentiment:", sentiment)

# ------------------------------
# Step 2: Generate responses with FEW-SHOT examples
# ------------------------------
tones = ["formal", "empathetic", "casual"]
responses = {}

few_shot_example = """
Example Response (Formal):
Apology: I'm sorry for the inconvenience.
Acknowledgement: I understand your monitor has suddenly gone black.
Troubleshooting steps:
- Step 1: Please ensure the monitor power cable is securely connected.
- Step 2: Verify HDMI or Display cables are properly plugged in.
- Step 3: Restart the computer and adjust brightness if possible.
Next step: If the issue continues, please contact IT support for further assistance.
"""

for tone in tones:
    prompt = f"""
You are an IT support assistant.
Customer complaint: "{complaint}"

Your task: Write a {tone} style reply.
Always follow this structure:

Apology: (one sentence)
Acknowledgement: (one sentence about the black screen problem)
Troubleshooting steps:
- Step 1: Check monitor power connection.
- Step 2: Verify HDMI/Display cables are properly plugged in.
- Step 3: Restart the computer and adjust brightness.
Next step: Advise contacting IT support if issue continues.

{few_shot_example}

Now generate the {tone} reply:
Response:
"""
    resp = generator(
        prompt,
        max_new_tokens=220,
        do_sample=False,
        num_beams=4
    )[0]['generated_text'].strip()

    if "Response:" in resp:
        resp = resp.split("Response:")[-1].strip()

    responses[tone] = resp

# ------------------------------
# Step 3: Translate responses (Spanish + French)
# ------------------------------
for tone, text in responses.items():
    es = GoogleTranslator(source='auto', target='es').translate(text)
    fr = GoogleTranslator(source='auto', target='fr').translate(text)
    print(f"\n{tone.capitalize()} Response")
    print("EN:", text)
    print("ES:", es)
    print("FR:", fr)

# ------------------------------
# Step 4: Mock Quality Metrics
# ------------------------------
print("\n✅ Quality Metrics (Prototype)")
print({
    "response_appropriateness": 0.99,
    "predicted_satisfaction": 0.95,
    "translation_confidence": {"es": 0.97, "fr": 0.94}
})