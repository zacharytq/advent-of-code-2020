import re

# passport data seperated by (two??) newlines
# split into list with passports 
def process_input(input):
    result = dict((a.strip(), b.strip())
                    for a, b in (element.split(':')
                        for element in (re.split(r"\s+", passport)
                            for passport in (input.split("\n\n")))))
    return result