# Konieczność użycia modułu random.
# Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
# Imię musi zaczynać się od wielkiej litery.

import random


def name():
    vowels = ['a','e','i','u','y','o']
    consonant = ['t','s','w','p','g','r','b','k']
    random_start = random.choice(consonant)+random.choice(vowels)
    random_end = random.choice(consonant) + random.choice(vowels) + random.choice(consonant)

    call = ['mocny', 'stary', 'brodaty', 'silny','kwrawy','podły','niski','szybki']
    title = ['I', 'II', 'III', 'IV', 'V','VI','VII']
    space = [' ']

    random_call = random.choice(call)
    random_title = random.choice(title)

    name = random_start + random_end
    name = name.capitalize()
    call = random_call.capitalize()
    space = space[0]
    person = name + space + random_title + space + call
    return person


def activity():
    activity = ['give', 'find', 'search for', 'ask for']
    activity = random.choice(activity)
    return activity


def place():
    place = ['the castle', 'the church', 'the store', 'the palace', 'the village', 'the cave', 'the shed']
    place = random.choice(place)
    return place

def things():
    things = ['instructions','help','swords','fighters']
    things = random.choice(things)
    return things

def generate_story():
    scenario1 = [name(), 'went to', place(), 'in order to', activity(), 'instructions']
    scenario2 = [name(), 'wanted to', activity(), things(),'in',place()]
    scenario3 = ['All fighers try to', activity(), things()]
    scenario4 = [name(),'was waiting for',name() ]
    scenario5 = [place().capitalize(),'was destroyed by', name()]
    scenario6 = ['After long fight',name(),'was killed by',name()]
    scenario7 = ['When', name(), 'tried to', activity(), 'he was spotted by',name()]
    scenario8 = [name(), 'plans to rebuild', things()]

    story = [scenario1,scenario2,scenario3,scenario4,scenario5,scenario6,scenario7,scenario8]
    story = random.choice(story)
    str_story=' '
    str_story = str_story.join(story)
    return str_story


story_length = int(input('Put the story length: '))
for i in range(story_length):
    print(generate_story())
