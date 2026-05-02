<<<<<<< HEAD
﻿## File ini berisi opsi yang dapat di ubah untuk mengkustomisasi game mu.
##
## Baris yang di awali dengan dua 'tanda '#' adalah komentar, dan kamu tidak
## seharusnya menghapus nya. Baris dengan satu '#' adalah kode yang di
## komentari, kamu dapat menghapus tanda '#' jika di butuhkan.    


## Dasar #######################################################################

## Nama game yang dapat dibaca oleh manusia. Ini digunakan untuk menset judul
## jendela, dan juga di tampilkan di antarmuka dan laporan kesalahan. 
##
## Tanda _() yang mengelilingi string menandai itu dapat di terjemahkan.
=======
﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.name = _("PROJECT APSI")


<<<<<<< HEAD
## Meng determinasikan apakah judul yang di berikan di atas di tampilkan di menu
## utama. Set ini ke False untuk menyembunyikan judul.
=======
## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define gui.show_name = True


<<<<<<< HEAD
## Versi Permainan.
=======
## The version of the game.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.version = "1.0"


<<<<<<< HEAD
## Teks yang ditempatkan pada layar tentang game. Tempatkan teks di antara tanda
## kutip tiga, dan biarkan baris kosong di antara paragraf.
=======
## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define gui.about = _p("""
""")


<<<<<<< HEAD
## Nama pendek permainan yang di gunakan untuk executable dan direktori di
## bangunan distribusi. Ini harus hanya berisi karakter ASCII-saja, dan tidak
## boleh mengandung  spasi, koma, atau kutip.
=======
## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define build.name = "PROJECTAPSI"


<<<<<<< HEAD
## Suara dan musik #############################################################

## Ketiga variabel ini mengontrol, antara lain, mixer mana yang ditampilkan
## kepada pemain secara default. Menetapkan salah satu dari variabel ini ke
## False akan menyembunyikan mixer yang sesuai.
=======
## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


<<<<<<< HEAD
## Untuk mengijinkan pengguna memainkan test suara di chanel suara atau musik,
## silahkan hapus tag komentar nya '#' dan set sampel suara untuk di mainkan.
=======
## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


<<<<<<< HEAD
## Silahkan hapus komentar dari baris berikut ini untuk men set file audio yang
## akan di mainkan ketika pemain berada di menu utama. File ini akan terus
## dimainkan sampai permainan di mulai, sampai di hentikan atau file lain di
## mainkan.
=======
## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

# define config.main_menu_music = "main-menu-theme.ogg"


<<<<<<< HEAD
## Transisi ####################################################################
##
## Variabel ini menset transisi yang digunakan ketika event tertentu terjadi.
## Setiap variabel harus di set ke transisi, atau 'None' Untuk mengindikasikan
## bahwa tidak ada transisi yang harus di gunakan.

## Memasuki atau keluar dari menu permainan.
=======
## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.enter_transition = dissolve
define config.exit_transition = dissolve


<<<<<<< HEAD
## Antara layar dari menu permainan
=======
## Between screens of the game menu.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.intra_transition = dissolve


<<<<<<< HEAD
## Transisi yang di gunakan setelah game di load.
=======
## A transition that is used after a game has been loaded.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.after_load_transition = None


<<<<<<< HEAD
## Digunakan ketika memasuki menu utama setelah game berakhir.
=======
## Used when entering the main menu after the game has ended.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.end_game_transition = None


<<<<<<< HEAD
## Variabel untuk menset transisi yang digunakan ketika mulai game tidak
## tersedia. Melainkan, menggunakan pernyataan with setelah menunjukan layar
## tertentu.


## Managemen Jendela ###########################################################
##
## Ini mengendalikan kapan dialog di tampilkan. Jika "show", berarti selalu
## di tampilkan. Juka "hide", berarti itu hanya di tampilkan ketika dialog
## tersedia. jika "auto", jendela di sembunyikan sebelum pernyataan scene dan di
## tunjukkan kembali jika dialog ditampilkan.
##
## Setelah permainan di mulai, ini dapat di ganti dengan pernyataan "window
## show", "window hide", dan "window auto".
=======
## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.window = "auto"


<<<<<<< HEAD
## Transisi yang digunakan untuk menunjukan dan menampilkan jendela dialog
=======
## Transitions used to show and hide the dialogue window
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


<<<<<<< HEAD
## Preferensi defaults #########################################################

## Mengendalikan kecepatan text default. Default nya, 0, ini berarti infiniti,
## Sementara angka yang lain adalah berapa karakter per detik yang akan di
## tampilkan.
=======
## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

default preferences.text_cps = 0


<<<<<<< HEAD
## Delay default otomatis-maju. Nomor yang lebih besar berujung kepada waktu
## menunggu lebih lama, 0 sampai 30 adalah jarak yang valid.
=======
## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

default preferences.afm_time = 15


<<<<<<< HEAD
## Direktori penyimpanan #######################################################
##
## Mengendalikan tempat penyimpanan file save untuk game ini secara spesifik
## untuk setiap platform. File akan di taruh di:
=======
## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
<<<<<<< HEAD
## Ini shearus nya tidak usah di ganti, dan juga iya, harus selalu berisi
## string, bukan expresi.

define config.save_directory = "PROJECTAPSI-1777644971"


## Ikon ########################################################################
##
## Ikon yang di tampilkan di taskbar atau dock.
=======
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "PROJECTAPSI-1777645068"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

define config.window_icon = "gui/window_icon.png"


<<<<<<< HEAD
## Pengaturan Build ############################################################
##
## Bagian ini mengendalikan bagaimana Ren'Py mengubah proyek mu ke file
## distribusi.

init python:

    ## Fungsi berikut mengambil pola file. Pola file merupakan case- insensitiv,
    ## dan sama dengan arah direktori dasar, dengan atau tanpa awalan /. Jika
    ## banyak pola sama, yang pertama yang akan di gunakan.
    ##
    ## Di dalam pola:
    ##
    ## / Ini adlaah
    ##
    ## * mencocokan semua karakter, kecuali pemisah direktori.
    ##
    ## ** mencocokan semua karakter, termasuk pemisah direktori.
    ##
    ## Contohnya, "*.txt" mencocokan file txt di direktori dasar, "game/**.ogg"
    ## matches ogg files in the game directory or any of its subdirectories, and
    ## "**.psd" matches psd files anywhere in the project.

    ## Mengklasifikasi file sebagai None  untuk memisahkannya dari distribusi
    ## build.
=======
## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

<<<<<<< HEAD
    ## Untuk mengarsipkan file, mengklasifikasikannya sebagai 'archive'.
=======
    ## To archive files, classify them as 'archive'.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

<<<<<<< HEAD
    ## Alur Dokumentasi pencocokan file di duplikasikan di build app mac, jadi
    ## mereka tampil di kedua aplikasi dan juga file zip.
=======
    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

    build.documentation('*.html')
    build.documentation('*.txt')


<<<<<<< HEAD
## Kunci lisensi Google Play diperlukan untuk melakukan pembelian dalam
## aplikasi. Kunci ini dapat ditemukan di konsol pengembang Google Play, di
## bawah "Monetisasi" > "Pengaturan Monetisasi" > "Lisensi".
=======
## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

# define build.google_play_key = "..."


<<<<<<< HEAD
## Nama pengguna dan nama proyek yang di asosiasikan dengan proyek itch.io, di
## pisahkan dengan garis miring.
=======
## The username and project name associated with an itch.io project, separated
## by a slash.
>>>>>>> 669da2b5e18f7f944d18d520f501aa9e1a63b7b8

# define build.itch_project = "renpytom/test-project"
