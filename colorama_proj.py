
# for this project, there will be options that will allow user to view different possible ways that colorama can be used.

from colorama import Fore, Back, Style

def start_colorama():
    # option variable will store a number (1 or 2) that will represent the option that will be printed out
    option = int(input("Please input 1 or 2? "))


    # option 1 is an example of using colorama with text
    # option 2 is an example of using colorama in an artistic form

    if option == 1:
       option_1()



def option_1():
    #setting backgroud white and text to black
    print(Back.WHITE + Fore.BLACK + "In this example I am using a white background with black text")
    
    #resetting colors
    print(Style.RESET_ALL + "By using Style.RESET_ALL I am now back to normal text")
  
    print(" ")
    print(Back.YELLOW + Fore.BLACK + "Colorama might actually be a useful tool for learning code")
    
    print("")
    print(Style.RESET_ALL + "I'll do an example below")
    
    



start_colorama()
