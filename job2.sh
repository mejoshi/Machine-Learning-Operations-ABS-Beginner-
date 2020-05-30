containers=$(docker container ps -qa | wc -w)
images_dml=$(docker image list | grep dml | wc -w)
image_tml=$(docker image list | grep tml | wc -w)

if [ $containers -ge 1 ];then 
	sudo docker stop $(sudo docker container ps -qa)
	sudo docker rm -f $(sudo docker container ps -qa)
fi

if [ $images_dml -ge 1 ];then
	sudo docker rmi -f dml
elif [ $image_tml -ge 1 ];then
	sudo docker rmi -f tml;
else
	echo 'Everthing is clear'
fi
    
    
    
    
#sudo docker rmi -f $(sudo docker image ls -qa)

x=$(sudo grep sklearn /root/ashu/main.py | wc -w)
y=$(sudo grep keras /root/ashu/main.py | wc -w)

if [ $x -ge 1 ];then
		cd /root/ashu/skl/
		sudo docker build /root/ashu/skl -t tml:v1
        echo "traditional ML (SKLEARN)"
        sudo docker run -dit --name tml -v /root/ashu/skl:/sklearn tml:v1
        sudo docker cp dml:/acc.txt /root/ashu/skl
else
		#cd /root/ashu/cnn/
        echo "Latest Approach of ML (TF or Keras) "
        sudo docker build /root/ashu/cnn/ -t dml:v1
        sudo docker run -dit --name dml -v /root/ashu/cnn:/keras dml:v1
        sudo docker cp dml:/acc.txt /root/ashu/cnn
fi

 