# Import tuxforms library
import tuxforms

# Load GPL-3 license from /usr/share/common-licenses/GPL-3
licenseFile = open("/usr/share/common-licenses/GPL-3", "r")
licenseText = licenseFile.readlines()
licenseFile.close()
del licenseFile

# Make about dialog
tuxforms.aboutDialog("Application name", "Description", "", "http://example.com/", "icon", "", "1.0.0", licenseText, ["Author 1", "Author 2"], ["Documenter 1"]);

# Show all windows
tuxforms.ShowAll()
