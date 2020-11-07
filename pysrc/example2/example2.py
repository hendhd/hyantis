#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show as simple Cone Search

import pyvo

service=pyvo.dal.SCSService("http://vo.km3net.de/ant20_01/nu/cone/scs.xml?")
neutrinos=service.search(pos=(43,35), radius=3)

neutrinos.votable.to_xml("neutrinos.xml")
neutrinos.broadcast_samp("topcat")


