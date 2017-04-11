# Import tuxforms library
import tuxforms

# Make text dialog
font = tuxforms.fontChooser()

# Make text dialog with font name, if font isn't False; If font is False, do not show anything, but log
if(type(font).__name__ == "str"):
	tuxforms.textDialog(text="Font name: %s" % font)
	tuxforms.ShowAll()
else:
	tuxforms.Log("warning", "User closed dialog or clicked \"Close\" button")
	
	tuxforms.messageDialog(text="User closed dialog or clicked \"Close\" button", messageType="warning")
	tuxforms.Showall()
