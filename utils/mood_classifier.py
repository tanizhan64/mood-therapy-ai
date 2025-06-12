from transformers import pipeline

# Load pre-trained emotion classification pipeline
model_name = "j-hartmann/emotion-english-distilroberta-base"

# Create a pipeline object for emotion classification
emotion_pipeline = pipeline("text-classification", model=model_name, tokenizer=model_name, return_all_scores=False)

def detect_mood(text):
    """
    Returns the top predicted emotion for the given input text.
    """
    result = emotion_pipeline(text)
    top_emotion = result[0]['label']
    return top_emotion.lower()
