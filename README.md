# CI_CD_Pipeline_Tool


its for creating tool which monitor and deploys new code changes
Building CI-CD Pipeline Tool Create a complete CI-CD pipeline using bash, python and crontabs. The list of tasks is specified below: Task 1: Set Up a Simple HTML Project Create a simple HTML project and push it to a GitHub repository. Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx Task 3: Write a Python Script to Check for New Commits Create a Python script to check for new commits using the GitHub API. Task 4: Write a Bash Script to Deploy the Code Create a bash script to clone the latest code and restart Nginx. Task 5: Set Up a Cron Job to Run the Python Script Create a cron job to run the Python script at regular intervals. Task 6: Test the Setup Make a new commit to the GitHub repository and check that the changes are automatically deployed. Submission Instructions: To submit your programs, please follow these guidelines:
•	Ensure that your programs are fully completed.
•	Push your code to a GitHub repository.
•	Share the repository link by including it in a text, Word, or PDF file format. Submit the file/text containing the repository link via VLearn.
________________________________________
Solution
1.	Launched a amazon linux 2023 instance, security group to allow all traffic my IP address, and ssh into the server
2.	change to root user and then updated the OS and softwares
sudo -i yum upgrade && yum update
3.	installed git, nginx, wget and also unzip
yum install git nginx wget unzip -y
4.	cloned the repo
git clone git@github.com:CharismaticOwl/ci-cd--herovired-1.git
5.	created ssh private key and public key, added the public key to git repo settings
6.	added te config file in ~/.ssh to add connection
HOST github.com user git identityfile ~/.ssh/private_key
7.	Changed the file permission for config file to 400
chmod 400 ~/.ssh/config
8.	tested the git connection
ssh -T git@github.com
9)cd into the folder that was cloned
cd /root/ci-cd--herovired-1
10.	unzip the template file
unzip ./2117_infinite_loop.zip
11.	before copying the files to nginx, we will start and check the status of nginx
systemctl start nginx systemctl enable nginx systemctl status nginx
13.	copy the files in the template folder and move them to /usr/local/nginx/html/
cp -r /root/ci-cd--herovired-1/2117_infinite_loop/* /usr/local/nginx/html/
14.	restart nginx
systemctl restart nginx
15.	check if the website did host on the public address for the server
http://public_address:80
port 80 is not required as it will be default
16.	now we will write a python program to fetch the latest sha/hashcode for the commit using github API
https://api.github.com/repos/owner/reponame/commits
compare the sha/hash code of the local repo, if the remote sha is changed then it will trigger a shell script to so git pull and update the local repo, and copy the new files to nginx html ocation
17.	Files created for python - git.py
18.	shell script created to get the latest hash for the local repo - getcurrenthash.sh
19.	shell script to update the local repo, and copy the file to ninx folder, and then restart the nginx service.
20.	Once this was tested, added the python script to crontab -e, so that it can run everytime
	/usr/local/python3 /root/git.py
21.	This completes the project, this was well tested.
