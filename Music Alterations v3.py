import os
import eyed3


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def title_alteration(music_artist_string):
    music_artist_string = music_artist_string.replace(';', ' feat. ', 1)
    semicolon_count = music_artist_string.count(';')
    music_artist_string = music_artist_string.replace(';', ', ', semicolon_count-1)
    music_artist_string = music_artist_string.replace(';', ' & ')
    return music_artist_string


def main():
    audio_files = eyed3.load(files('D:\\iTunes Music\\iTunes\\iTunes Media\\Music'))
    title_alteration(audio_files.tag.artist)


if __name__ == '__main__':
    main()
