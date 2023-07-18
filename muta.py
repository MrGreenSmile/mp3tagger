#https://ko.from-locals.com/python-mutagen-mp3-id3/

from mutagen.easyid3 import EasyID3 as eid
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

file = './input/' + 'canary.mp3'
'''
aud_path = filedialog.askopenfilename(filetypes=[('mp3', '.mp3'), ('wma', '.wma'), ('all audio', '*.*')], initialdir='./input/')
if path == '':
    lbl = Label(window, text='no file')
    lbl.grid(row=9, column=1)
if path:
    path = path.replace('\\', '/')      #\를 /로 바꿔야 EasyID3에서 인식
    aud = eid.load(path)
'''
aud = eid(file)
aud['title'] = 'canary'
aud['artist'] = 'Yonezu Kenshi'
aud['genre'] = 'ballad'
aud['albumartist'] = 'Yonezu Kenshi'
aud['album'] = 'Stray Sheep'
aud['tracknumber'] = '15'
aud['composer'] = 'Yonezu Kenshi'       #textframe
aud['date'] = '2019'                    #timestamp
aud.save()

cover_img = './input/' + 'aa.jpg'

aud = MP3(file, ID3=ID3)    #커버 이미지 넣기
aud.tags.add(
    APIC(                   #https://mutagen.readthedocs.io/en/latest/api/id3_frames.html
        encoding=0,         #0 : LATIN1 / 1 : UTF16 / 2 : UTF16BE / 3 : utf-8
        mime='image/jpg',   #
        type=3,             #cover image    type.txt
        data=open(cover_img, 'rb').read()    #디폴드(r) 일 때 cp949 에러가 생길 수 있음
    )
)
aud.save()