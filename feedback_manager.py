from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def provide_feedback(quiz_results):
    llm = OpenAI(model_name="text-davinci-003")
    feedback_prompt = "Provide feedback based on the quiz results: {results}"
    prompt = PromptTemplate.from_template(feedback_prompt)
    feedback_chain = LLMChain(llm=llm, prompt=prompt)
    feedback = feedback_chain.run({"results": quiz_results})
    return feedback

if __name__ == "__main__":
    sample_results = "Student answered 3 out of 5 questions correctly, struggling with concepts A and B."
    feedback = provide_feedback(sample_results)
    print("Feedback:\n", feedback)