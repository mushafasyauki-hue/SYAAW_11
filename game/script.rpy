<<<<<<< HEAD
﻿# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character("farell")

# Game dimulai disini.
label start:

    scene bg blck with dissolve
    e "Hallo Rehan."

    e "Setelah kamu menambahkan cerita, gambar, dan musik, kamu bisa merilis nya ke dunia!"
=======
﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

    return
