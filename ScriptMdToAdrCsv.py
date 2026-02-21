# "1","00:00:00:00","00:00:00:01","Character","Script","False"
# https://filmlifestyle.com/timecode-film/
# https://www.geeksforgeeks.org/python/python-datetime-timedelta-function/


from sys import argv
from sys import exit
import re
from os import path
from datetime import timedelta

def add_timecode(timecode:str, seconds:float):
    results = re.search(r"(\d{2})\:(\d{2})\:(\d{2})\:(\d{2})", timecode)
    hours = results.groups(0)[0]

if __name__ == "__main__":
    if len(argv) < 4:
        print("please provide input with the following format: EdlToCsv.py 'input_file_path' 'output_path' 60")
        exit()

    if not path.exists(argv[1]):
        print(f"No markdown file found at {argv[1]}")
        exit()
    
    if not path.exists(path.dirname(argv[2])):
        print("Please provide an output path for a new csv export")
        exit()

    if path.exists(argv[2]):
        print(f"CSV already exists at destination {argv[2]}")
        exit()

    framerate = argv[3]                                         # Necessary for timecode calculations
    # Open new text file at destination
    with open(argv[2], 'w') as output_csv:
        with open(argv[1], 'r') as input_md:
            for md_line in enumerate(index, input_md[2:]):      # Exclude header
                results = re.search(r"\|([^\|\-]+)\|([^\|\-]+)\|([^\|\-]+)\|([^\|\-]+)\|([^\|\-]+)", marker)
                timecode_start = results.groups(0)[0].strip()
                duration_seconds = float(results.groups(0)[1].strip())
                script = results.groups(0)[4]

