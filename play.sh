#!/bin/bash
ansible-playbook --tag=test site.yml
cat ./files/BR2-CORE.bgp

