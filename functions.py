import pyfiglet
import random
##############################################################
###           {Difficulties} and {constants}  2122             ###
##############################################################
linebreak = "=" * 75  # seperator
underline = '-' * 17

difficulties = {   # dict containing difficulty(str) and amount of guesses(int)
    1:              "1.EASY",                         # 1
    2:              "2.NORMAL",                       # 2
    3:              "3.HARD",                         # 3
    4:              "4.MEGA HARD",                    # 4
    "1.EASY":           (9,       range(1,11))  ,     # 5       
    "2.NORMAL":         (4,       range(1,51))  ,     # 6      
    "3.HARD":           (2,       range(1,101)) ,     # 7     
    "4.MEGA HARD":      (1,       range(1,1001)),     # 8    
}

constants = {    # this is a dictionary with str and int stored in it 
     "total_correct": 0 , 
     "total_attempts": 0,
     "conswrong": 0,
    } 
def userwrong():
    constants["total_attempts"] += 1     #
    constants["conswrong"] += 1          #
   #                                        # these all update our constants{} dictionary 
def userright():                            
    constants["total_correct"] += 1      #         
    constants["total_attempts"]  += 1    #              
    constants["conswrong"] = 0 

def reset():           # this gets called if a user exits the BNG !
    global constants
    constants = {"total_correct": 0 , "total_attempts": 0,"conswrong": 0}     #
###############################################################################

########################        PRINTS         ################################

def PRINTBNG():   # difficulty select print formatted into func , called in mainmenu
    BNG = pyfiglet.figlet_format(
          f"{'THE BNG':>24}",   # choice of str and centering format
          font = "standard")    # pyfig font
    
    print(f"{linebreak}\n{BNG}")
    print(f"{'[Binary Number Generator]':^75}\n{linebreak}")
    print(f"{'PLEASE SELECT YOUR DIFFICULTY :':^2}") 
    print(f"{'| 1.  EASY    |':^75}") 
    print(f"{'| 2. MEDIUM   |':^75}")
    print(f"{'| 3.  HARD    |':^75}")
    print(f"{'| 4.MEGA HARD |':^75}")
    print(f"{'|      OR     |':^75}")
    print(f"{' / "q" or "quit" \\ ':^75}")  # \\ to be explicit its not a command ?i think ?
    print(linebreak)


def PRINTgameover(): # prints Womp WOMp in a nice ascii format if user really sucks at binary
    gameover = pyfiglet.figlet_format(
        f"{'Womp Womp!':^20}",
        font= "standard")
      
    print(f"{linebreak}\n")
    print(f"{'Out of Guesses!':^75}")
    print(gameover)


def PRINTusergaveup():  # user quit print (mid - game)
    exit = pyfiglet.figlet_format(
        f"{'User Gave Up':^30}", 
        font="standard")
    print(f"{exit}")


def PRINTuserconfirmquit():  # user hit "q" on main menu
    confirmquit = pyfiglet.figlet_format(f"{'Are You Sure ?':>20}",
    font= "standard")
    print(linebreak)                                                                                    
    print(confirmquit) 
    print(linebreak)

def PRINTfinalquit():  # FINAL print statement
    exitgame = pyfiglet.figlet_format(f"{'probably for ':>20}",
    font= "standard")
    exitgame2 = pyfiglet.figlet_format(f"{'the best . . . ':>27}",
    font= "standard")
    print(linebreak)
    print(f"{exitgame}")
    print(f"{exitgame2}")
    print(linebreak)

def PRINTinvalidinput():
            print(linebreak)
            print(f"{'Please enter the corresponding number':^75}" )
            print(f"{'|':^75}")
            print(f"{'V':^75}\n")

            for options in range(1,5):                     #  the values relating to keys 1-4 : 
                    print(f"{difficulties[options]:^75}")  # display key values 1-4
            print(linebreak)


######################### ^ END OF PRINTS ONLY ^ ##########################

######################### v     MEATY BITS     v ##########################


def randomint(questionrange):
    number = random.choice(questionrange)
    binarynum = f"{number:b}"
    return number, binarynum         
#                                            ^                              ^
#                                          question func made to pair with above
#                                             V                              V
def question(difficultychoice):    ### TAKES number and binarynum made to condense and simplify randomint()                             
    number , binarynum = randomint(difficultychoice)
    
    Fstring1 = f"what is : {binarynum} as an integer?"   # combining Fstrings to avoid a "f"""f"" mess 
    Fstring2 = f"Int: {number} (for testing lol idk binary)" # test print
    print(linebreak)
    print(f"{underline*2:^75}")    #     simplified print statements made of fstrings
    print(f"{Fstring1:^75}")       #     
    print(f"{Fstring2:^75}")
    print(f"{underline*2:^75}")           
    print(linebreak)                  

    return int(number) , str(binarynum) 


def usertry():
    guess = input(f"{ 'Enter guess here: ':>45}").strip().lower()
    if guess == "q" or guess == "quit":
         return "USERQUIT"
    try: # try to convert user input into an interger
        guess = int(guess)  
        return guess #if it can be converted, return that interger as our "guess" 
    except ValueError: 
        return None # if user inputs a STR(letter) insted of INT(num) return None to signify try again
 

def yesorno():
    while True:
        yesno = input(f"{ 'Yes or No? (y/n): ':>45}").strip().lower()
        if yesno == "y" or yesno == "yes":
            return  "y"
        elif yesno == "n" or yesno == "no":
            return "n"
        else:
            print("YES OR NO DUMMY")
  
    
def QUITFLAG(): # we are here because user pressed "q"
    PRINTuserconfirmquit() # are you sure ? 

    userinput = yesorno() # returns "y" or "n"
    if userinput == "y": 
        print(linebreak)
        return "USERQUIT"
    
    else:
        userinput == "n"  # if they didnt want to quit, we will return to the main menu again.
        print(linebreak)
        return "CONTINUE"


