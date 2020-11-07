#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show how a TAP query in PyVO works. 

import pyvo

service = pyvo.dal.TAPService ("http://dc.zah.uni-heidelberg.de/tap")
result = service.search ("SELECT TOP 1 * FROM ivoa.obscore")

result.votable.to_xml("votable.vot")

