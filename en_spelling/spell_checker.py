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
    """Get and return link to audio file on wiktionary.org
    for the given word in English.
    The first found link of any type (wav, ogg, mpeg)
    is used.

    """
    response = scrape("en", "en", word) 
    # scrape does return translations, so
    # workaround used: translation from en to en
    for d in response['pronunciation']:
        for val in d['values']:
            if val['type'] in ['audio/wav', 'audio/ogg', 'audio/mpeg']:
                return "https:" +  val['value']


def play_sound(link):
    subprocess.call([
        "mplayer", "-nolirc", "-really-quiet",
        "-noconsolecontrols", link, "&> /dev/null"
        ])


def get_correct_input(word):
    while True:
        attempt = input("Spell: ")
        if attempt == word:
            return


def get_words_file(words_file="100_hfw.txt"):
    if len(sys.argv) == 2:
        words_file = sys.argv[1]
    return words_file


def generate_links_for_words(words, n):
    """Generate and return dictionary {"word": "link"}
    with n {key: value} pairs.
    n words are selected randomly from the words list.
    
    """
    result = {}
    while len(result) < n:
        word = random.choice(words)
        link = get_audio_link(word)
        if link:
            result[word] = link
    return result


#TODO: implement functionality to download and save to TMP
# audio files 
#TODO: consider using threading or multiprocessing for downloading,
# consider downloading firstly the file for the first word.
# (Assume dictionary order is guaranteed to be insertion order 
# from python version 3.7.


def main():
    fglt = Figlet()
    print(fglt.renderText("Welcome  to  the  spelling  test!"))

    words_file = get_words_file()
    words = get_words(words_file)
    words_links = generate_links_for_words(words, 10)

    characters = cowsay.char_names
    # Removing ugly chracters from the list 
    for char in ['beavis', 'miki']:
        characters.remove(char)
    
    score = 0
    for word in words_links:
        link = words_links[word]

        i = 0
        while i < 3:
            print("=" * 80)
            play_sound(link)
            attempt = input("Spell: ")
            if attempt == word:
                score += 1
                congratulation = random.choice([
                    "Great!", "Just right!", "Super!", "Very nice!",
                    "Excellent!", "Amazing!", "Cool!", "Well done!",
                    "Great job!", "Awesome!", "Wonderful!", "Fantastic!",
                    "Brilliant!", "Magnificent!", "Terrific!"
                    ])
                #print(fglt.renderText(congratulation)) 
                character = random.choice(characters)
                eval(f"cowsay.{character}('{congratulation}')")
                play_sound(link)
                break
            elif i < 2:
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
