import random
import time

def ChooseOption():
    print(" choose from Rock , Paper Or Scissors : \n")
    print("     Type 'R' or 'ROCK' ")
    print("     Type 'P' or 'PAPER' ")
    print("     Type 'C' or 'SCISSORS' ")
    print("\n     TYPE 'D' FOR DEVELOPER ")
    print("     TYPE 'E' FOR EXIT \n\n")



time.sleep(1)
print(r"""
 ____   ___   ____ _  __
|  _ \ / _ \ / ___| |/ /
| |_) | | | | |   | ' / 
|  _ <| |_| | |___| . \ 
|_| \_\\___/ \____|_|\_\
                        
 ____   _    ____  _____ ____  
|  _ \ / \  |  _ \| ____|  _ \ 
| |_) / _ \ | |_) |  _| | |_) |
|  __/ ___ \|  __/| |___|  _ < 
|_| /_/   \_\_|   |_____|_| \_\
                               
 ____   ____ ___ ____ ____   ___  ____  ____  
/ ___| / ___|_ _/ ___/ ___| / _ \|  _ \/ ___| 
\___ \| |    | |\___ \___ \| | | | |_) \___ \ 
 ___) | |___ | | ___) |__) | |_| |  _ < ___) |
|____/ \____|___|____/____/ \___/|_| \_\____/ """)
print("\n\n")
time.sleep(1)
ChooseOption()
time.sleep(2)



