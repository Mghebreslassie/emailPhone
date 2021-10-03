def multi_quiz():
    '''
    creates a simple 12 question multiplication quiz
    with random qoutients and a timer of 30 s
    '''
    import random, time, pyinputplus as pyip
    
#random multiplication quiz
#ask twelve questions
#time quiz 30 secs
    starttime = time.time()
    finishtime = starttime + 30
    
    list = [(random.randint(1,12), random.randint(1,12)) for x in range(1,13)]    
    right = 0
    wrong = 0
    for a, b in list:
        answer = a*b
        response = pyip.inputNum(f'What is {a} times {b}?')
        if answer == response:
            right += 1
            print('Correct')
        else:
            wrong += 1
            print('Incorrect')  
        starttime = time.time()
        if finishtime <= starttime:
            print('You are out of time...')
            break
    print('You got {} right and {} were wrong'.format(right, wrong))

    
#run a for loop randomly select numbers to multiply
#ask for answer
#check answer against calc value
#print right or wrong
#keep track of answer
#give total score at end