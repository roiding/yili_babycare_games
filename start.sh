if [ $AUTHORIZATION ]
then

    python ./shuafen.py $AUTHORIZATION >/logs/shuafen.log
    pid1=$!
fi
if [ $SENDKEY ]
then

    python ./jiankong.py $SENDKEY >/logs/jiankong.log
    pid2=$!
fi
while true
do
    if [[(-n "${pid1}" && -d "/proc/${pid1}") ||(-n "${pid2}" && -d "/proc/${pid2}")]]
    then
        sleep 1s
    else
        break
    fi
done