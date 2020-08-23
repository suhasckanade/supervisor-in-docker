# Using supervisor

Using supervisor process control in docker to trigger & manage multiple processes. 

After deploying the docker, run below command to check whether processes are running or not.

tail -f /home/docker-supervisorctl/process.log 

Sample output is like...

process-1.py: Running since seconds 0
process-2.py: Running since seconds 0
process-3.py: Running since seconds 1
process-1.py: Running since seconds 3
process-2.py: Running since seconds 3
process-3.py: Running since seconds 4