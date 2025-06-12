from transformers import pipeline

# Load Hugging Face model
model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_pipeline = pipeline("text-classification", model=model_name, tokenizer=model_name)

def detect_mood(text):
    """
    Detect mood and confidence score from input text.
    Returns:
        mood (str), score (float)
    """
    result = emotion_pipeline(text)
    top_result = result[0]
    mood = top_result['label'].lower()
    score = round(top_result['score'], 2)
    return mood, score
