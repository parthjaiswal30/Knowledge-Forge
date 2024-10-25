import unittest
from models.quiz_generator import generate_quiz_questions

class TestQuizGeneratorFunctionality(unittest.TestCase):

    def test_generate_quiz_questions(self):
        sample_summary = "Machine learning is a field of artificial intelligence. It involves algorithms."
        expected_questions = [
            "What is machine learning?",
            "What does machine learning involve?"
        ]

        generated_questions = generate_quiz_questions(sample_summary)

        self.assertEqual(len(generated_questions), len(expected_questions))
        for question in expected_questions:
            self.assertIn(question, generated_questions)

if __name__ == "__main__":
    unittest.main()
