import xbmc
import xbmcgui
import time
import os
import socket
import xbmcaddon

print "Starting Car PC Manager"


# Start aditional services
os.system("startx&")

# Make sure Map is hidden behind Navit Menu
os.system("xdotool mousemove 100 100 mousedown 1&")

def CarpcController_SendCommand(command):
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Send request to server
	sock.sendto(command + "\0", (UDP_IP, UDP_PORT))

	sock.close()


while (not xbmc.abortRequested):

	# If Radio is Active and User is trying to play a file switch Radio OFF
	if str(xbmcgui.Window(10000).getProperty('Radio.Active')) == "true" and xbmc.Player().isPlaying():
		CarpcController_SendCommand("system_mode_toggle")
	if str(xbmcgui.Window(10000).getProperty('Volume.Changed'))== "true" :
		settings = xbmcaddon.Addon(id='script.program.tdasettings')
		settings.setSetting('volume',xbmcgui.Window(10000).getProperty('Volume.Value'))

	
	time.sleep(1)