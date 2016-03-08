#!/usr/bin/env bash
mkdir -p /tmp/letsencrypt-auto
/home/ec2-user/letsencrypt/letsencrypt-auto certonly -a webroot --agree-tos  --rsa-key-size=4096 --renew-by-default --webroot-path=/tmp/letsencrypt-auto -d madness.novoconstruction.com
sudo /etc/init.d/nginx reload

#git clone https://github.com/letsencrypt/letsencrypt

# Make sure this is added to nginx.conf
#location ~ .well-known/acme-challenge/ {
#  root /tmp/letsencrypt-auto;
#  default_type text/plain;
#}
