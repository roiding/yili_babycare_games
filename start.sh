if [ $AUTHORIZATION ]
then

    python ./shuafen.py $AUTHORIZATION &>./logs/shuafen.log &
    pid1=$!
fi
echo "pid1:${pid1}"

if [ $SENDKEY ]
then
    python ./jiankong.py $SENDKEY &>./logs/jiankong.log &
    pid2=$!
fi
echo "pid2:${pid2}"

while true
do
    if [ -n "${pid1}" -o -d "/proc/${pid1}" ] || [ -n "${pid2}" -o -d "/proc/${pid2}" ]
    then
        sleep 1s
    else
        break
    fi
done