#!/bin/sh

trap closePython SIGTERM


if [ $AUTHORIZATION ]
then

    python ./shuafen.py $AUTHORIZATION &>>./logs/runtime.log &
    pid1=$!
fi
echo "pid1:${pid1}"

if [ $SENDKEY ]
then
    python ./jiankong.py $SENDKEY &>>./logs/runtime.log &
    pid2=$!
fi
echo "pid2:${pid2}"

closePython(){
    if [ -n "${pid1}" -o -d "/proc/${pid1}" ]]
    then
       kill ${pid1}
    fi
    if [ -n "${pid2}" -o -d "/proc/${pid2}" ]]  
    then 
       kill ${pid2}
    fi
}

while true
do  
    
    if [ -n "${pid1}" -o -d "/proc/${pid1}" ] || [ -n "${pid2}" -o -d "/proc/${pid2}" ]
    then
        sleep 1s
    else
        break
    fi
done