import unittest
from models.feedback_manager import provide_feedback

class TestFeedbackFunctionality(unittest.TestCase):

    def test_provide_feedback(self):
        sample_results = "Student answered 4 out of 5 questions correctly."
        expected_feedback = "Great job! Keep practicing on the topics you struggled with."  # Adjust as needed

        feedback = provide_feedback(sample_results)

        self.assertEqual(feedback, expected_feedback)

if __name__ == "__main__":
    unittest.main()