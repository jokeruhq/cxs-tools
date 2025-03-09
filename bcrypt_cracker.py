import requests
import bcrypt
from concurrent.futures import ThreadPoolExecutor, as_completed
from pystyle import Colors, Colorate

def format_message(prefix, message):
    colored_prefix = Colorate.Color(Colors.red, f"  [{Colors.white}!{Colors.red}]")
    return f"{colored_prefix}{Colors.reset} {message}"

def check_word(word, hash):
    try:
        if bcrypt.checkpw(word.encode("utf-8"), hash.encode("utf-8")):
            return (word, True)
    except Exception as e:
        print(format_message("Error", f"Error with '{word}': {str(e)}"))
    return (word, False)

def crackbcrypt(hash):
    if not (hash.startswith(("$2a$", "$2b$", "$2y$")) and len(hash) == 60):
        print(format_message("Error", "Invalid bcrypt hash."))
        return None
    print(format_message("Info", "Downloading wordlist..."))
    try:
        response = requests.get("https://raw.githubusercontent.com/tarraschk/richelieu/master/french_passwords_top20000.txt", timeout=15)
        response.raise_for_status()
        words = [word.strip() for word in response.text.splitlines() if word.strip()]
        words = list(dict.fromkeys(words))
        print(format_message("Success", f"{len(words)} words loaded (e.g.: '{words[13]}')."))
    except Exception as e:
        print(format_message("Error", f"Download failed: {str(e)}"))
        return None
    print(format_message("Info", f"Starting crack with {len(words)} words..."))
    found = None
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(check_word, word, hash): word for word in words}
        try:
            for future in as_completed(futures):
                word, status = future.result()
                if status:
                    found = word
                    executor.shutdown(wait=False, cancel_futures=True)
                    print(format_message("Success", f"Password found: {word}{Colors.reset}"))
                    return found
                print(format_message("Debug", f"Tested: {word}"), end="\r")
        except Exception as e:
            print(format_message("Error", f"   Crash: {str(e)}"))

    if not found:
        print(format_message("Error", "No result."))
    return found

banner = """\n\n\n
        ▄████▄  ▒██   ██▒  ██████     ▄▄▄▄     █████▒▒█████   ██▀███   ▄████▄  ▓█████  ██▀███  
        ▒██▀ ▀█  ▒▒ █ █ ▒░▒██    ▒    ▓█████▄ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒
        ▒▓█    ▄ ░░  █   ░░ ▓██▄      ▒██▒ ▄██▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   ▓██ ░▄█ ▒
        ▒▓▓▄ ▄██▒ ░ █ █ ▒   ▒   ██▒   ▒██░█▀  ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  
        ▒ ▓███▀ ░▒██▒ ▒██▒▒██████▒▒   ░▓█  ▀█▓░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒
        ░ ░▒ ▒  ░▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░   ░▒▓███▀▒ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░
        ░  ▒   ░░   ░▒ ░░ ░▒  ░ ░   ▒░▒   ░  ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░
        ░         ░    ░  ░  ░  ░      ░    ░  ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░     ░░   ░ 
        ░ ░       ░    ░        ░      ░                 ░ ░     ░     ░ ░         ░  ░   ░     
        ░                                   ░                          ░                        
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')
import socket
pc_name = socket.gethostname()
gradient_banner = Colorate.Vertical(Colors.red_to_white, banner)
print(gradient_banner)
hash_input = input(f"   {Colors.red}┌───({Colors.reset}{pc_name}{Colors.red})\n   └──$ {Colors.reset}Enter the hash to crack (bcrypt only): ")
result = crackbcrypt(hash_input)
