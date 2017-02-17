rebuild:
	docker rmi $(docker images | grep '<none>' | awk '{ print $3; }'); exit 0;
	docker build -t last.fm_to_vk .
	docker rm -f last.fm_to_vk
	docker run -d --name last.fm_to_vk --network=host --restart=always last.fm_to_vk
