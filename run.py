import pylast
import vk
import time

API_KEY = "bedb9e9f4b1e4a7df1fdf5440ef3f6aa" 
API_SECRET = "e2496730a8ed87e0579f9ab3d03418e9"
VK_LOGIN = ''
VK_PASS = ''

username = ""
password_hash = pylast.md5("")

session = vk.AuthSession(app_id='4973555', user_login = VK_LOGIN, user_password = VK_PASS, scope = 'status')
vk_api = vk.API(session)

lastfm_api = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
    API_SECRET, username = username, password_hash = password_hash)

while True:
	if lastfm_api.get_user('ngalayko').get_now_playing():
		vk_api.status.set(text = 'Слушаю: ' + lastfm_api.get_user('ngalayko').get_now_playing())
	else:
		vk_api.status.set(text = 'Fuck it, Dude. Let\'s go bowling.')
	time.sleep(10)