FROM python:3.9-slim
MAINTAINER Roi Ding "dingran@ran-ding.ga"
# 环境变量 权限串
# ENV AUTHORIZATION=XXXX
# ENV SENDKEY=XXX
WORKDIR /usr/yili-carebaby-game

# 修正时区
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y tzdata \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

COPY shuafen.py shuafen.py
COPY jiankong.py jiankong.py
COPY start.sh start.sh


RUN pip install requests &&chmod +x start.sh&& mkdir -p /usr/yili-carebaby-game/logs

CMD ["/usr/yili-carebaby-game/start.sh"]