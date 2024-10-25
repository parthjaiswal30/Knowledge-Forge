from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

def generate_quiz_questions(summary_text):
    llm = OpenAI(model_name="text-davinci-003")
    quiz_prompt_template = "Generate 5 quiz questions based on the following summary: {text}"
    prompt = PromptTemplate.from_template(quiz_prompt_template)
    quiz_chain = LLMChain(llm=llm, prompt=prompt)
    questions = quiz_chain.run({"text": summary_text})
    return questions

def save_quiz(questions, save_path):
    with open(save_path, "w") as f:
        f.write(questions)
    print(f"Quiz questions saved to {save_path}")

if __name__ == "__main__":
    summary_path = os.path.join("data", "processed", "summary.txt")
    quiz_path = os.path.join("data", "processed", "quiz_questions.txt")

    with open(summary_path, "r") as f:
        summary_text = f.read()
    questions = generate_quiz_questions(summary_text)
    save_quiz(questions, quiz_path)
