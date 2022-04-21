
## import the class
from QuestionPrompt import question

question_prompts = [
    "what colors are apples? \n(a)Red \n(b) Purple \n(c) Orange \n\n",
    "what colors are bananas? \n(a)Teal \n(b) Magneta \n(c) Yellow \n\n",
    "what colors are strawberries? \n(a)Yellow \n(b) Red \n(c) Blue \n\n"
]

questions =[
    question(question_prompts[0],'a'),
    question(question_prompts[1],'c'),
    question(question_prompts[2],'b'),
]


def run_test(questions):
    score=0

    for question in questions:
        answer  = input(question.prompt)
        if answer==question.answer : 
            score += 1
            
    print(" final score is: "+str(score))            


run_test(questions)
