import random

questions = {
"Keyword used to define a function?": "def",
    "Keyword used to return a value from a function?": "return",
    "Function used to display output on the console?": "print",
    "Function used to get the number of items in a list or string?": "len",
    "Data type returned by 5 / 2 in Python 3?": "float",
    "Keyword used to start a conditional statement?": "if",
    "Keyword used to create a loop over an iterable?": "for",
    "Keyword used to handle exceptions along with except?": "try",
    "Keyword used to define an anonymous, single-line function?": "lambda",
    "Built-in function used to convert a value to a string?": "str",
    "Keyword used to import external modules into a script?": "import",
    "Boolean evaluation result of bool([])?": "False",
    "Built-in function used to generate a sequence of numbers in loops?": "range",
    "Key property of tuples compared to lists (Mutable vs. _____)?": "Immutable",
    "Built-in function used to pair elements from multiple iterables?": "zip",
    "Method used to add an element to the end of a list?": "append"}

def main_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0 

    selected_question = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_question):
     print(f"{index +1}. {question}")
     user_answer = input("Your Answer: ").lower().strip()
     correct_answer = questions[question]

     if user_answer == correct_answer.lower() :
        print("Correct!\n")
        score += 1
     else:
        print(f"Wrong! The correct answer is: {correct_answer}")

    print(f"Game Over! :) Your final score is: {score}/{total_questions}")

main_game()    