while True:

        
    while True:
        playerChoices = input(" \nChoose : ")
        CapitalPlayerChoices = playerChoices.upper()


        if CapitalPlayerChoices == "R" or CapitalPlayerChoices == "P" or CapitalPlayerChoices == "S":
            break
        if CapitalPlayerChoices == "ROCK" or CapitalPlayerChoices == "PAPER" or CapitalPlayerChoices == "SCISSORS" or CapitalPlayerChoices == "SCISSOR" or CapitalPlayerChoices == "SCISOR" or CapitalPlayerChoices == "SISOR" or CapitalPlayerChoices == "SISORS" or CapitalPlayerChoices == "SISERS" or CapitalPlayerChoices =="SISER" or CapitalPlayerChoices == "CISORS" or CapitalPlayerChoices == "CISOR" or CapitalPlayerChoices == "CICERS" or CapitalPlayerChoices == "CISER":
            break
        
        if CapitalPlayerChoices == "E"  or CapitalPlayerChoices == "EXIT" :
            while True:
                print("\n           Are you sure you want to exit ? : ")
                print("\n        (press Y for yes)     (press N for no)")
                exitChoiceInput = input("\n                            : ")
                exitChoice = exitChoiceInput.upper()
                if exitChoice == "Y" or exitChoice == "YES":
                    exit()
                if exitChoice == "N" or exitChoice == "NO":
                    break
                else:
                    print("\n           please select a valid option\n")
                    continue
        
        if CapitalPlayerChoices == "D" or CapitalPlayerChoices == "DEVELOPER":
            print(r"""
 _____ _   _ ___ ____      ____    _    __  __ _____   __        ___    ____  
|_   _| | | |_ _/ ___|    / ___|  / \  |  \/  | ____|  \ \      / / \  / ___| 
  | | | |_| || |\___ \   | |  _  / _ \ | |\/| |  _|     \ \ /\ / / _ \ \___ \ 
  | | |  _  || | ___) |  | |_| |/ ___ \| |  | | |___     \ V  V / ___ \ ___) |
  |_| |_| |_|___|____/    \____/_/   \_\_|  |_|_____|     \_/\_/_/   \_\____/ 
                                                                              
 ____  _______     _______ _     ___  ____  _____ ____     ______   __
|  _ \| ____\ \   / / ____| |   / _ \|  _ \| ____|  _ \   | __ ) \ / /
| | | |  _|  \ \ / /|  _| | |  | | | | |_) |  _| | | | |  |  _ \\ V / 
| |_| | |___  \ V / | |___| |__| |_| |  __/| |___| |_| |  | |_) || |  
|____/|_____|  \_/  |_____|_____\___/|_|   |_____|____/   |____/ |_|  
                                                                      
    _      ____   __   __     _      _   _ 
   / \    |  _ \  \ \ / /    / \    | \ | |
  / _ \   | |_) |  \ V /    / _ \   |  \| |
 / ___ \  |  _ <    | |    / ___ \  | |\  |
/_/   \_\ |_| \_\   |_|   /_/   \_\ |_| \_|""")            

        else:
            print("\n\n                   Please check your spellings")
            print("                   Or a choose valid option\n")
            ChooseOption()
            continue


    choices = ["ROCK","PAPER","SCISSORS","ROCK","PAPER","SCISSORS","ROCK","PAPER","SCISSORS","ROCK","PAPER","SCISSORS"]
    ComputerChoices = random.choice(choices)

    while True:

        # if CapitalPlayerChoices == ComputerChoices:
        #     print(f"\n           YOU CHOOSED {ComputerChoices}")
        #     time.sleep(2)
        #     print(f"\n           COMPUTER CHOOSED {ComputerChoices}")
        #     time.sleep(1)
        #     print("\n               ITS TIE\n\n")
        #     break    
        if CapitalPlayerChoices == "R" or CapitalPlayerChoices == "ROCK" :

            if ComputerChoices == "PAPER":
                time.sleep(2)
                print(f"\n           YOU CHOOSED ROCK")
                print(f"\n           COMPUTER CHOOSED PAPER")
                time.sleep(1)
                print("\n               YOU LOSE\n\n")
                break
            if ComputerChoices == "ROCK":
                time.sleep(2)
                print(f"\n           YOU CHOOSED ROCK")
                print(f"\n           COMPUTER ALSO CHOOSED ROCK")
                time.sleep(1)
                print("\n               ITS TIE\n\n")
                break
            if ComputerChoices == "SCISSORS":
                time.sleep(2)
                print(f"\n           YOU CHOOSED ROCK")
                print(f"\n           COMPUTER CHOOSED SCISSORS")
                time.sleep(1)
                print("\n               YOU WIN\n\n")
                break


        if CapitalPlayerChoices == "P" or CapitalPlayerChoices == "PAPER" :
                
            if ComputerChoices == "SCISSORS":
                time.sleep(2)
                print(f"\n           YOU CHOOSED PAPER")
                print(f"\n           COMPUTER CHOOSED SCISSORS")
                time.sleep(1)
                print("\n               YOU LOSE\n\n")
                break
            if ComputerChoices == "PAPER":
                time.sleep(2)
                print(f"\n           YOU CHOOSED PAPER")
                print(f"\n           COMPUTER ALSO CHOOSED PAPER")
                time.sleep(1)
                print("\n               ITS TIE\n\n")
                break
            if ComputerChoices == "ROCK":
                time.sleep(2)
                print(f"\n           YOU CHOOSED PAPER")
                print(f"\n           COMPUTER CHOOSED ROCK")
                time.sleep(1)
                print("\n               YOU WIN\n\n")
                break


        if CapitalPlayerChoices == "S" or CapitalPlayerChoices == "SCISSORS" or CapitalPlayerChoices == "SCISSOR" or CapitalPlayerChoices == "SCISOR" or CapitalPlayerChoices == "SISOR" or CapitalPlayerChoices == "SISORS" or CapitalPlayerChoices == "SISERS" or CapitalPlayerChoices =="SISER" or CapitalPlayerChoices == "CISORS" or CapitalPlayerChoices == "CISOR" or CapitalPlayerChoices == "CICERS" or CapitalPlayerChoices == "CISER"   :
                
            if ComputerChoices == "ROCK":
                time.sleep(2)
                print(f"\n           YOU CHOOSED SCISSORS")
                print(f"\n           COMPUTER CHOOSED ROCK")
                time.sleep(1)
                print("\n               YOU LOSE\n\n")
                break
            if ComputerChoices == "SCISSORS":
                time.sleep(2)
                print(f"\n           YOU CHOOSED SCISSORS")
                print(f"\n           COMPUTER ALSO CHOOSED SCISSORS")
                time.sleep(1)
                print("\n               ITS TIE\n\n")
                break
            if ComputerChoices == "PAPER":
                time.sleep(2)
                print(f"\n           YOU CHOOSED SCISSORS")
                print(f"\n           COMPUTER CHOOSED PAPER")
                time.sleep(1)
                print("\n               YOU WIN\n\n")
                break
