import pylast
import vk
import time
import argparse
import sys

def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-ll', '--last-fm-login', default = None)
	parser.add_argument('-lp', '--last-fm-password', default = None)
	parser.add_argument('-vl', '--vk-login', default = None)
	parser.add_argument('-vp', '--vk-password', default = None)
	parser.add_argument('-s', '--status', default = '')

	return parser

if __name__ == '__main__':
	API_KEY = "bedb9e9f4b1e4a7df1fdf5440ef3f6aa" 
	API_SECRET = "e2496730a8ed87e0579f9ab3d03418e9"

	parser = create_parser()
	namespace = parser.parse_args(sys.argv[1:])

	if not namespace.last_fm_login and not namespace.last_fm_password and not namespace.vk_login and not namespace.vk_password:
		print('You should use all flags!')
		sys.exit()

	session = vk.AuthSession(app_id='4973555', user_login = namespace.vk_login, user_password = namespace.vk_password, scope = 'status')
	vk_api = vk.API(session)

	lastfm_api = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
	    API_SECRET, username = namespace.last_fm_login, password_hash = pylast.md5(namespace.last_fm_password))

	while True:
		curr_status = vk_api.status.get()['text']
		curr_playing = lastfm_api.get_user(namespace.last_fm_login).get_now_playing()
		if curr_playing and curr_status.replace('Слушаю: ', '') != str(curr_playing):
			vk_api.status.set(text = 'Слушаю: ' + str(curr_playing))
		elif not curr_playing and curr_status != namespace.status:
			vk_api.status.set(text = namespace.status)
		time.sleep(0.3)