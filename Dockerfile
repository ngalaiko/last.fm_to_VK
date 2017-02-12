FROM python:3.5.3

ADD . /root/last.fm_to_VK

WORKDIR /root/last.fm_to_VK

RUN pip3 install -r ./requirements.txt

RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
