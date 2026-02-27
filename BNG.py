from functions import * 
####################### OUR MAIN MENU ############################

def mainmenu():  # returns "USERQUIT",maxwrong(int) and

    PRINTBNG()  # # difficlty select and guess conversion
    while True:
        userinput = input(f"{ 'Pick a Difficulty: ':>47}").lower().strip() #define terminal prompt text

        while True:
            if userinput == "q" or userinput == "quit":
                    if QUITFLAG() == "USERQUIT":                        #works as intended
                            return "USERQUIT"
            break         
          
        if userinput.isdigit() is False:
            PRINTinvalidinput()
            
        else: 
            userinput = int(userinput)

            if userinput in difficulties:
                userchoice = difficulties[userinput]      #if user types 1- "1.EASY"

                maxwrong = difficulties[userchoice][0] #  9  guesses get returned   # assign the correct amount of guesses : difficulties ->  1(key) = "EASY"(value)  returns  "EASY"(key) = 9(value)  
                diffrange = difficulties[userchoice][1]      
    
                Fstring  = f"{difficulties[userinput][2:]} {'MODE SELECTED'}"  #
                Fstring2 = f"you have {maxwrong +1} guesses"                    #    
    
                print(f"{underline*2:^75}")                                     #      these sections are                                             
                print(f"{Fstring:^75}")                                         #  just all one concise print,         
                print(f"{Fstring2:^75}")                                        #   formatted to the "centere"           
                print(f"{underline*2:^75}")                                     #                                              
                print(linebreak)                                                #                                                  
                return maxwrong , diffrange# give maxwrong back for reference
        
            print(linebreak)
            for userinput in range(1,5):                     #  the values relating to keys 1-4 : 
                    PRINTinvalidinput()  # display key values 1-4



################################################ THE REAL DEAL ################################################
def theBNG():

    while True:                 # displaying difficulties
        difficultydisplay = mainmenu()  # handles difficulty selection

        if difficultydisplay == "USERQUIT": # user Hit "q" in main menu
            PRINTfinalquit()
            return
        
        else:
            difficulty = int(difficultydisplay[0])
            maxwrong = difficulty         # max amount of guesses based on userchoice 
            
            questionrange = difficultydisplay[1] 

        while True:         #num generation loop.                
            target_int, target_bin = question(questionrange)             # question() is just randint() with a question printed and returns an int and str
            attempts = 0    # reset after correct answer 

            while True:                                                                                                                       
                guess = usertry()       # returns 2 values, we check for both here  


                if guess == "USERQUIT":       # "q" will initiate QUITFLAG()
                
                    if QUITFLAG() == "USERQUIT":  # quitflag handles confirmation  
                        ragequit = f"{constants['total_correct']} correct out of {constants['total_attempts']} total attempts."
                        
                        PRINTusergaveup()  # fancy word art condensed into a func
                        print(f"{ragequit:^75}")  
                        print(linebreak)
                        return False  #break out of loop. user QUIT
                        
                    else: # user pressed "N" int quitflag()
                         okthen = f"Ok then, what is: {target_bin}?"
                         
                         print(f"{underline:^75}")
                         print(f"{okthen:^75}")
                         print(f"{underline:^75}")
                         print(linebreak)
                         continue
                        
                                                                                           

                if guess is None:  ### None came back, meaning they need to type a NUMBER
                    print(linebreak)
                    print(f"\n           Thats not a  Number...  try again what is : {target_bin} ?")
                    print(linebreak)
                    continue # skip all to ask again 

                if guess == target_int:  
                    userright() # if user is right, this func updates all relative values

                    print(linebreak)
                    print(f"{underline*3:^75}")
                    print(f"            Well done Smartass! {target_bin} = {target_int} (only took {attempts +1 } attempts)") # plus 1 to account for the latest guess
                    print(f"{underline*3:^75}")
                    break

                userwrong()   # if we are here, all relative values get updated            
                attempts += 1 # answer is wrong,, attempts + 1

                if constants["conswrong"] > maxwrong: #  referencing dictionary key "conswrong" 

                    wrong1 = f" {constants['total_correct']} correct out of {constants['total_attempts']} total attempts."  # f"string to display relative dictionary key 
                    wrong2 = f"By the way the answer was - {target_int} - Dumbass..."  #   insult and kick
                    PRINTgameover() # asci art print   
                    print(f"{wrong1:^75}")  
                    print(f"{wrong2:^75}") 
                    print(linebreak)
                    return #  user gets booted out

                if constants["conswrong"] == maxwrong:   #referencing dictionary for value, checking if on last guess

                    Fstr = f"WHAT IS {target_bin} AS A NUMBER ?"
                    print(linebreak)                
                    print(f"{ 'FINAL GUESS.':^75}")     
                    print(f"{underline:^75}")       
                    print(f"{Fstr:^75}")            
                    print(linebreak)                

                else: # default WRONG message if user has more than 1 guess left
                    guesses = (maxwrong - constants["conswrong"])  # guesses variable is only used here for a print statement

                    Fstr1 = f"{ 'TRY AGAIN DUMBASS' }"                                                                                                                                                                   
                    Fstr2 = f"! You have {guesses + 1} guesses left !"                                                                            
                    Fstr3 = f"What is {target_bin} as a number ?"                                                                            
                    print(f"{linebreak}")                                                                            

                    print(f"{underline*2:^75}") 
                    print(f"{Fstr1:^75}")                                                                               
                    print(f"{Fstr2:^75}")                                                                                     
                    print(f"{underline*2:^75}")
                                                                                                                                          
                    print(f"{Fstr3:^76}")
                    print(f"{underline*2:^75}")                                                                            
                    print(f"{linebreak}")                                                                              

theBNG()
