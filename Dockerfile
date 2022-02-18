FROM python:3.9-slim
MAINTAINER Roi Ding "dingran@ran-ding.ga"
# 环境变量 权限串
# ENV AUTHORIZATION=XXXX

WORKDIR /usr/yili-carebaby-game

COPY shuafen.py shuafen.py
COPY jiankong.py jiankong.py
COPY start.sh /start.sh

RUN pip install requests && chmod +x /start.sh

ENTRYPOINT /start.sh