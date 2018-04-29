# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: SkymashiTV
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.HakimTechTV'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCQzzMG7WZntIrZgdlhiNRXw"   #TBE BOXING
YOUTUBE_CHANNEL_ID_2 = "UCYNBd5tm6AHEsJy_8FFohlw"   #NILE VALLEY RADIO
YOUTUBE_CHANNEL_ID_3 = "UCCj1JjAHEw22k1ipG029-Ug"   #AFRICAN HOLLYWOOD


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="TBE BOXING",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-CIO1Jgwu6jg/AAAAAAAAAAI/AAAAAAAAAAA/nAZ8u_OUBPA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="https://i.ytimg.com/vi/hWDIguddcd8/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLB_Zz_tx3_9aV2BHNpF0DQzqIOfWg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NILE VALLEY RADIO",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-pzrg83y9x4Q/AAAAAAAAAAI/AAAAAAAAAAA/xvRrTkpYKHo/s176-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="https://lh3.googleusercontent.com/-wwYbftz3P-I/VoE1NUVmq2I/AAAAAAAAAgI/5ttSmqF73EA/w530-h607-p/12184191_908525449183585_278060795567416208_o.jpg",
        folder=True )

     #action="", 
        title="AFRICAN HOLLYWOOD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-BKvrXkpU1-A/AAAAAAAAAAI/AAAAAAAAAAA/5GAGhQSebjY/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",
        fanart="https://lh3.googleusercontent.com/wpw_twvZlabX3HG_d-tG6-GolMLosKN4uD7lHRewzVHbknk42QroDZbshEtJKrmvXyxK=h310",
        folder=True )

		
run()
