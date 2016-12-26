## A panda exercice

This code includes 2 python HTTP services deployed with Vagrant using virtualbox provider ( Ubuntu 14.04 ).
The code is deployed by ANSIBLE and runs on port 8080 and 8090.

You can use the start.py script this way to deploy one of the 2 services ( static or counting ):

<code>
python start.py -d static
</code>


To see the result browse to:

http://localhost:8080 ( or/and 8090 )


