DEFAULT_SUMMARY_MODEL = "facebook/bart-large-cnn"
DEFAULT_QUIZ_MODEL = "text-davinci-003"
DEFAULT_FEEDBACK_MODEL = "text-davinci-003"

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
