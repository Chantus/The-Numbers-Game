import random
def start_game():
   print()
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
          choice = input("Great Guess! It took you {} attempts!".format(attempt_count))
         
    except ValueError:
          choice = input("Please enter a valid value   ")
            
       

            