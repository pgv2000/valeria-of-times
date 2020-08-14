class SpriteKindLegacy(Enum):
    Player = 0
    Projectile = 1
    Food = 2
    Enemy = 3

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

pokebola: Sprite = None
game.splash("VALERIONA LA MOLACHA")
tiles.set_tilemap(tiles.create_tilemap(hex("""
            1000100001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
        """),
        [myTiles.transparency16, sprites.castle.tile_grass1],
        TileScale.SIXTEEN))
info.start_countdown(60)
info.set_score(0)
Valeya = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . f f f f . . . . . . . 
            . . . . e 4 4 4 4 e . . . . . . 
            . . . e e 4 f 4 f e e . . . . . 
            . . . e 4 4 4 4 4 4 e . . . . . 
            . . e . f f f f f f . e . . . . 
            . . . f f f 3 3 3 f f . . . . . 
            . f f f f 3 3 3 3 f f f f . . . 
            . . . . f 3 3 3 3 f . . . . . . 
            . . . . f f f f 3 3 . . . . . . 
            . . . . . f . . . f . . . . . . 
            . . . . . f f . f f . . . . . .
    """),
    SpriteKindLegacy.Player)
controller.move_sprite(Valeya)
scene.camera_follow_sprite(Valeya)
music.siren.play()

def on_update_interval():
    global pokebola
    pokebola = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 2 2 . . . . . . . . . 
                    . . . 2 2 2 2 2 . . . . . . . . 
                    . . 2 2 2 f 2 2 2 . . . . . . . 
                    . . f f f 1 f f f . . . . . . . 
                    . . f 1 1 f 1 1 f . . . . . . . 
                    . . . f 1 1 1 f . . . . . . . . 
                    . . . . f f f . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    pokebola.set_position(randint(0, 160), randint(0, 120))
game.on_update_interval(2000, on_update_interval)
