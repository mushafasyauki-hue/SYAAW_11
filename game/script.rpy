# Kamu dapat taruh script game mu di file ini.

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


    return
