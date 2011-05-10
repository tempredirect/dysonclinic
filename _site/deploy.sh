#!/bin/bash
#
#  deploy
#
#  Created by  on 2011-05-10.
#  Copyright (c) 2011 Logical Practice Systems Limited. All rights reserved.
#

usage()
{
    echo "./deploy.sh - builds and deploys the site"
    exit 1
}         

quit_on_error()
{
	if [[ "$1" != "0" ]] ; then
		echo "ERROR: $2 error code :$1"
		usage
	fi
}


# build site

jekyll --no-auto

#rm "_site/deploy.sh"

scp -r _site/* root@ec2a.logicalpractice.com:/mnt/www/dysonclinic.co.uk
echo "Fixing persmisions"
ssh root@ec2a.logicalpractice.com -e "chown -R www-data:www-data"
