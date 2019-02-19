#!/usr/bin/python

# Support Sonar 7.x (or maybe latest versions) only

import sys
import requests
from datetime import datetime

def main():
    if len(sys.argv) != 5:
        print "Usage: create_with_profile.py <username> <password> <quality profile name> <file with sonar project names>"
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
	quality_profile = sys.argv[3]
    file = sys.argv[4]

    flog = open('log_create.txt', 'w')
    
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            splitted_line = line.split()
            pkey, pname = splitted_line[0], splitted_line[1]
            print(line)
            
            headers = {'content-type': 'application/json'}
            url = 'https://sonar.company.com:8443/api/projects/create'
            params = { 'project' : pkey, 'name': pname }
            r = requests.post(url, params=params, data="", headers=headers, auth=(username, password))
            print(r.status_code)
            print(r.content)
    
            flog.write("create [" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]\n")
            flog.write('Project ' + line + '. Status code: ' + str(r.status_code) + '\n')
            flog.write(r.text + "\n\n")
            
            headers = {'content-type': 'application/json'}
            url = 'https://sonar.company.com:8443/api/qualityprofiles/add_project'
            params = { 'language': 'java', 'projectKey': pkey, 'qualityProfile': quality_profile}
            r = requests.post(url, params=params, data="", headers=headers, auth=(username, password))
            print(r.status_code)
            print(r.content)
            
            flog.write("profile [" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]\n")
            flog.write('Project ' + line + '. Status code: ' + str(r.status_code) + '\n')
            flog.write(r.text + "\n\n")
    flog.close()
    
if __name__ == '__main__':
	main()
