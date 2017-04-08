# tuxforms.py
# https://github.com/TuxForms/ TODO
#
# (C) Elias Ojala 2017
#

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def dialogWithText(text, title = "", ):
    print "Type of window: " + "dialogWithText"
    print "Title: " + title
    print "Text: " + text

    win = Gtk.Window(title=title)
    win.add( Gtk.Label(text) )

    win.connect("delete-event", Gtk.main_quit) # TODO do like vb6, ability to set "onDeleteEvent" etc...
    win.show_all()

def aboutDialog(appName = "Application Name", description = "Description", title = "", website = "", icon = "", dialogIcon = "gtk-info", versionNumber = "", authors = ["foo"], documenters = ["foo"]): # TODO "About" -> "About " + appName ; TODO add gtk.AboutDialog.set_translator_credits?
    #win = Gtk.AboutDialog(transient_for=self.window, modal=True) TODO carify what is "transient_for=self.window

    win = Gtk.AboutDialog(modal=True)

    win.set_program_name(appName)
    if(description != ""):
        win.set_comments(description)
    if(title != ""):
        win.set_title(title) # If title is undefined, GTK uses "About - [Application Name]"
    if(dialogIcon != ""):
        win.set_icon_name(dialogIcon)
    if(icon != ""):
        win.set_logo_icon_name(icon)
    if(website != ""):
        win.set_website(website)
    if(versionNumber != ""):
        win.set_version(versionNumber)

    if(type(authors).__name__ == 'list' and authors):
        win.set_authors(authors)
    else:
        print "TODO" # TODO remove authors button
        win.get_set_wrap_authors = True
    if(type(documenters).__name__ == 'list' and documenters):
        win.set_documenters(documenters)

    win.set_license("License text") # TODO fetch license text from somewhere

    def close(w, res):
        if res == Gtk.ResponseType.CANCEL or res == Gtk.ResponseType.DELETE_EVENT:
            Gtk.main_quit()
    win.connect("response", close)
    win.show_all()

def ShowAll():
    Gtk.main()

