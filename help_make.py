import colorama
from colorama import Fore

colorama.init(autoreset=True)

print(Fore.CYAN + "\u25CA update_my_code_rupinder:", Fore.WHITE +
      "Fetches code from github and update main(local) and rupinder(local)")

print("\n\t\u21B3 Usage:", Fore.YELLOW + "make",
      Fore.CYAN + "update_my_code_rupinder", "\n")

print(Fore.CYAN + "\u25CA update_my_code_rishabh:", Fore.WHITE +
      "Fetches code from github and update main(local) and rupinder(local)")

print("\n\t\u21B3 Usage:", Fore.YELLOW + "make",
      Fore.CYAN + "update_my_code_rupinder", "\n")

print(Fore.CYAN + "\u25CA push_changes_rupinder:", Fore.WHITE +
      "Push changes from rupinder to github")

print("\n\t\u21B3 Usage:", Fore.YELLOW + "make", Fore.CYAN +
      "push_changes_rupinder message=" + Fore.MAGENTA + "'Your commit message here'", "\n")

print(Fore.CYAN + "\u25CA push_changes_rishabh:", Fore.WHITE +
      "Push changes from rishabh to github")

print("\n\t\u21B3 Usage:", Fore.YELLOW + "make", Fore.CYAN +
      "push_changes_rishabh message=" + Fore.MAGENTA + "'Your commit message here'", "\n")

print(Fore.CYAN + "\u25CA create_pull_request_rupinder:", Fore.WHITE +
      "create a pull request from rupinder -> main(default)")

print("\n\t\u21B3 Usage:", Fore.YELLOW + "make", Fore.CYAN +
      "create_pull_request_rupinder message=" + Fore.MAGENTA + "'Your pull request message here'", "\n")

print("\t\u2757 Note:", Fore.RED +
      "please push changes before creating a pull request", '\n')

print(Fore.CYAN + "\u25CA create_pull_request_rishabh:", Fore.WHITE +
      "create a pull request from rishabh -> main(default)")

print("\n\t\u21B3 Usage:", Fore.YELLOW + "make", Fore.CYAN +
      "create_pull_request_rishabh message=" + Fore.MAGENTA + "'Your pull request message here'", "\n")

print("\t\u2757 Note:", Fore.RED +
      "please push changes before creating a pull request", '\n')
