# 09/14/2021

# Colorizing
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Initializes user input / Error checking
while True:
    try:
        pyramid_height = int(input(f"{Fore.YELLOW}Enter Pryamid Height: "))
        while True:
            if pyramid_height > 8:
                print(f"{Fore.RED}Your number is greater than 8, try again")
                pyramid_height_input = input()
                pyramid_height = int(pyramid_height_input)
            elif pyramid_height <= 0:
                print(f"{Fore.RED}Your number is less than 0 or equal to 0, try again")
                pyramid_height_input = input()
                pyramid_height = int(pyramid_height_input)
            elif pyramid_height <= 8 and pyramid_height > 0:
                print(f"{Fore.GREEN}Pyramid Height:", str(pyramid_height))
                break
        break
    except ValueError:
        print(f"{Fore.RED}Error! That wasn't a valid number, please try again!")

# Making sure number is less than 9, but greater than 0 (per CS50x project instructions)



# To "count" how many '#' are being sent

space_counter = pyramid_height - 1
hashtag_counter = pyramid_height - space_counter

# Makes the pyramid 

while True:
    if hashtag_counter > pyramid_height:
        print(f"{Fore.CYAN}Your pyramid has been generated")
        break
    elif hashtag_counter <= pyramid_height:
        print(space_counter* f"{Fore.BLUE} ", hashtag_counter*f"{Fore.MAGENTA}#", "", hashtag_counter*f"{Fore.MAGENTA}#")
        hashtag_counter+=1
        space_counter-=1