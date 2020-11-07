#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show all-VO data discovery.

import pyvo
from astropy.table import Table



QUERY="""
SELECT
   TOP 10
   *
   FROM ivoa.obscore AS db
   JOIN TAP_UPLOAD.lt AS tc
   ON 1=CONTAINS(POINT('ICRS', db.s_ra, db.s_dec),
                 CIRCLE('ICRS', tc.RA, tc.Decl, Beta))
"""

def search_obscsvc(services, lt):
  for row in services:
    try:

      print ("Querying {url}".format(url=row.access_url))

      service=pyvo.dal.TAPService(row.access_url)
    
      result=service.run_async(query=QUERY, uploads={"lt":lt})
    
      result.broadcast_samp("topcat")

    except KeyboardInterrupt:
      # someone lost their patience with a service.  Query next.
      pass
    except Exception as msg:
     # some service is broken; you *should* complain, but
     # then let's be lazy here
     print("  Broken: {} ({})\n".format(row.access_url, msg))


def search_ssvc(svcurl, lt):
  try:
    service=pyvo.dal.TAPService(svcurl)
    result=service.run_async(query=QUERY, uploads={"lt":lt})
    result.broadcast_samp("topcat")
  except KeyboardInterrupt:
      # someone lost their patience with a service.  Query next.
    pass
  except Exception as msg:
    # some service is broken; you *should* complain, but
    # then let's be lazy here
    print("  Broken: {} ({})\n".format(svcurl, msg))


def main():
  # get local neutrino data
  lt = Table.read('neutrinos.xml', format='votable')
  print (lt)

  # Search the registry and save the result

  obsvc=pyvo.registry.search(datamodel="obscore")
  obsvc.votable.to_xml("obscore_services.xml")

  search_obscsvc(obsvc, lt)
#  search_ssvc("http://dc.zah.uni-heidelberg.de/tap", lt)

	
if __name__=="__main__":
    main()



