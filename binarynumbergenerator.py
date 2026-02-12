import pyfiglet
from random import randint

## REMOVE PRINT ON LINE 23 IF YOU TRULY WANT A GUESSING GAME 

def generatebinarynumber():
        linebreak = "=" * 50
        total_correct = 0
        total_attempts = 0
        conswrong = 0
        maxwrong = 5
        while True:
            start = pyfiglet.figlet_format(
                  "        THE BNG",
                  font = "standard")
            print(f"{linebreak}\n{start}")
            print("                [Binary Number Generator]")
            while True:
                # Generate ONE number
                target_int = randint(1, 100)
                target_bin = f"{target_int:b}"
                print(f"{linebreak}"f"\nwhat is : {target_bin} as an interger?\n")
                print(f"Int: {target_int} (for testing lol idk binary) \n{linebreak}")

                attempts = 0

                # RETRY LOOP for THIS number (not auto-advancing)
                while True:
                    user_input = input("('q' to quit) answer =  ").strip() # this is the random number
                    # Check if user wants to quit
                    if user_input.lower() == 'q':
                        exit = pyfiglet.figlet_format("         User Gave Up",
                            font = "standard")
                        print(f"{exit}\n                 {total_correct} correct out of {total_attempts} total attempts.\n")
                        return
                    # Try to convert binary input to interger
                    try:
                            guess = int(user_input)
                    except ValueError:
                        print(f"{linebreak}\nthat aint a number dumbass. try again what is : {target_bin} ? ")
                        continue
                    # Check if correct
                    if guess == target_int and conswrong < 5 :
                        total_attempts += 1
                        total_correct += 1
                        attempts += 1
                        conswrong = 0
                        print(f"{linebreak}\nWell done Smartass! {target_bin} = {target_int} (took {attempts} attempts)")          
                        break
                    else: # Wrong answer - keep guessing
                        conswrong += 1
                        attempts += 1
                        total_attempts += 1
                        guesses = (maxwrong - conswrong)
                    if  guess != target_int and conswrong < 5:
                        print("{linebreak}\nYOU IDIOT, try again.\n")
                        print(f"What is {target_bin} as a number ?") 
                        print(f"\nYOU HAVE {guesses} GUESSES LEFT!\n{linebreak} ")
                    else:
                        if conswrong == 5:
                            print(f"{linebreak}\n          FINAL GUESS.\n \nWHAT IS {target_bin} AS A NUMBER ? \n{linebreak}")

                    if conswrong >= 5 and guess == target_int :
                        print("\nwell done ! got it on the last try!")                 
                        total_attempts += 1
                        total_correct += 1
                        attempts -= 1 
                        conswrong = 0
                        break
                    if conswrong > 5 and guess != target_int:

                        gameover = pyfiglet.figlet_format("                        Game Over!",
                        font= "standard")  ##ascii art for game over
                        print(f"{linebreak}{linebreak}\n                                      THE ANSWER WAS - {target_int} - DUMBASS")
                        print(gameover)       
                        print(f"                              You got {total_correct} correct out of {total_attempts} total attempts. \n{linebreak}{linebreak}") 
                        return False
            
generatebinarynumber()