#!/bin/bash
# get scores, update standings, update possible points every 5 min
/home/ec2-user/.virtualenvs/madness/bin/python /home/ec2-user/madness/django-march-madness/manage.py update_scores
/home/ec2-user/.virtualenvs/madness/bin/python /home/ec2-user/madness/django-march-madness/manage.py update_standings
/home/ec2-user/.virtualenvs/madness/bin/python /home/ec2-user/madness/django-march-madness/manage.py update_possible_points