FROM python:3.9-slim
MAINTAINER Roi Ding "dingran@ran-ding.ga"
# 环境变量 权限串
# ENV AUTHORIZATION=XXXX

WORKDIR /usr/yili-carebaby-game
COPY shuafen.py shuafen.py

RUN pip install requests

ENTRYPOINT python ./shuafen.py $AUTHORIZATION