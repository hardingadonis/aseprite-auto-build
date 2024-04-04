import requests
import os

ASEPRITE_REPOSITORY = 'aseprite/aseprite'

def get_latest_tag_aseprite():
	response = requests.get(f'https://api.github.com/repos/{ASEPRITE_REPOSITORY}/releases/latest')
	response_json = response.json()
	return response_json['tag_name']

def clone_aseprite(tag):
	clone_url = f'https://github.com/{ASEPRITE_REPOSITORY}.git'
	git_cmd = f'git clone -b {tag} {clone_url} src/aseprite --depth 1'
	os.system(git_cmd)
	os.system('cd src/aseprite && git submodule update --init --recursive')

if __name__ == '__main__':
	tag = get_latest_tag_aseprite()
	clone_aseprite(tag)