import random

NAME = input('Hi I am your Math teacher for today. Can you tell me your name please? ')
print('Nice to meet you '+NAME+"! Let's start our math class.")
ENTER = input('Press Enter key to start the class. ')

def main():
    print("\nNow before we start the class there is a notice for you that this class is a life long class so whenever you want to stop the class you just type 'stop' and your class will be over.")
    number = input("\nTell me your favourite number between 1 to 10: ")
    count = 0
    incorrect = 0
    while True:
        number = is_num_not_under_10(int(number))
        a = taking_input(number)
        if a == 0:
            break
        if a == -1:
            incorrect += 1
        count += 1
    users_score(count,incorrect)
    print("\nThanks for playing with Math "+str(NAME))

def users_score(total_attempt,incorrect_attempt):
    '''
    This function is analyse that how the user good or bad in Mathematics based on their attempts.
    '''
    correct_attempt = total_attempt - incorrect_attempt
    average = (correct_attempt / total_attempt) * 100
    if average >= 90:
        print("Excelent!!! "+NAME+" you'r genius.")
        print('You got ',"%.2f"%(average),'%')
    elif average >= 70 and average < 90:
        print("Not bad..."+NAME+" you'r Math is","%.2f"%(average),"% good.")
        print("Try to get more for next time.")
    elif average >= 50 and average < 70:
        print("Hey "+NAME+" you are an average in Math, you got only","%.2f"%(average),"%")
        print("Just practice as much as you can, because practice makes man perfect.")
    elif average >= 30 and average < 50:
        print("You are weak in Math only","%.2f"%(average),"% you got.")
    else:
        print(NAME+" You are very poor in Math","%.2f"%(average),'% is not a better sign of yours.')

def taking_input(number):  
    '''
    It will take the input from the user.
    '''
    return generate_random_calculation(number)

def generate_random_calculation(number):
    '''
    It generates random calculation in the range of 100
    and based on that it will ask us some arithmetic calculation.
    '''
    rand = random.randint(1,100)
    if rand <= 50:
        add_by_user = input("\nOkay, now add "+str(rand)+" to "+str(number)+': ')
        if add_by_user == 'stop':
            return 0
        add_by_comp = rand + number
        incorrect_attempt = checking_correction(int(add_by_user),add_by_comp)
        return incorrect_attempt
    else:
        if number > rand:
            cut_by_user = input("\nOkay, now cut "+str(rand)+" from "+str(number)+': ')
            if cut_by_user == 'stop':
                return 0
            cut_by_comp = number - rand
            incorrect_attempt = checking_correction(int(cut_by_user),cut_by_comp)
            return incorrect_attempt
        else:
            cut_by_user = input("\nOkay, now cut "+str(number)+" from "+str(rand)+': ')
            if cut_by_user == 'stop':
                return 0
            cut_by_comp = rand - number
            incorrect_attempt = checking_correction(int(cut_by_user),cut_by_comp)
            return incorrect_attempt

def checking_correction(by_user,by_computer):
    '''
    this is going to check that the user enterd calculation is correct with computered calculation or not.
    because computer never do the wrong calculation so it a best way to judge human.
    '''
    if by_user != by_computer:
        print('\nohh no... You are wrong\nThe answer is '+str(by_computer))
        print("Don't worry "+NAME+" Let's try again")    
        return -1
    else:
        print('Great!!! you are correct... '+NAME)
    
def is_num_not_under_10(number):
    '''
    This will check that user only enter his favourite number between 1 to 10.
    '''
    while number > 10 or number < 1:
        print(str(number)+" This is not between 1 to 10.")
        number = int(input("Enter a valid number: "))
    return number

if __name__ == '__main__':
    main()