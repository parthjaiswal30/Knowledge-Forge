import os
from models.summarize import process_and_summarize
from models.quiz_generator import generate_quiz_questions, save_quiz
from models.feedback_manager import provide_feedback
from config.settings import RAW_DATA_PATH, PROCESSED_DATA_PATH

def main():
    for filename in os.listdir(RAW_DATA_PATH):
        if filename.endswith(".pdf"):
            raw_path = os.path.join(RAW_DATA_PATH, filename)
            summary_path = os.path.join(PROCESSED_DATA_PATH, f"summary_{filename[:-4]}.txt")
            process_and_summarize(raw_path, summary_path)

            with open(summary_path, "r") as f:
                summary_text = f.read()
            quiz_path = os.path.join(PROCESSED_DATA_PATH, f"quiz_{filename[:-4]}.txt")
            questions = generate_quiz_questions(summary_text)
            save_quiz(questions, quiz_path)

    sample_results = "Student answered 4 out of 5 questions correctly."
    feedback = provide_feedback(sample_results)
    print("Feedback:\n", feedback)

if __name__ == "__main__":
    main()