'''
Random US State-Capitol Quiz generator from 'Automate the Boring Stuff' pg 206
    - Will create 35 different quizzes (questions presented in a different order)
    - Muliple choice
    - With answer key
'''

import random

# The quiz data. Keys are states, and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate 35 different quiz files
for quizNum in range(35): # Go through 35 times, aka the total no. of quizzes we want to have
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w') # name of the quizzes will end with a number, that's why it is %s, to indicate which version of the quiz it is
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)


    # Loop through all 50 states, making a question for each state: options A - D
    for questionNum in range(50): # because there are 50 states
        
        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]] # Easy to obtain, just the value associated with each key!
        wrongAnswers = list(capitals.values()) # First duplicate ALL values in the dict.
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # Then, delete the correct answers!
        wrongAnswers = random.sample(wrongAnswers, 3) # Select random values for the keys, aka  the State capitols for the quiz, and we want 3 wrong answers
        answerOptions = wrongAnswers + [correctAnswer] # Total number of answer options we want on the quiz
        random.shuffle(answerOptions) 

        # Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s? \n' % (questionNum + 1,
            states[questionNum]))
        for i in range(4): # Answer options
            quizFile.write('           %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))
            
    quizFile.close()
    answerKeyFile.close()
        