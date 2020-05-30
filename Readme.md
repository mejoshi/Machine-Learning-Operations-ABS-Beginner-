# MLOps

MLOps, which means “Machine Learning Operations” is a development practice similar to DevOps, but built from the ground up for Machine Learning best practices. Just as DevOps looks to provide regular, shorter releases, so too does MLOps look to enhance every step of the ML development lifecycle.

# ABout Task 3 
Whenever someone pushes a machine learning file to GitHub repo, it will start training. After successfully hypothesis trained, if its accuracy is less than 90% than it will try again with some more epochs and more CRP layers. Else it will send an email with accuracy.

# MLOps Task 3
1. Create container image that’s has Python3 and Keras or numpy installed using dockerfile. Jenkins job should detect the code that it is code of ML or DL. When we launch this image, it should automatically starts train the model in the container.

2. Create a job chain of job1, job2, job3 and job4 using build pipeline plugin in Jenkins. 

3. Job1 : Pull the Github repo automatically when some developers push repo to Github, and download that on container. For code

4. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing). For code
[Click Here](/job2.sh)

5. Job3 : Train your model and predict accuracy or metrics. For Code
[Click Here](/job3.sh)

7. Job 4 : If prediction is less than 90% than it will tweak tha machine learning model. Code here 
[Click Here](/job4.sh)

6. Job 5 : Successfull email will send notify developer with model accuracy, code by Email notification.
