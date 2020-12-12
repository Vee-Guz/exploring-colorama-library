
# for this project, there will be options that will allow user to view different possible ways that colorama can be used.

from colorama import Fore, Back, Style

def start_colorama():
    # option variable will store a number (1 or 2) that will represent the option that will be printed out
    option = int(input("Please input 1 or 2? "))


    # option 1 is an example of using colorama with text
    # option 2 is an example of using colorama in an artistic form

    if option == 1:
       option_1()
    elif option == 2:
       option_2()
    else:
       print("Not valid entry")



def option_1():
    #setting backgroud white and text to black
    print(Back.WHITE + Fore.BLACK + "In this example I am using a white background with black text")
    
    #resetting colors
    print(Style.RESET_ALL + "By using Style.RESET_ALL I am now back to normal text")
  
    print(" ")
    print(Back.YELLOW + Fore.BLACK + "Colorama might actually be a useful tool for learning code")
    
    print("")
    print(Style.RESET_ALL + "I'll do an example below")
    
    print("If we wanted to teach about how variables work in python we can do so using colorama. Let's take into account, x = 5")

    variable = Back.RED + "x" + Back.RESET
    value = Back.CYAN + "5"+ Back.RESET
    

    print("The variable is " + variable + ". A variable stores a value in memory that can be accessed throughout your code. In this scenario, our variable is called x, but it can have any name as long as it does not start with a number.")


    print("The value is " + value)
    
    print("By writing " + variable + " = " + value + " we are saying that x holds the content of interger 5")


    print("When we want to refer to our value of variable " + variable + " we simply just use the name that we named the variable. For example, if we do " +
         variable + " 10. What would be the result?")
    


def option_2():  
    # the drawing will be a christmas tree
    
    # * represents the start and it will be in yellow, since I will be using green next I am resetting after printing the star
    print(Fore.YELLOW + "      *      " + Fore.RESET)
    
    # printing 0's to make a tree
    # Since text has been defined above any text I write will also be green and bright
    print(Fore.GREEN + "      0      ")
    print("     000     ")
    print("    00000    ")
    print("   0000000   ")
    print("  000000000  ")
   
    # When ever we want to reset we have to print it as well, text will now be black, | represent the start of the tree stump
    print(Fore.RESET + Fore.RED + "      |      ")
    

start_colorama()
