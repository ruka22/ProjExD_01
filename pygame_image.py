import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    kk_img = pg.transform.flip(pg.image.load("ex01-20230418/fig/3.png"),True,False)
    kk_imgs = [kk_img, \
               pg.transform.rotozoom(kk_img,0.5,1.0), pg.transform.rotozoom(kk_img,1,1.0), \
               pg.transform.rotozoom(kk_img,1.5,1.0), pg.transform.rotozoom(kk_img,2,1.0), \
               pg.transform.rotozoom(kk_img,2.5,1.0), pg.transform.rotozoom(kk_img,3,1.0), \
               pg.transform.rotozoom(kk_img,3.5,1.0), pg.transform.rotozoom(kk_img,4,1.0), \
               pg.transform.rotozoom(kk_img,4.5,1.0), pg.transform.rotozoom(kk_img,5,1.0), \
               pg.transform.rotozoom(kk_img,5.5,1.0), pg.transform.rotozoom(kk_img,5,1.0), \
               pg.transform.rotozoom(kk_img,4.5,1.0), pg.transform.rotozoom(kk_img,4,1.0), \
               pg.transform.rotozoom(kk_img,3.5,1.0), pg.transform.rotozoom(kk_img,3,1.0), \
               pg.transform.rotozoom(kk_img,2.5,1.0), pg.transform.rotozoom(kk_img,2,1.0), \
               pg.transform.rotozoom(kk_img,1.5,1.0), pg.transform.rotozoom(kk_img,1,1.0), \
               pg.transform.rotozoom(kk_img,0.5,1.0)] 

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False), [1600-x, 0])
        screen.blit(bg_img,[3200-x,0])

        n = tmr % 22
        screen.blit(kk_imgs[n],[300,200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()