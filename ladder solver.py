from words import wv_words
from time import time

def get_time(raw):
    raw = round(raw, 2)
    numbers = int(raw)
    decimals = round(raw - numbers, 2)
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365
    final = ""
    if numbers >= year:
        years = int((numbers - (numbers % year)) / year)
        numbers -= years * year
        if years > 0:
            final += f"{years} years "
    if numbers >= day:
        days = int((numbers - (numbers % day)) / day)
        numbers -= days * day
        if days > 0:
            final += f"{days} days "
    if numbers >= hour:
        hours = int((numbers - (numbers % hour)) / hour)
        numbers -= hours * hour
        if hours > 0:
            final += f"{hours} hours "
    if numbers >= minute:
        minutes = int((numbers - (numbers % minute)) / minute)
        numbers -= minutes * minute
        if minutes > 0:
            final += f"{minutes} minutes "
    final += f"{round(numbers + decimals, 2)} seconds"
    return final

def isOneOff(a, b):
    if len(a) != len(b):
        raise TypeError(f"words must be same length {len(a)}=/={len(b)}")
    else:
        return sum([int(a[l].lower() == b[l].lower()) for l in range(len(a))]) == len(a) - 1


start = input("first word: ").lower()
end = input("last word: ").lower()

paths = [[start]]

if start not in wv_words:
    raise TypeError(f"{start} is not a valid word")
if end not in wv_words:
    raise TypeError(f"{end} is not a valid word")
if end == start:
    raise TypeError(f"both words can't be {start}")

print("Algorithm started please wait while solutions are generated")

generation = 0

solutions = []

start_time = time()

while True:                                      # The Algorithm
    length = len(paths) - 1                      # makes a number, so we can see where we are even if the list changes size
    for loc, path in enumerate(paths[::-1]):     # for loop grabbing paths in backwards order so when we delete a path
                                                 # or add one it doesn't affect the loc number
        matches = []                             # matches is used to hold all the words that match my rules
        for word in wv_words:                    # sifts through all words in list
            if isOneOff(path[-1], word) \
                    and word not in path \
                    and not sum([int(isOneOff(turns, word)) for turns in path[:-1]])\
                    and not sum([word in chunk for chunk in paths]):
                                                 # check if word is a One off and not already in path and not already a
                                                 # One off of other turns in path and not in any other paths
                matches.append(word)             # adds word to "matches" if all criteria looks good
        for match in matches:                    # sifts through matched words
            paths.append(path + [match])         # makes new path with previous words and new matched word
        if len(matches):
            del paths[length - loc]              # deletes old path that new paths were based off
    for path in range(len(paths)):               # sifts through paths
        if paths[path][-1] == end:               # check if solution is found
            solutions.append(paths[path])        # adds all solutions to solutions
    generation += 1                              # generation counter increase
    print(f"{generation} generations with {len(paths)} nodes, took {get_time(time() - start_time)}")
    if len(solutions):                           # if solutions exist
        break                                    # break out of for loop

print(f"{len(solutions)} solution{'s' if len(solutions)!=1 else ''} found")
for solution in solutions:
    print(solution)
