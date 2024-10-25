import json
import os

class StudyPlan:
    def __init__(self, user_id):
        self.user_id = user_id
        self.study_plan = {}
        self.load_study_plan()

    def load_study_plan(self):
        """Load the study plan from a JSON file, if it exists."""
        try:
            with open(f"data/processed/study_plan_{self.user_id}.json", "r") as f:
                self.study_plan = json.load(f)
        except FileNotFoundError:
            self.study_plan = {}

    def save_study_plan(self):
        """Save the current study plan to a JSON file."""
        with open(f"data/processed/study_plan_{self.user_id}.json", "w") as f:
            json.dump(self.study_plan, f)

    def add_topic(self, topic, hours_needed):
        """Add a topic to the study plan."""
        self.study_plan[topic] = {"hours_needed": hours_needed, "hours_studied": 0}
        self.save_study_plan()

    def update_progress(self, topic, hours_studied):
        """Update progress for a specific topic."""
        if topic in self.study_plan:
            self.study_plan[topic]["hours_studied"] += hours_studied
            self.save_study_plan()

    def display_study_plan(self):
        """Display the current study plan."""
        print("Study Plan:")
        for topic, data in self.study_plan.items():
            print(f"{topic}: {data['hours_studied']} hours studied / {data['hours_needed']} hours needed")

if __name__ == "__main__":
    user_study_plan = StudyPlan(user_id="student1")
    user_study_plan.add_topic("Mathematics", 10)
    user_study_plan.update_progress("Mathematics", 2)
    user_study_plan.display_study_plan()
