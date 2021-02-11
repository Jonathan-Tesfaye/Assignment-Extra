def on_countdown_end():
    if info.score() > 0:
        game.over(True)
    else:
        game.over(False)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    music.zapped.play()
    mySprite.start_effect(effects.rings, 200)
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile2: Sprite = None
mySprite: Sprite = None
music.play_melody("E D G F B A C5 B ", 120)
info.set_life(3)
scene.set_background_color(3)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . 
            . . . f f f f f f . . . 
            . f f f e e e e e f . . 
            f f f e e e e e e e f . 
            f f f f e e e e e e e f 
            f f f f f e e e 4 e e f 
            f f f f e e e 4 4 e e f 
            f f f f 4 4 4 4 4 e f f 
            f f 4 e 4 f f 4 4 e f . 
            f f 4 d 4 d d d d f . . 
            . f f f 4 d d b b f . . 
            . 4 d d e 4 4 4 e f . . 
            . e d d e 1 1 1 1 f . . 
            . f e e f 6 6 6 6 f f . 
            . f f f f f f f f f f . 
            . . f f . . . f f f . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
scene.camera_follow_sprite(mySprite)
info.start_countdown(20)
info.set_score(100)

def on_update_interval():
    global projectile2
    projectile2 = sprites.create_projectile_from_side(img("""
            ..............bbbbbbb...........
                    ...........bb66663333baa........
                    .........bb3367776333663aa......
                    ........b33333888333389633aa....
                    .......b3333333333333389633aa...
                    ......b34443333333333338633bae..
                    .....b3455433333333334443333ae..
                    ....b33322333dddd3333455233daee.
                    ...b3d333333dd3bbbb33322333dabe.
                    ..b3d333333d3bb33bb33333333da4e.
                    ..bd33333333b33aab3333333223a4ee
                    .b3d3663333b33aab33366332442b4ee
                    .bd3b983333a3aa3333387633ee3b4ee
                    .bd6983333baaa333333387633bb4bee
                    b3d6833333bba333333333863ba44ebe
                    bdd3333333bb3333333333333a44bebe
                    add666633333322333366333ba44bbbe
                    ad67776333332442336983d3a444b4e.
                    add888b333333ee3369833d3a44b44e.
                    add333333333333336833d3a444b4e..
                    a3dd3333344433333dddd3a444b44e..
                    ab33ddd325543333dd33aa444b44e...
                    .eabb3dd32233333baaa4444b44e....
                    .ebabb3d333d33baa444443b44e.....
                    ..ebaab3ddd3aaa4444433b44e......
                    ..eebbaab33a44444333b444e.......
                    ...eeebbaab444b333b4444e........
                    ....ebeeebbbbbbbb4444ee.........
                    .....eebbbb44444444ee...........
                    .......eeebbb444eee.............
                    ..........eeeeee................
                    ................................
        """),
        randint(-100, 100),
        randint(-100, 100))
game.on_update_interval(100, on_update_interval)
