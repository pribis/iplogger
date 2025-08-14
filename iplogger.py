#iplogger - A simple program to keep a running count of
#ip from your access.log. I created this to help me identify
#potential hacking or bot abuse.
#
#Use at your own risk.
#
#Covered under the GNU GPL (v3)
#

import time
from typing import Iterator
import re

access_log = '/var/www/boxcar/logs/access.log'

flush_limit = 1000 #At what point do we initiate a flush. Based on len(ip array). Prevents resource issues.

ignore = ['66.108.141.252','24.185.40.181','172.97.96.178']

def follow(file, sleep_sec=1) -> Iterator[str]:
    """ Yield each line from a file as they are written.
    `sleep_sec` is the time to sleep after empty reads. """
    line = ''
    
    while True:
        tmp = file.readline()
        if tmp is not None and tmp != "":
            line += tmp
            if line.endswith("\n"):
                yield line
                line = ''
        elif sleep_sec:
            time.sleep(sleep_sec)

def main():
    u_ip = {}
    last_key = ''
    last_val = 0
    with open(access_log, 'r') as file:
        file.seek(0, 2)
        for line in follow(file):

            line = re.search('\d+\.\d+\.\d+\.\d+', line)

            if line[0]  in ignore:
                continue
            
            if line[0].strip() not in u_ip:
                u_ip[line[0]] = 1
                
            else:
                u_ip[line[0]] += 1

            print(f'{line[0]}: {u_ip[line[0]]}')                
            if len(u_ip) > flush_limit:
                print(f'Flushing {len(u_ip)}')
                u_ip = {}

            time.sleep(0.1)


if __name__ == '__main__':
    main()
