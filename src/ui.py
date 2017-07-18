#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from urllib.request import urlretrieve
from threading import Thread
import hashlib
import os.path

DOWNLOAD_LINK = "https://download-cf.jetbrains.com/cpp/CLion-2017.1.3.tar.gz"
DOWNLOAD_SHA256 = "efb80d5c66db367b6d576923850c56dbb0054f44e0370a274ef37ae2d69ab710"
DOWNLOAD_FILE = "CLion.tar.gz"

class SnapUIWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Downloader")
        self.set_border_width(10)
        self.set_default_size(640, 480)
        self.set_position(Gtk.WindowPosition.CENTER)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "CLion Downloader"
        self.set_titlebar(hb)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(vbox)

        label = Gtk.Label("This tool will download CLion to your computer.")
        label.set_line_wrap(True)
        vbox.pack_start(label, False, True, 10)

        label = Gtk.Label("This is an unofficial CLion snap. For legal reasons "
                          "I can't distribute CLion directly in the snap so this "
                          "tool will download it for you.")
        label.set_line_wrap(True)
        vbox.pack_start(label, False, True, 10)

        button1 = Gtk.LinkButton("https://www.jetbrains.com/clion/", "Read more at jetbrains.com")
        vbox.pack_start(button1, False, True, 0)
        button2 = Gtk.LinkButton("https://github.com/nsg/clion-snap", "Submit an issue or PR")
        vbox.pack_start(button2, False, True, 0)

        button = Gtk.Button.new_with_mnemonic("Download CLion")
        button.connect("clicked", self.on_clicked)
        vbox.pack_start(button, False, True, 40)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 20)

    def on_clicked(self, button):
        self.message("Downloading CLion, the application will start when "
                     "it's done.")
        self.progressbar.set_show_text(True)
        button.hide()
        thread = Thread(target=self.download_thread)
        thread.start()

    def download_thread(self):
        urlretrieve(DOWNLOAD_LINK, DOWNLOAD_FILE, self.reporthook)
        dh = hashlib.sha256(open(DOWNLOAD_FILE, 'rb').read()).hexdigest()
        if dh == DOWNLOAD_SHA256:
            self.message("Checksum matches")
            Gtk.main_quit()
        else:
            self.message("Error: Checksum {} did not match {}".format(dh, DOWNLOAD_SHA256))

    def reporthook(self, blocknum, blocksize, totalsize):
        p = round((blocknum * blocksize) / totalsize, 2)
        self.progressbar.set_fraction(p)

    def message(self, text):
        self.progressbar.set_text(text)
        print(text)

if not os.path.isfile(DOWNLOAD_FILE):
    win = SnapUIWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
