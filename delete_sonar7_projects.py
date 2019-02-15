#!/usr/bin/python

import sys
import requests
from datetime import datetime

def main():
    if len(sys.argv) != 4:
        print "Usage: delete_sonar_projects.py <username> <password> <file with sonar project names>"
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    file = sys.argv[3]

    flog = open('log_7.txt', 'w')
    
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            print(line)
            
            headers = {'content-type': 'application/json'}
            url = 'https://sonar.company.com:8443/api/projects/bulk_delete'
            params = { 'projects' : line }
            r = requests.post(url, params=params, data="", headers=headers, auth=(username, password))
            print(r.status_code)
    
            flog.write("[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]\n")
            flog.write('Project ' + line + '. Status code: ' + str(r.status_code) + '\n')
            flog.write(r.text + "\n\n")
    flog.close()
    
if __name__ == '__main__':
	main()
