#!/usr/bin/env python3
# zipfile pass cracker using bruteforce

# loading imports
from termcolor import colored
import zipfile
import threading
import sys
import optparse


# function module to handle the pass crackin logic
def extractPass(zFile, passwd):
  try:
    
    zFile.extractall(pwd=passwd)
    print(f"{colored('[+] Password Found','green')} : {passwd} ")
    sys.exit()
    
  except:
    print(f"{colored('[-] Invalid Password','red')} : {passwd} ")
  
  
# main function to initiate the cracking process
def main():
  parser = optparse.OptionParser(f"Usage: {sys.argv[0]} -f <zip file> -d <dictionary file> \n\n {colored('By Peter Nyando --> www.github.com/anomalous254','blue')}")
  parser.add_option('-f', dest='zipfile', type='string', help='specify zip file')
  parser.add_option('-d', dest='dictionaryFile', type='string', help='specify dictionary file')
  (options, args) = parser.parse_args()

  if options.zipfile == None or options.dictionaryFile == None:
    print(parser.usage)
    sys.exit()
  else:
    zname = options.zipfile
    dname = options.dictionaryFile
  # instantiatig the zipfile from zipfile class
  zFile = zipfile.ZipFile(zname)
  # opening the dictionary file contaiig the test passwords
  passwords = open(dname)
  # iterating the passwords to check for validy from the crack 
  for password in passwords.readlines():
    passwd = password.strip('\n')
    t = threading.Thread(target=extractPass, args=(zFile, passwd))
    t.start()
    
  

if __name__ == '__main__':
  main()