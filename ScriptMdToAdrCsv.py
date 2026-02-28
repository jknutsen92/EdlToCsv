from sys import argv
from sys import exit
from os import path
from datetime import timedelta
import re

def add_timecode(timecode:str, addend_seconds:float, framerate:int) -> str:
    results = re.search(r"(\d{2})\:(\d{2})\:(\d{2})\:(\d{2})", timecode)
    total_seconds = 0
    total_seconds += int(results.groups(0)[0]) * 3600       # Hours
    total_seconds += int(results.groups(0)[1]) * 60         # Minutes
    total_seconds += int(results.groups(0)[2])              # Seconds
    frames = int(results.groups(0)[3])
    addened_frames = int(addend_seconds * framerate)
    frames_sum = (frames + addened_frames) % framerate
    total_seconds += (frames + addened_frames) // framerate
    hours_sum = total_seconds // 3600
    minutes_sum = (total_seconds - hours_sum * 3600) // 60
    seconds_sum = (total_seconds - hours_sum * 3600 - minutes_sum * 60)
    return f"{hours_sum:02d}:{minutes_sum:02d}:{seconds_sum:02d}:{frames_sum:02d}"


if __name__ == "__main__":
    if len(argv) < 3:
        print("please provide input with the following format: EdlToCsv.py 'input_file_path' 60")
        exit()

    if not path.exists(argv[1]):
        print(f"No markdown file found at {argv[1]}")
        exit()
    
    try:
        framerate = int(argv[2])                                        # Necessary for timecode calculations
    except ValueError:
        print("Please enter the timeline's framerate as an integer for the second argument")
        exit()

    row_regex =  re.compile(r"\|\s((?:\d{2}\:){3}\d{2})\s\|([^\|]+)\|([^\|]+)\|([^\|]+)\|([^\|]+)")
    # Open new text file at destination
    with open(argv[1], 'r') as input_md:
        for index, md_line in enumerate(filter(lambda line: row_regex.match(line), input_md.readlines()), start=1):
            results = row_regex.search(md_line)
            timecode_start = results.groups(0)[0].strip()
            duration_seconds = float(results.groups(0)[1].strip())
            timecode_end = add_timecode(timecode_start, duration_seconds, framerate)
            script = results.groups(0)[4].strip()
            print(f'"{index}","{timecode_start}","{timecode_end}","","{script}", "False"')
