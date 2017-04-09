import tuxforms

licenseFile = open("/usr/share/common-licenses/GPL", "r")
licenseText = licenseFile.readlines()
licenseFile.close()
del licenseFile

tuxforms.aboutDialog("Application name", "Description", "", "http://example.com/", "icon", "", "1.0.0", licenseText, ["Author 1", "Author 2"], ["Documenter 1"]);

tuxforms.ShowAll()
