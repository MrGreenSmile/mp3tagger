import eyed3

aud = eyed3.load('./input/Kenshi Yonezu - Uma to Shika.mp3')
aud.initTag()
aud.tag.title = '馬と鹿'
aud.tag.artist = '米津玄師'
aud.tag.album = '馬と鹿'
aud.tag.album_artist = '米津玄師'
aud.tag.track_num = 1
aud.tag.genre = 'pop'
aud.tag.original_release_date = '2019'
aud.tag.composer = '米津玄師'
aud.tag.save()

print(aud.tag.title)
print(aud.tag.artist)
print(aud.tag.album)
print(aud.tag.album_artist)
print(aud.tag.track_num)
print(aud.tag.genre)
print(aud.tag.original_release_date)