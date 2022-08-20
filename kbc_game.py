import random

questions = ['When is World Earth Day?',
             'Which country was part of the allies in World War 2?',
             'Which is fastest car in 2021?',
             'Which is full form of BCCI?',
             'Who developed Python language']

'''add random current_options Done
add question randomizer done
add settings to add lifeline conditions done
add a lifeline done
add better error handeling done
make the interface look better done
add QUESTION done
remove questions done
ensure only 4 options are considered done
ensure that the game control can only be accessed if no one has played the game Done
'''

options = [
['10 June', '25 December', '22 April' , '29 Febuary'],
['The UK', 'Japan', 'South Africa' , 'Australia'],
['Ferrari', 'Tesla Model 3', 'Buggati' , 'SSC Tuatara'],
['Board of Control for Cricket', 'Board of Control for Cricket in India', 'Board of Cricket in India' , 'Board of Council for Cricket in India'],
['Charles Babbage', 'Dennis Ritchie', 'Djarne' , 'Guido Van'],
]

answers = ['22 April', 'The UK', 'SSC Tuatara', 'Board of Control for Cricket in India', 'Guido Van']

def number_check(lower_limit,upper_limit,user_message):
    while True:
        try:
            user_input=int(input(user_message))
            if user_input>upper_limit or user_input<lower_limit:
                print('Your number is outside, the acceptable limit.')
                continue
            break
        except:
            print('Your input should be a number, the number represents your choice')
            continue
    return user_input

def randomized_options(option_number,options):
    current_options=options[option_number]
    random.shuffle(current_options)
    return current_options

def play_game(name, questions, answers, options, user_input_lifelines):
    print("Hello",name, ".. All the best!!")
    print('\nYou have',user_input_lifelines,'lifeline, to use the lifeline press on 5')
    lifeline=user_input_lifelines
    scores = 0
    number_list=[]
    for i in range(len(questions)): number_list.append(i)
    for i in range(len(questions)):
        if len(number_list)>1:
            question_randomizer=random.choice(number_list)
        else:
            question_randomizer=number_list[0]
        current_question = questions[question_randomizer]
        correct_answer = answers[question_randomizer]
        current_options = randomized_options(question_randomizer,options)
        print("\nQuestion ",i+1,'\n',current_question,sep='')
        for counter, each_option in enumerate(current_options):
            print(counter+1, ") ", each_option, sep='')
        while True:
            user_answer_index = number_check(1,5,"\nPlease enter your option (1,2, 3 or 4) : ")
            if user_answer_index==5 and lifeline>0:
                lifeline=lifeline-1
                while True:
                    random_number=random.randint(0,3)
                    if current_options[random_number]==correct_answer:
                        continue
                    wrong_option=current_options[random_number]
                    current_options=[correct_answer, wrong_option]
                    random.shuffle(current_options)
                    for counter, each_option in enumerate(current_options):
                        print(counter+1, ") ", each_option, sep='')
                    user_answer_index = number_check(1,2,"\nPlease enter your option (1 or 2) : ")
                    break
            elif user_answer_index==5 and lifeline==0:
                print('No lifelines left')
                continue
            break
        user_answer = current_options[user_answer_index-1]
        if user_answer == correct_answer:
            print("Correct Answer")
            scores += 100
        elif scores==500:
            break
        else:
            print("Wrong Answer")
            break
        number_list.remove(question_randomizer)
    print("Your final score : ", scores)
    return name, scores

def view_score(names_and_scores):
    print('\n')
    for name, score in names_and_scores.items():
        print(name, "scored", score)

def user_lifeline(questions,lifelines):
    print('\nBy default lifeline is set to 1, you can change it')
    print('The current lifeline amount is',lifelines)
    lifelines=number_check(0,len(questions),'Number of lifelines: ')
    return lifelines

def user_input_question(questions,answers,options):
    user_question=input('Please input the question: ')
    questions.append(user_question)
    user_correct_answer=input('Please input the correct answer: ')
    answers.append(user_correct_answer)
    user_options=[user_correct_answer]
    for i in range(3):
        user_wrong_option=input('Please enter a wrong option:')
        while True:
            if user_wrong_option==user_correct_answer:
                print('Wrong option and correct option is matching, please enter another wrong option')
                user_wrong_option=input('Please enter a wrong option: ')
                continue
            else: break
        user_options.append(user_wrong_option)
    options.append(user_options)

def user_remove_question(questions,options,answers,lifelines):
    if len(questions)>1 and len(questions)>lifelines:
        for i in range(len(questions)):
            print(i+1,questions[i])
        user_removed_question_number=number_check(0,len(questions),'\nQuestion number of question to be removed or 0 to exit: ')
        if user_removed_question_number==0:return
        questions.remove(questions[user_removed_question_number-1])
        options.remove(options[user_removed_question_number-1])
        answers.remove(answers[user_removed_question_number-1])
    else:
        print('\nGame has to have 1 question or number of lifelines has to be smaller than number of questions: ')
        return

def display_screen(questions, answers, options):
    names_and_scores = {}
    lifelines=1
    while True:
        print("\nWelcome to the KBC Game...")
        print("1) Play Game\n2) View Scores\n3) Exit\n4) game_control")
        user_input = number_check(1,4,"Please enter your input (1, 2, 3, 4) : ")
        if user_input == 1:
            name = input("Please enter your name : ")
            name, score = play_game(name, questions, answers, options,lifelines)
            names_and_scores[name] = score
        elif user_input == 2:
            view_score(names_and_scores)
        elif user_input == 3:
            break
        elif user_input == 4:
            if names_and_scores == {}:
                user_input_game_control=number_check(1,3,'1) Change lifelines\n2) Questions\n3) Exit\n')
                if user_input_game_control==1:
                    lifelines=user_lifeline(questions,lifelines)
                elif user_input_game_control==2:
                    user_input_game_control_questions=number_check(1,3,'1) Add questions\n2) Remove questions\n3) Exit\n')
                    if user_input_game_control_questions==1:
                        while True:
                            user_input_question(questions,answers,options)
                            user_input_game_control_questions_continue=number_check(1,2,'1) Add questions\n2) Exit\n')
                            if user_input_game_control_questions_continue==1: continue
                            else: break
                    elif user_input_game_control_questions==2:
                        while True:
                            user_remove_question(questions,options,answers,lifelines)
                            user_input_game_control_questions_continue=number_check(1,2,'\n1) Remove questions\n2) Exit')
                            if user_input_game_control_questions_continue==1: continue
                            else: break
                elif user_input_game_control==3:
                    print('Removing from game control')
            else:
                print('Game control for the game is already set')
        else:
            print("Invalid input.. Please enter valid input again...")

display_screen(questions, answers, options)
