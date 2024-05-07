from tkinter import Tk, filedialog
from tkinter import Label, Entry, Button

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

import eyed3

def aud_opener():
    global path
    global aud

    path = filedialog.askopenfilename(filetypes=[('mp3', '.mp3'), ('wma', '.wma'), ('all audio', '*.*')], initialdir='./input/')
    aud = eyed3.load(path)

    aud_title.configure(text=aud.tag.title)
    aud_artist.configure(text=aud.tag.artist)
    aud_genre.configure(text=aud.tag.genre)
    aud_album.configure(text=aud.tag.album)
    aud_date.configure(text=aud.tag.original_release_date)
    aud_albumartist.configure(text=aud.tag.album_artist)
    aud_composer.configure(text=aud.tag.composer)
    aud_tracknumber.configure(text=aud.tag.track_num[0])
    
    title_input.delete(0, len(str(title_input.get())))
    artist_input.delete(0, len(str(artist_input.get())))
    genre_input.delete(0, len(str(genre_input.get())))
    album_input.delete(0, len(str(album_input.get())))
    date_input.delete(0, len(str(date_input.get())))
    albumartist_input.delete(0, len(str(albumartist_input.get())))
    composer_input.delete(0, len(str(composer_input.get())))
    tracknumber_input.delete(0, len(str(tracknumber_input.get())))

    title_input.insert(0, aud.tag.title)
    artist_input.insert(0, aud.tag.artist)
    genre_input.insert(0, aud.tag.genre)
    album_input.insert(0, aud.tag.album)
    date_input.insert(0, str(aud.tag.original_release_date))
    albumartist_input.insert(0, aud.tag.album_artist)
    composer_input.insert(0, aud.tag.composer)
    tracknumber_input.insert(0, aud.tag.track_num[0])
    
    tag_comp_lbl.configure(text='tag : yet!')
    cov_comp_lbl.configure(text='cover : yet!')

def cover_img():
    cov_path = filedialog.askopenfilename(filetypes=[('jpg', '.jpg'), ('png', '.png'), ('all images', '*.*')], initialdir='./input/')
    cov_path = cov_path.replace('\\', '/')

    if cov_path.endswith('png'):
        mime = 'image/png'
    if cov_path.endswith('webp'):
        mime = 'image/webp'
    if cov_path.endswith('jpg'):
        mime = 'image/jpg'
    if cov_path.endswith('jpeg'):
        mime = 'image/jpeg'

    aud = MP3(path, ID3=ID3)
    aud.tags.add(
            APIC(
                encoding=0,
                mime=mime,
                type=3,
                data=open(cov_path, 'rb').read()
            )
        )
    aud.save()

    cov_comp_lbl.configure(text='cover : done!')

def saver():
    aud.initTag()
    aud.tag.title = title_input.get()
    aud.tag.artist = artist_input.get()
    aud.tag.genre = genre_input.get()
    aud.tag.album = album_input.get()
    aud.tag.original_release_date = date_input.get()
    aud.tag.album_artist = albumartist_input.get()
    aud.tag.composer = composer_input.get()
    aud.tag.track_num = tracknumber_input.get()
    aud.tag.save()

    if aud.tag.title:
        aud_title.configure(text=aud.tag.title)
    if aud.tag.artist:
        aud_artist.configure(text=aud.tag.artist)
    if aud.tag.genre:
        aud_genre.configure(text=aud.tag.genre)
    if aud.tag.album:
        aud_album.configure(text=aud.tag.album)
    if aud.tag.original_release_date:
        aud_date.configure(text=aud.tag.original_release_date)
    if aud.tag.album_artist:
        aud_albumartist.configure(text=aud.tag.album_artist)
    if aud.tag.composer:
        aud_composer.configure(text=aud.tag.composer)
    if aud.tag.track_num:
        aud_tracknumber.configure(text=aud.tag.track_num[0])

    tag_comp_lbl.configure(text='tag : done!')

window = Tk()

window.title('mp3tagger 1.2.0')
window.geometry('400x250+400+200')
window.resizable(False, False)
window.iconbitmap('./icon.ico')

aud_title = Label(window, width=20)
aud_title.grid(row=1, column=2, columnspan=2)
aud_artist = Label(window, width=20)
aud_artist.grid(row=2, column=2, columnspan=2)
aud_genre = Label(window, width=20)
aud_genre.grid(row=3, column=2, columnspan=2)
aud_album = Label(window, width=20)
aud_album.grid(row=4, column=2, columnspan=2)
aud_date = Label(window, width=20)
aud_date.grid(row=5, column=2, columnspan=2)
aud_albumartist = Label(window, width=20)
aud_albumartist.grid(row=6, column=2, columnspan=2)
aud_composer = Label(window, width=20)
aud_composer.grid(row=7, column=2, columnspan=2)
aud_tracknumber = Label(window, width=20)
aud_tracknumber.grid(row=8, column=2, columnspan=2)

title = Label(window, text='Title : ')
title.grid(row=1, column=0)
artist = Label(window, text='Artist : ')
artist.grid(row=2, column=0)
genre = Label(window, text='Genre : ')
genre.grid(row=3, column=0)
album = Label(window, text='Album : ')
album.grid(row=4, column=0)
date = Label(window, text='Year : ')
date.grid(row=5, column=0)
albumartist = Label(window, text='Album Artists : ')
albumartist.grid(row=6, column=0)
composer = Label(window, text='Composer : ')
composer.grid(row=7, column=0)
tracknumber = Label(window, text='Track Number : ')
tracknumber.grid(row=8, column=0)

title_input = Entry(window, width=15)
#title_input.insert(0, aud.tag.title)
title_input.grid(row=1, column=1)
artist_input = Entry(window, width=15)
#artist_input.insert(0, aud.tag.artist)
artist_input.grid(row=2, column=1)
genre_input = Entry(window, width=15)
#genre_input.insert(0, aud.tag.genre)
genre_input.grid(row=3, column=1)
album_input = Entry(window, width=15)
#album_input.insert(0, aud.tag.album)
album_input.grid(row=4, column=1)
date_input = Entry(window, width=15)
#date_input.insert(0, str(aud.tag.original_release_date))
date_input.grid(row=5, column=1)
albumartist_input = Entry(window, width=15)
#albumartist_input.insert(0, aud.tag.album_artist)
albumartist_input.grid(row=6, column=1)
composer_input = Entry(window, width=15)
#composer_input.insert(0, aud.tag.composer)
composer_input.grid(row=7, column=1)
tracknumber_input = Entry(window, width=15)
#tracknumber_input.insert(0, aud.tag.track_num[0])
tracknumber_input.grid(row=8, column=1)

opener = Button(text='Open Files', command=aud_opener)
opener.grid(row=9, column=0)
cover = Button(text='Cover Image', command=cover_img, width=10)
cover.grid(row=9, column=2)
saver_btn = Button(text='여!', command=saver, width=10)
saver_btn.grid(row=9, column=3)

cov_comp_lbl = Label(text='cover : yet')
tag_comp_lbl = Label(text='tag : yet')
cov_comp_lbl.grid(row=10, column=2)
tag_comp_lbl.grid(row=10, column=3)

window.mainloop()
