import random

questions = [
    {
        "question": "What is the capital of India?",
        "answers": ["New Delhi", "Mumbai", "Bangalore", "Kolkata"],
        "correct": "New Delhi"
    },
    {
        "question": "Who is the prime minister of India?",
        "answers": ["Narendra Modi", "Rahul Gandhi", "Arvind Kejriwal", "Mamata Banerjee"],
        "correct": "Narendra Modi"
    },
    {
        "question": "Which of these is a programming language?",
        "answers": ["Python", "French", "Hindi", "Physics"],
        "correct": "Python"
    },
    {
        "question": "Which is the highest mountain peak in the world?",
        "answers": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "correct": "Mount Everest"
    },
    {
        "question": "Which river is the longest in the world?",
        "answers": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "correct": "Nile"
    }
]

# Shuffle the questions
random.shuffle(questions)

# Set the initial prize money to 0
prize_money = 0

# Loop through the questions
for question in questions:
    print(f"Question: {question['question']}")
    print("Answers:")
    for i, answer in enumerate(question['answers']):
        print(f"{i+1}. {answer}")
    user_answer = input("Enter your answer: ")
    if user_answer == question['correct']:
        print("Correct!")
        prize_money += 100000
    else:
        print(f"Incorrect. The correct answer was: {question['correct']}")
        break

print(f"You won a total of {prize_money} rupees!")