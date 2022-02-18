if [ $AUTHORIZATION ];then
python ./shuafen.py $AUTHORIZATION >./logs/shuafen.log
if [$SENDKEY];then
python ./jiankong.py $SENDKEY >./logs/jiankong.log