enum SpriteKindLegacy {
    Player,
    Projectile,
    Food,
    Enemy
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    otherSprite.destroy()
})
let pokebola: Sprite = null
game.splash("VALERIONA LA MOLACHA")
tiles.setTilemap(tiles.createTilemap(hex`1000100001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101`, img`
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
    `, [myTiles.transparency16,sprites.castle.tileGrass1], TileScale.Sixteen))
info.startCountdown(60)
info.setScore(0)
let Valeya = sprites.create(img`
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
    `, SpriteKindLegacy.Player)
controller.moveSprite(Valeya)
scene.cameraFollowSprite(Valeya)
music.siren.play()
game.onUpdateInterval(500, function () {
    pokebola = sprites.create(img`
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
        `, SpriteKind.Food)
    pokebola.setPosition(randint(0, 160), randint(0, 120))
})
