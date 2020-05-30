x=$(sudo cat /root/ashu/cnn/acc.txt)
sudo docker start dml

if [ $x -lt 90 ];then
	sudo docker exec dml python3 /levelUp.py
else
	echo 'with large epochs'
fi

sudo docker cp dml:/acc.txt /root/ashu/cnn
y=$(sudo cat /root/ashu/cnn/acc.txt)


if [ $y -lt 90 ];then
	sudo docker exec dml python3 /levelUp2.py
else
	echo 'with large epochs'
fi

sudo docker cp dml:/acc.txt /root/ashu/cnn
z=$(sudo cat /root/ashu/cnn/acc.txt)

if [ $z -lt 90 ];then
	sudo docker exec dml python3 /levelUp3.py
else
	echo 'with large epochs'
    ls
    pwd
fi