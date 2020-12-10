# example from documentation found on https://pypi.org/project/colorama/

from colorama import Fore, Back, Style

# Fore - text color
# Back - background color
# Style - change text

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL) 	# resets all previous settings
print('back to normal')
