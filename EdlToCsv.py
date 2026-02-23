from sys import argv
from sys import exit
import re
from os import path

if __name__ == "__main__":
    if len(argv) < 3 or not re.match(r".+\.edl$", argv[1]) or not path.exists(argv[1]):
        print("No valid edl file path provided")
        exit()
    try:    
        framerate = int(argv[2])
    except ValueError:
        print("Please enter the timeline's framerate as an integer for the second argument")
        exit()

    # Open text file
    with open(argv[1], "r") as marker_export:
        print("timecode,duration(s),title,notes,script")
        # Split records by double newline [2:] (exclude header). Filter for cream markers to isolate script notes
        for marker in filter(lambda block: re.search(r"ResolveColorCream", block), marker_export.read().split("\n\n")):
            # Parse out each field, render csv line to standard output
            results = re.search(r"(?:\d+\s+){2}V\s+C\s+([\d\:]+)\s[\d\:\s]+([^\|]+)\s+\|.+\|M\:(.+)\s+\|D\:(\d+)", marker)
            timecode = results.groups(0)[0]
            notes = results.groups(0)[1].strip().replace(',', ';').replace('\n', '')
            title = results.groups(0)[2].replace(',', ';')
            duration = float(results.groups(0)[3]) / 60.0
            print(f"{timecode},{duration:.2f},{title},{notes},")