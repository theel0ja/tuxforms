# tuxforms.py
# https://github.com/TuxForms/tuxforms
# License: LGPL-3
#
# (C) Elias Ojala 2017
#

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def textDialog(text, title = "", width = 240, height = 240, dialogIcon = "", windowPosition = "none"):
    win = Gtk.Window(title=title, window_position=windowPosition)
    
    win.set_default_size(width, height)
    if(dialogIcon != ""):
        win.set_icon_name(dialogIcon)

    # Add text
    win.add( Gtk.Label(text) )



    win.connect("delete-event", Gtk.main_quit) # TODO do like vb6, ability to set "onDeleteEvent" etc...
    win.show_all()

def aboutDialog(appName, description = "", title = "", website = "", icon = "", dialogIcon = "gtk-info", versionNumber = "", license = "", authors = [], documenters = ["bar"]): # TODO add gtk.AboutDialog.set_translator_credits?

    # If license's type is 'list', for example if readlines is used
    if(type(license).__name__ == 'list'):
        newLicense = ""

        for licenseLine in license:
            newLicense += licenseLine

        license = newLicense
        del newLicense

    #win = Gtk.AboutDialog(transient_for=self.window, modal=True) TODO clarify what is "transient_for=self.window

    win = Gtk.AboutDialog(modal=True)

    win.set_program_name(appName)

    if(description != ""):
        win.set_comments(description)
    if(title != ""):
        win.set_title(title) # If title is undefined, GTK uses "About - [Application Name]"
    if(dialogIcon != ""):
        win.set_icon_name(dialogIcon)
    else:
        win.set_icon_name("gtk-info")
    if(icon != ""):
        win.set_logo_icon_name(icon)
    if(website != ""):
        win.set_website(website)
    if(versionNumber != ""):
        win.set_version(versionNumber)


    hideAuthorsBtn = 1
    # AUTHORS
    if(type(authors).__name__ == 'list' and authors):
        win.set_authors(authors)
        hideAuthorsBtn = 0

    # DOCUMENTERS
    if(type(documenters).__name__ == 'list' and documenters):
        win.set_documenters(documenters)
        hideAuthorsBtn = 0

    if(hideAuthorsBtn == 1):
        print "TODO" # TODO remove authors button

    # LICENSE
    if(license != ""):
        win.set_license(license)
    else:
        print "TODO" # TODO remove license button


    # Handle close button and delete method (like from taskbar or window's X-button)
    def closeWindow(w, res):
        if res == Gtk.ResponseType.CANCEL or res == Gtk.ResponseType.DELETE_EVENT:
            Gtk.main_quit()
    win.connect("response", closeWindow)
    win.show_all()

def ShowAll():
    Gtk.main()

