# locust-performance-test
performance test tools

#Installation
sudo apt-get update
sudo apt-get install -y python-pip
sudo apt-get install -y python-dev
sudo apt-get install -y libzmq-dev
 
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install locustio
pip install pyzmq

#Running
locust -f locust-example.py --host=http://example.com
