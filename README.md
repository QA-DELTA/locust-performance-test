# locust-performance-test
performance test tools

## Installation

`sudo apt-get update`<br />
`sudo apt-get install -y python-pip`<br />
`sudo apt-get install -y python-dev`<br />
`sudo apt-get install -y libzmq-dev`<br />
 
`sudo pip install virtualenv`<br />
`virtualenv venv`<br />
`source venv/bin/activate`<br />
`pip install locustio`<br />
`pip install pyzmq`<br />

## Running

locust -f locust-example.py --host=http://example.com
