import unittest
from models.summarize import process_and_summarize

class TestSummarizeFunctionality(unittest.TestCase):

    def test_process_and_summarize(self):
        test_pdf_path = "data/raw/test_sample.pdf"
        expected_summary = "This is a summary of the sample text." 

        summary_output_path = "data/processed/summary_test_sample.txt"
        process_and_summarize(test_pdf_path, summary_output_path)

        with open(summary_output_path, "r") as f:
            generated_summary = f.read().strip()

        self.assertEqual(generated_summary, expected_summary)

if __name__ == "__main__":
    unittest.main()