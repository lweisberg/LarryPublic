#!/usr/bin/env python
import os
import re


import argparse


if __name__ == '__main__':
#    parser = argparse.ArgumentParser(description="My parser")
    parser = argparse.ArgumentParser()
    parser.add_argument("dir") 
    args = parser.parse_args()
    dir = args.dir
    print  'dir: ' + dir
    pathname = os.getcwd() 
    print 'path is ' + pathname
    print 'getting list in ' + pathname + '/' + dir
    fullpath = os.path.join(pathname, dir)
    for fname in os.listdir(dir ):
    #for fname in os.listdir(fullpath ):
        fullname = os.path.join(dir,fname)
        #fullname = os.path.join(fullpath,fname)
        if os.path.isfile(fullname):
            print fullname
	    m = re.search(r"(.*)([sS]\d+).*([eE]\d+)(.*)", fname)
	    if (m):
	        print m.groups()
	        #print 'mv %s %s' % (fullname, os.path.join(fullpath,m.group(2) + '_' + m.group(3) + '_' +  m.group(1) + m.group(4)))
	        print 'mv %s %s' % (fullname, os.path.join(dir,m.group(2) + '_' + m.group(3) + '_' +  m.group(1) + m.group(4)))
	    else:
	        print 'fname has no reg expr matches'


