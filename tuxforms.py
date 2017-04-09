# tuxforms.py
# https://github.com/TuxForms/tuxforms
# License: LGPL-3
#
# (C) Elias Ojala 2017
#

# TODO implement subwindow system

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def textDialog(text, title = "", width = 240, height = 240, dialogIcon = "", windowPosition = "none"):
	win = Gtk.Window(title=title, window_position=windowPosition)
	
	win.set_default_size(width, height)
	if(dialogIcon != ""):
		win.set_icon_name(dialogIcon)

	# Add text
	text = win.add( Gtk.Label(text) )



	win.connect("delete-event", Gtk.main_quit) # TODO do like vb6, ability to set "onDeleteEvent" etc...
	win.show_all() # TODO if some attribute is set, do not do this, do in tuxforms.UseWindow() :)

	return win

def aboutDialog(appName, description = "", title = "", website = "", icon = "", dialogIcon = "gtk-info", versionNumber = "", license = "", authors = [], documenters = []):

	# If license's type is 'list', for example if readlines is used, convert it to 'str'
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
		win.set_wrap_license(True) # 
	else:
		print "TODO" # TODO remove license button


	# Handle close button and delete method (like from taskbar or window's X-button)
	def handleButtons(w, res):
		if res == Gtk.ResponseType.CANCEL or res == Gtk.ResponseType.DELETE_EVENT:
			Gtk.main_quit() #TODO
	win.connect("response", handleButtons)
	win.show_all() # TODO if some attribute is set, do not do this, do in tuxforms.UseWindow() :)

	return win

# TODO
def selectFile(selectDirectories = False, multiple = False): # some of the features of this: https://help.gnome.org/users/zenity/stable/file-selection.html.fi
															 # (do not include --save, replace --separator with lists)
															 # https://python-gtk-3-tutorial.readthedocs.io/en/latest/dialogs.html#filechooserdialog
	fileName = False0
	return fileName


def fontChooser(title="fontChooser", windowPosition="center", width = 320, height = 320, dialogIcon = "helloworld"): # Todo
	win = Gtk.FontChooserDialog(title=title, window_position=windowPosition)
	
	win.set_default_size(width, height)
	if(dialogIcon != ""):
		win.set_icon_name(dialogIcon)
	else:
		# default icon
		print "use default icon"

	response = win.run()
	
	# Handle OK button in font chooser, close button and delete method (like from taskbar or window's X-button)
	def deleteWindow():
		win.destroy()
		
	if response == Gtk.ResponseType.CANCEL or response == Gtk.ResponseType.DELETE_EVENT:
		deleteWindow()
		
		return False
	elif response == Gtk.ResponseType.OK:
		fontName = win.get_font()
		
		deleteWindow()
		return fontName
		
def UseWindow(window):
	win.show_all()
	# TODO prevent this to tuxforms.fileSelection() and tuxforms.fontChooser()

def ShowAll():
	Gtk.main()

def Log(logLevel = "Unknown logLevel", logText = "Log Text is undefined"):
	if(type(logLevel).__name__ == "str" and type(logText).__name__ == "str"):
		if(type(logLevel):
		print "TuxForms " + logLevel + " - " + logText
	else:
		if(type(logLevel).__name__ != "str" and type(logText).__name__ == "str"): # logLevel is wrong
			errorMsg = "logLevel isn't 'str'"
		elif(type(logLevel).__name__ == "str" and type(logText).__name__ != "str"): # logText is wrong
			errorMsg = "logText isn't 'str'"
		elif(type(logLevel).__name__ != "str" and type(logText).__name__ != "str"): # logLevel and logText is wrong
			errorMsg = "logLevel & logText aren't 'str'"
		
		print "Tuxforms ERROR - " + errorMsg

	# TODO >> BUG
	# Bug reported by @theel0ja
	#
	#>>> import tuxforms
	#>>> tuxforms.Log(123, "text")
	#Traceback (most recent call last):
	#  File "<stdin>", line 1, in <module>
	#  File "tuxforms.py", line 140, in Log
	#    else:
	#NameError: global name 'loglevel' is not defined
	#>>> 
