#!/usr/bin/python
"""  Python script to run all the things. """
import config

def main ():
   setup()

   while True:
      print ("Main")

def setup ():
   print("Setup")
   config.config()

main()
