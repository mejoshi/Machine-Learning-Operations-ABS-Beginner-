#!/bin/bash

x=$(grep sklearn task3.py | wc -w)
y=$(grep keras task3.py | wc -w)

echo $x
echo $y


if [ $x -ge 1 ];then
	echo "sklearn both will install"
	#cd /cnn
	#docker build .

elif [ $y -ge 1 ];then
	echo "Keras  will install"
else 
	echo "Default will install"
fi