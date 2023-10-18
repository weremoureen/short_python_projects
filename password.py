#import random 

#length = int(input("Enter password length:"))

#s = "trertertdrtdfrtcvghvhgvhkbvkhjbjhkOHBIJBKJBJKLBHBHVCFYGGFCXG1234567890!@#$%^&**()"

#password = "".join(random.sample(s, length))

#print(password)





#import random
#player = input("Enter a choice(rock, paper, scissors): ")
#possible_actions = ["rock", "paper", "scissors"]
#computer_action = random.choice(possible_actions)
#print(f"\nyou chose {player}, computer chose {computer_action}.\n")

#if player == computer_action:
   #print(f"Both players selected {player}. its a tie!")
#elif player == "rock":
   #if computer_action == "scissors":
      #print("Rock smashes scissors! You win!")
   #else:
      #print("Paper covers rock! You lose.")

#elif player == "paper":
   #if computer_action == "rock":
      #print("Paper covers rock! You win!")
   #else:
      #print("scissors cut paper! you lose")

#elif player == "scissors":
   #if computer_action == "paper":
      #print("Scissors cut paper! You win!")
   #else:
      #print("Rock smashes scissors! You lose.")







#import face_recognition
#picture_of_me = face_recognition.load_image_file("me.jpg")
#my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

#unknown_picture = face_recognition.load_image_file("unknown.jpg")
#unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

#results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

#if results[0] == true:
  #print("it's a picture of me!")
#else:
  #print("It's not a picture of me!")






#import random
#lower_bound = 1
#upper_bound = 1000
#max_attempt = 10

#secret_number = random.randint(lower_bound, upper_bound)

#def get_guess():
    #while True:
      #try:
         #guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
         #if lower_bound <= guess <= upper_bound:
            #return guess
         #else:
            #print("Invalid input . please a number within the specified range. ")
      #except ValueError:
            #print("Invalid input. please enter a valid number.")

#def check_guess(guess, secret_number):
    #if guess ==secret_number:
       #return"correct"
    #elif guess < secret_number:
       #return "Too low"
    #else:
       #return "Too high"


#def play_game():
    #attempts = 0
    #won = False
    
    #while attempts < max_attempt:
        #attempts += 1
        
        
    
    
        #guess = get_guess()
        #results = check_guess(guess, secret_number)

        #if results == "correct":    
           #print(f"Congratulations! you guessed the secret number {secret_number} in {attempts} attempts.")
           #won = True
       
           #break
        #else:
           #print(f"{results}. Try again!")
    #if not won:
       #print(f"Sorry, you ran out of attempts! The secret number is {secret_number}. ")
       
#if __name__ == "__main__":
    #print("Welcome to the Number Guessing Game! ")
    #play_game()
       




#def voter_eligibility(age): return age >= 18

#def main():
    #try:
        #age = int(input("Input your age: "))
        #if age < 0:
           #print("Age cannot be negative.")
        #elif voter_eligibility(age):
           #print("You  are eligible to vote.")
        
        #else:
           #print("You are not eligible to vote.")
  
    #except ValueError:
        #print("Invalid input. Please input a valid age.")

#if __name__ == "__main__":
    #main()
    







import secrets
import string
import hashlib
from getpas import getpass

USER_DETAILS_FILEPATH = "users.txt"
PUNCTUATIONS = "@#$%&"
DEFAULT_PASSWORD_LENGTH = 12
INVALID_LENGTH_MESSAGE = f '''

    def generate_password(Length=12):
        characters = string.ascii_letters + string.digits + PUNCTUATIONS
        pwd = ''.join(secrets.choice(characters) for - in range(length))
        return pwd
    
    def hash_password(pwd):
        """Hash a password using SHA-256 algorithm"""
        pwd_bytes = pwd.encode('utf-8')
        hashed_pwd = hashlib.sha(pwd_bytes).hexdigest()
        return hashed_pwd

    def save_user(username, hashed_pwd):
        with open(USER_DETAILS_FILEPATH, "a") as f:
            f.write(f"{username} {hashed_pwd}\n")
        
 



      








