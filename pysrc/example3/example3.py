#! /usr/bin/ python
# -*- coding=utf-8 -*- 

from astropy.table import Table
import pyvo

QUERY="""
SELECT
   TOP 10
   *
   FROM ivoa.obscore AS db
   JOIN TAP_UPLOAD.lt AS tc
   ON 1=CONTAINS(POINT('ICRS', db.s_ra, db.s_dec),
                 CIRCLE('ICRS', tc.RA, tc.Decl, tc.Beta))
   AND db.dataproduct_type='image'
"""

# Try to load neutrino file from example2 
try:
  lt = Table.read('../example2/neutrinos.xml', format='votable')

# Or get the fallback file
except: 
  lt = Table.read('fallback.xml', format='votable')

# Make Service Object
service = pyvo.dal.TAPService ("http://dc.zah.uni-heidelberg.de/tap")

# Run Search on obscore table on the GAVO dc
result = service.run_async(query=QUERY, uploads={"lt":lt})
 
# Send resulting table to Topcat via SAMP
result.broadcast_samp("topcat")




