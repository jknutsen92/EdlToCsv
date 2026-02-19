# EdlToCsv

I wrote this script to convert the .edl files that Davinci Resolve exports its timeline markers in to a csv output via the console. The intent was to convert from markers to script notes eventually intended to be converted back to ADR cue csv and then re-imported into Resolve.

# Usage

`python EdlToCsv.py "./path_to_file.edl"`

You can redirect the output to a file
`python EdlToCsv.py "./path_to_file.edl" > out.csv`

Or pipe it into the output of another command

`python EdlToCsv.py "./path_to_file.edl" | pyenv exec csv2md`