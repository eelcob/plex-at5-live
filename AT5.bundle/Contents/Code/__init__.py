# -*- coding: utf-8 -*-
import os
from string import ascii_uppercase

PLUGIN_TITLE   = 'AT5 Live'

ART            = 'art-at5.jpg'
ICON           = 'icon-default.png'
ICON_SEARCH    = 'icon-search.png'
ICON_PREFS     = 'icon-prefs.png'

base			= 'http://www.at5.nl'
uzgurl			= base + '/live'
streamserver 	= 'rtmp://82.94.228.203/live/'
clip 			= 'live1\.stream'
art				= 'art-at5.png',
icon			= 'icon-at5.png'


###################################################################################################
def Start():
	Plugin.AddPrefixHandler('/video/at5live', MainMenu, PLUGIN_TITLE, ICON, ART)
	Plugin.AddViewGroup('List', viewMode='List', mediaType='items')
	Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')
  
	MediaContainer.title1 = PLUGIN_TITLE
	MediaContainer.viewGroup = 'InfoList'
	MediaContainer.art = R(ART)
  
	DirectoryItem.thumb = R(ICON)
	WebVideoItem.thumb = R(ICON)
	VideoItem.thumb = R(ICON)

	HTTP.CacheTime = 300
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0'

###################################################################################################
def MainMenu():
	dir = MediaContainer()
	dir.Append(Function(VideoItem(PlayVideo, title='AT5 Live')))

	return dir

###################################################################################################
def PlayVideo(sender):
	playclip = 'mp4:' + clip
	Log.Debug(streamserver + playclip)
	return Redirect(RTMPVideoURL(streamserver, playclip, live='true'))