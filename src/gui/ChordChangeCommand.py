from gui.Command import Command
from logic.Chordhandler import Chordhandler
import time
import sys
import os

class ChordChangeCommand(Command):
    def __init__(self):
        self.handler = Chordhandler()
        
    def execute(self):
        os.system('cls')
        chord1, chord2 = self.handler.get2RandomChords()

        header = "--------------------------------------------------\n"
        header += "Chord Change Exercise\n"
        header += "--------------------------------------------------"

        print(header)
        time_limit = int(input("Enter time limit in seconds (default 60): "))
        sys.stdout.write("\033[F")
        input(f"Change from {chord1} to {chord2}\nPress any key to start...")
        sys.stdout.flush()
        sys.stdout.write("\033[F")
        
        start_countdown = range(3, 0, -1)
        for i in start_countdown:
            sys.stdout.write(f"Starting in...\n{i}\n")
            sys.stdout.flush()
            time.sleep(1)
            if i != 1:
                sys.stdout.write("\033[F" * 2)  # Move up 2 lines in the console

        print("GO!")

        for i in range(time_limit, -1, -1):
           sys.stdout.write(f"Time left: {i}\n")
           sys.stdout.flush()
           time.sleep(1)
           if i != 0:
               sys.stdout.write("\033[F")  # Move up 4 lines in the console

        print("Time's up!")
        num_changes = int(input("Enter the number of chord changes: "))