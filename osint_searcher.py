import os, time, fade
from colorama import Fore, Style
from googlesearch import search

class color:
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ret():
    choice = input(color.WHITE + f'\n[*] Press {color.RED}ENTER{color.WHITE} to return to the menu: ')
    main()

def error(text):
    print(color.WHITE + f'\n[*] Unexpected error in {color.RED}OSINT{color.WHITE}: ' + color.RED + text)
    choice = input(color.WHITE + f'[*] Press {color.RED}ENTER{color.WHITE} to return to the menu: ')
    main()

def fetch_top_search_results(query, num_results=10):
    search_results = []
    try:
        for result in search(query, num=num_results, pause=2.0):
            search_results.append(result)
    except Exception as e:
        print(f"{color.RED}Error: {e}{color.RESET}")
    return search_results

def main():
    clear()
    title = '''
    /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$
   /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/
  | $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$       
  | $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$       
  | $$  | $$ \____  $$  | $$  | $$  $$$$   | $$       
  | $$  | $$ /$$  \ $$  | $$  | $$\  $$$   | $$      
  |  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$   | $$      
   \______/  \______/ |______/|__/  \__/   |__/   
'''
    print(fade.fire(title))

    search_query = input(color.WHITE + "  [*] Enter your search query: ")
    print('\n')
    top_results = fetch_top_search_results(search_query, num_results=10)

    if not top_results:
        print(f"{color.RED}  [*] No results found or an error occurred{color.RESET}")
    else:
        print(color.WHITE + "  [*] Search results: " + '\n')
        for idx, result in enumerate(top_results, 1):
            print(f"{color.GREEN}  [{color.WHITE}{idx}{color.GREEN}] {result}{color.RESET}")

    ret()

if __name__ == '__main__':
    main()
