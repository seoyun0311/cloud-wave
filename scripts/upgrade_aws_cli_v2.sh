#!/bin/bash
# aws cli v2 install script
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
export PATH=/usr/local/bin:$PATH
source ~/.bash_profile

# create awscli symbolic link '/usr/bin/aws'
ln -fs /usr/local/bin/aws /usr/bin/aws