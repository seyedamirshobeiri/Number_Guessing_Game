#import liberary for random number
import random 

#produce random number
random_number=random.randint(0, 100)

#We use the infinite loop until the correct answer is found
while(True):
    
    #take a number from user until the correct answer is found
    user_number=int(input('please,Enter your number: '))
    
    #if your answer is correct
    if(random_number==user_number):
        break
    #if your number is larger than the number we want
    elif(random_number<user_number):
        print("Your number is larger than the number we want")
        
    ##if your number is smaller than the number we want
    elif(random_number>user_number):
        print("Your number is smaller than the number we want")
        
#when you win
print('You win!')
