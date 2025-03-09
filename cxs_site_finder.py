from googlesearch import search
from pystyle import Colorate, Colors, Center
from datetime import datetime
import os
import socket

banner = """
    ▄████▄  ▒██   ██▒  ██████      ██████  ██▓▄▄▄█████▓▓█████      █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
    ▒██▀ ▀█  ▒▒ █ █ ▒░▒██    ▒    ▒██    ▒ ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
    ▒▓█    ▄ ░░  █   ░░ ▓██▄      ░ ▓██▄   ▒██▒▒ ▓██░ ▒░▒███      ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
    ▒▓▓▄ ▄██▒ ░ █ █ ▒   ▒   ██▒     ▒   ██▒░██░░ ▓██▓ ░ ▒▓█  ▄    ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
    ▒ ▓███▀ ░▒██▒ ▒██▒▒██████▒▒   ▒██████▒▒░██░  ▒██▒ ░ ░▒████▒   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
    ░ ░▒ ▒  ░▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░░▓    ▒ ░░   ░░ ▒░ ░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░  ▒   ░░   ░▒ ░░ ░▒  ░ ░   ░ ░▒  ░ ░ ▒ ░    ░     ░ ░  ░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
    ░         ░    ░  ░  ░  ░     ░  ░  ░   ▒ ░  ░         ░       ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
    ░ ░       ░    ░        ░           ░   ░              ░  ░           ░           ░    ░       ░  ░   ░     
    ░                                                                                    ░                      
"""

def search_google(query, num_results):
    try:
        results = search(query, lang="en", num=num_results)  
        return list(results)
    except Exception as e:
        print(f"Search error: {e}")
        return []

def main():
    pc_name = socket.gethostname()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter(Colorate.Vertical(Colors.red_to_white, banner)))

    query = input(f"   {Colors.red}┌───({Colors.reset}{pc_name}{Colors.red})\n   └──$ {Colors.reset}Enter your Google dork: ").strip()
    
    if not query:
        print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} No dork entered. Defaulting to: inurl:.php?id=")
        query = "inurl:.php?id="
    
    try:
        num_results = int(input(f"   {Colors.red}┌───({Colors.reset}{pc_name}{Colors.red})\n   └──$ {Colors.reset}Enter the number of results: ").strip())
    except ValueError:
        print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} Invalid value, defaulting to 10 results.")
        num_results = 10

    results = search_google(query, num_results)

    if not results:
        print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} No results found.")
        return

    http_results = [result for result in results if result.startswith('http://')]
    https_results = [result for result in results if result.startswith('https://')]

    print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} HTTP Results:")
    for result in http_results:
        print(f"    {Colors.red}   └──{Colors.reset} {result}")

    print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} HTTPS Results:")
    for result in https_results:
        print(f"    {Colors.red}   └──{Colors.reset} {result}")

    print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} Search complete.")
    print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} Total number of results: {len(results)}")

    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "_results.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"CXS Site finder: {query}\n\n")
        file.write("HTTPS Results:\n")
        for result in https_results:
            file.write(result + "\n")
        file.write("\nHTTP Results:\n")
        for result in http_results:
            file.write(result + "\n")

    print(f"    {Colors.red}[{Colors.white}!{Colors.red}]{Colors.reset} Results exported to file: {filename}")

if __name__ == "__main__":
    main()
