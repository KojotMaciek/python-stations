#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'stations');

# ask user

q_name = raw_input("Station Name: ")
q_address = raw_input("Station address: ")
q_location = raw_input("GPS coordinates: ")
q_city = raw_input("City of the station: ")
q_story = raw_input("Story of the station: ")
q_crdata = raw_input("Date of creation(YYYY-MM-DD): ")

with con:
	
	cur = con.cursor()
	cur.execute("set names utf8;")
	cur.execute("INSERT INTO local(name, address, location, city, story, creationdata) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (q_name, q_address, q_location, q_city, q_story, q_crdata))

