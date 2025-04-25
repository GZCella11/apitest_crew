#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import ApitestCrew

from dotenv import load_dotenv

load_dotenv()   

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def get_user_inputs():
    """
    Get inputs from user through command line prompts.
    """
    print("\n=== AI Research Configuration ===")
    topic = input("Enter the research topic: ")
    current_year = input("Enter the target year for research (press Enter for current year): ")
    
    # Use current year if user didn't specify one
    if not current_year.strip():
        current_year = str(datetime.now().year)
    
    return {
        'topic': topic,
        'current_year': current_year
    }

def run():
    """
    Run the crew.
    """
    print("\nWelcome to the AI Research Crew!")
    inputs = get_user_inputs()
    
    print("\nStarting research with the following parameters:")
    print(f"Topic: {inputs['topic']}")
    print(f"Target Year: {inputs['current_year']}")
    print("\nInitiating crew...\n")
    
    try:
        ApitestCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()


