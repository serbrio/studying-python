#!/usr/bin/env python3

import sys
import subprocess
import random
from scraper import scrape
from pyfiglet import Figlet
import cowsay


def get_words(file):
    words = []
    with open(file) as f:
        # assume: in file given a word in a line
        for line in f:
            words.append(line.strip())
    return words


def get_audio_link(word):
    response = scrape("en", "en", word)
    for d in response['pronunciation']:
        for val in d['values']:
            if val['type'] in ['audio/wav', 'audio/ogg', 'audio/mpeg']:
                #print(val['value'])
                return "https:" +  val['value']


def play_sound(link):
    subprocess.call(["mplayer", "-nolirc", "-really-quiet", link, "&> /dev/null"])


def get_correct_input(word):
    while True:
        attempt = input("Spell: ")
        if attempt == word:
            return


def get_words_file(words_file="100_hfw.txt"):
    if len(sys.argv) == 2:
        words_file = sys.argv[1]
    return words_file


def main():
    words_file = get_words_file()
    words = get_words(words_file)
    ten_words = random.sample(words, 10)
    
    characters = cowsay.char_names
    # Removing ugly chracters from the list 
    for char in ['beavis', 'miki']:
        characters.remove(char)
    
    fglt = Figlet()

    score = 0
    for word in ten_words:
        link = get_audio_link(word)
        
        i = 0
        while i < 3:
            if link:
                print("=" * 80)
                play_sound(link)
            else:
                break

            attempt = input("Spell: ")
            if attempt == word:
                score += 1
                congratulation = random.choice([
                    "Great!", "Just right!", "Super!", "Very nice!", \
                    "Excellent!", "Amazing!", "Cool!", "Well done!", \
                    "Great job!", "Awesome!", "Wonderful!", "Fantastic!", \
                    "Brilliant!", "Magnificent!", "Terrific!"])
                #print(fglt.renderText(congratulation)) 
                character = random.choice(characters)
                eval(f"cowsay.{character}('{congratulation}')")
                break
            print("Try again...")
            i += 1
        else:
            # After 3 attempts passed and no correct spelling entered:
            print("Correct spelling: " + word)
            get_correct_input(word)
            play_sound(link)
            print(fglt.renderText("Nice work!"))
    
    print(fglt.renderText(f"Your score: {score}"))


if __name__ == "__main__":
    main()
