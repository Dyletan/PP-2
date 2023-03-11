import pygame as pg

songs = [r'lab_7\music\mystery.mp3', r'lab_7\music\subwoofer lullaby.mp3', r"lab_7\music\wii_shop.mp3", r'lab_7\music\bloody stream.mp3']


def set_bg(cur_song):
    cur_image = r"lab_7\bg\minecraftcover.png"
    if cur_song == r'lab_7\music\subwoofer lullaby.mp3':
         cur_image = r"lab_7\bg\minecraftcover.png"
    elif cur_song == r"lab_7\music\wii_shop.mp3":
         cur_image = r"lab_7\bg\wii.png"
    elif cur_song == r'lab_7\music\bloody stream.mp3':
         cur_image = r"C:\PP 2\lab_7\bg\jojo.jpg"
    elif cur_song == r'lab_7\music\mystery.mp3':
         cur_image = r"lab_7\bg\mystery.jpg"
    global bg
    bg = pg.image.load(cur_image)

def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]] # move current song to the back of the list
    set_bg(songs[0])
    pg.mixer.music.load(songs[0])
    pg.mixer.music.play()

def play_prev_song():
    global songs
    songs = [songs[-1]] + songs[:-1]
    print(songs[0])
    set_bg(songs[0])
    pg.mixer.music.load(songs[0])
    pg.mixer.music.play()

done = False



pg.init()
screen = pg.display.set_mode((1100,1000))
done = False
play = True
clock = pg.time.Clock()

SONG_END = pg.USEREVENT + 1

pg.mixer.music.set_endevent(SONG_END)
play_next_song()

while not done:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    play = not play
                elif event.type == SONG_END or (event.type == pg.KEYDOWN and event.key == pg.K_RIGHT):
                    play_next_song()
                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    play_prev_song()
        screen.fill((255, 255, 255))

        if not play:
              pg.mixer.music.pause()
        else:
              pg.mixer.music.unpause()

        screen.blit(bg, (0, 0))

        pg.display.flip()

        clock.tick(60)
