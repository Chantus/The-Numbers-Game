import random


print("Welcome to the Numbers Guessing Game!")
num1 =  random.randint(0, 10)
attempt_count = 1
choice = input("please choose a random number between 0 and 10    ")
   

    
while True:     
    try:
       if int(choice) > num1:
          choice = input("Try Again.  Your number is too high   ")
          attempt_count += 1  
       if int(choice) < num1:
          choice = input("Try Again.  Your number is too low   ")
          attempt_count += 1
   
       if int(choice) == num1:
          
          print("Great Guess! It took you {} attempts!\n  ".format(attempt_count))
          print("Thanks for playing the Numbers Guessing Game!")
          break
          
          
        
          
    except ValueError:
          choice = input("Please enter a valid value   ")
            
    


                     
       

            