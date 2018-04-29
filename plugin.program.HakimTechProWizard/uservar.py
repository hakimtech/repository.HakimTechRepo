import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'HakimTech Pro Wizard'
EXCLUDES       = [ADDON_ID, 'repository.HakimTechRepo', 'plugin.program.HakimTechProWizard']
# Text File with build info in it.
BUILDFILE      = 'http://hakimtechnology.com/HakimTech/TextFiles/builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://hakimtechnology.com/HakimTech/TextFiles/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'For YouTube Channel '
YOUTUBEFILE    = 'http://hakimtechnology.com/HakimTech/TextFiles/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://hakimtechnology.com/HakimTech/TextFiles/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://hakimtechnology.com/HakimTech/TextFiles/Advanced.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONMAINT      = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONAPK        = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONADDONS     = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONYOUTUBE    = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONSAVE       = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONTRAKT      = 'http://http://hakimtechnology.com/HakimTech/images/trakt.png'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONCONTACT    = 'http://hakimtechnology.com/HakimTech/images/icon.png'
ICONSETTINGS   = 'http://hakimtechnology.com/HakimTech/images/icon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'Yes'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']HakimTechnology[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing HakimTtechnology.\r\n\r\nContact us on facebook at http://facebook.com'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://hakimtechnology.com/HakimTech/images/icon.png'
CONTACTFANART  = 'http://hakimtechnology.com/HakimTech/images/fanart.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://hakimtechnology.com/HakimTech/TextFiles/autobuilds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.HakimTechRepo'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://hakimtechnology.com/HakimTech/repo/repository.HakimTechRepo/addon.xml'
# Url to folder zip is located in
REPOZIPURL     = 'http://hakimtechnology.com/HakimTech/repo/repository.HakimTechRepo/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://hakimtechnology.com/HakimTech/repo/TextFiles/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'HakimTech Pro Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'http://hakimtechnology.com/HakimTech/images/fanart.jpg'
#########################################################