import os
import eyed3


# def files(path):
#    for file in os.listdir(path):
#        if os.path.isfile(os.path.join(path, file)):
#            yield file

"""
Turns out that the eyed3.load functionality just takes path as a parameter.
"""


# def path_getter(path):
#    path = input("Please enter what path you'd like: ")
#    print(path)

"""
All Cap!
"""


def title_alteration(music_artist_string):
    music_artist_string = music_artist_string.replace(';', ' feat. ', 1)
    semicolon_count = music_artist_string.count(';')
    music_artist_string = music_artist_string.replace(';', ', ', semicolon_count-1)
    music_artist_string = music_artist_string.replace(';', ' & ')
    return music_artist_string


def main(path):
    audio_files = eyed3.load(path)
    title_alteration(audio_files.tag.artist)


if __name__ == '__main__':
    x = input("Please enter your path: ")
    main(x)
