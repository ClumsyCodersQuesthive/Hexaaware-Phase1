import random
from questions import questions

def generate_questions(num_easy, num_medium, num_difficult):
    selected_questions = {
        "easy": random.sample(questions["easy"], min(num_easy, len(questions["easy"]))),
        "medium": random.sample(questions["medium"], min(num_medium, len(questions["medium"]))),
        "difficult": random.sample(questions["difficult"], min(num_difficult, len(questions["difficult"]))),
    }
    
    # Print the selected questions to the console
    for difficulty, q_list in selected_questions.items():
        print(f"Difficulty: {difficulty}")
        for q in q_list:
            print(f"- {q}")
        print("\n")
    
    return selected_questions

if __name__ == '__main__':
    # Prompt user for input
    num_easy = int(input("Enter the number of easy questions: "))
    num_medium = int(input("Enter the number of medium questions: "))
    num_difficult = int(input("Enter the number of difficult questions: "))

    # Generate and print the questions
    generate_questions(num_easy, num_medium, num_difficult)