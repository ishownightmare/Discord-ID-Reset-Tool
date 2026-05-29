import asyncio
import os
import sys
import time
import webbrowser
from pyfiglet import Figlet
from core.Bot import run_bot

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def startup_process():
    clear_screen()
    stages = ["Initializing...", "Connecting...", "Summoning Justice...", "Ready!"]
    for stage in stages:
        sys.stdout.write(f"\r⚡ {stage}")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

def badass_ui():
    clear_screen()
    figlet = Figlet(font="slant")
    print("\033[91m" + figlet.renderText("JUSTICE") + "\033[0m")
    print("\033[95mMade by ZyZe\033[0m")
    print("\033[94mJoin:\033[0m https://discord.gg/U6yKn2Dt4V\n")
    print("\033[92m[1]\033[0m Reset Friends")
    print("\033[94m[2]\033[0m Reset Groups")
    print("\033[96m[3]\033[0m Reset Servers")
    print("\033[93m[4]\033[0m Reset DMs")
    print("\033[95m[5]\033[0m Full Reset (ALL)")
    print("\033[91m[0]\033[0m Exit\n")
    return input(">> Select an option: ").strip()

async def main():
    webbrowser.open("https://discord.gg/U6yKn2Dt4V", new=2)
    startup_process()
    while True:
        choice = badass_ui()
        if choice == "0":
            print("⚡ Exiting JUSTICE...")
            break
        await run_bot(choice)
        input("\nPress Enter to return to JUSTICE menu...")

if __name__ == "__main__":
    asyncio.run(main())
