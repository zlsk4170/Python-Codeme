# Konieczność użycia modułu random.
# Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
# Imię musi zaczynać się od wielkiej litery.

import random


def name():
    start = ['ta', 'sa', 'wu', 'pe', 'ga', 're', 'by', 'ko']
    end = ['red', 'ron', 'muk', 'fer', 'muld', 'rados', 'manos']
    call = ['mocny', 'stary', 'brodaty', 'silny']
    title = ['I', 'II', 'III', 'IV', 'V']
    space = [' ']

    random_start = random.choice(start)
    random_end = random.choice(end)
    random_call = random.choice(call)
    random_title = random.choice(title)

    name = random_start + random_end
    name = name.capitalize()
    call = random_call.capitalize()
    space = space[0]
    person = name + space + random_title + space + call
    return name


def activity():
    activity = ['read', 'find', 'search for', 'ask for']
    activity = random.choice(activity)
    return activity


def place():
    place = ['the castle', 'the church', 'the store', 'the palace', 'the village']
    place = random.choice(place)
    return place

def things():
    things = ['instructions','help']
    things = random.choice(things)
    return things

def generate_story():
    scenario1 = [name(), 'went to', place(), 'in order to', activity(), 'instructions']
    scenario2 = [name(), 'wanted to', activity(), things(),'in',place()]
    scenario3 = ['All fighers try to', activity(), things()]
    scenario4 = [name(),'was waiting for',name() ]
    scenario5 = [place().capitalize(),'was destroyed by', name()]
    scenario6 = ['After long fight',name(),'was killed by',name()]
    story = [scenario1,scenario2,scenario3,scenario4,scenario5,scenario6]
    story = random.choice(story)
    str_story=' '
    str_story = str_story.join(story)
    return str_story


story_length = int(input('Put the story length: '))
for i in range(story_length):
    print(generate_story())
