#!/usr/bin/python

import argparse
import subprocess
import os
import re

status_response = '(\S+)\s*running \(([^)]+)\)'
machine = "base"
parser = argparse.ArgumentParser(description="Tool for deploying Panda services")
parser.add_argument("--deploy","-d",choices=["static","counting","all"],required="True",help="Choose what to deploy")
args = parser.parse_args()

# Set up the env variable for Vagrant run
os.environ["panda"] = args.deploy

# If the machine already runs we prefer to run provision
# print will occur only after the execution
status=subprocess.check_output('vagrant status', shell=True)
if re.findall(status_response, status):
    print "Already running ...Provisionning.."
    provision = subprocess.check_output('vagrant provision', shell=True)
    print provision
else:
    print "Bringing machine up.."
    up = subprocess.check_output('vagrant up '+ machine, shell=True)
    print up
