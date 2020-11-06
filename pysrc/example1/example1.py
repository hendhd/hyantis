#! /usr/bin/ python
# -*- coding=utf-8 -*- 

# A demo program to show all-VO data discovery.


from astropy import table
import pyvo

QUERYA = """
SELECT
   TOP 10000
   db.*,tc.*, 
DISTANCE (POINT (db.s_ra, db.s_dec), POINT(tc.RA, tc.Decl)) AS dis
   FROM ivoa.obscore AS db
   JOIN TAP_UPLOAD.t7 AS tc
   ON 1=CONTAINS(POINT('ICRS', db.s_ra, db.s_dec),
                 CIRCLE('ICRS', , tc.Decl, tc.Beta))
AND tc.MJD BETWEEN t_min AND t_max 
"""

QUERY = """
SELECT
   TOP 10000
   db.*,tc.*, 
DISTANCE (POINT (db.s_ra, db.s_dec), POINT(tc.RA, tc.Decl)) AS dis
   FROM ivoa.obscore AS db
WHERE 1=CONTAINS(POINT('ICRS', db.s_ra, db.s_dec),
                 CIRCLE('ICRS', 43, 35, 0.5))
"""


def make_targets_table(objects):
    """returns an astropy table containing main_id, ra, dec from GAVO's
    service providing data on antares neutrinos"""
    svc = pyvo.dal.TAPService("http://dc.zah.uni-heidelberg.de/tap")
    res = svc.run_sync(
    QUERY)
    return res.table


def print_col_stats(col):
    """print a bit of column statistics.
    """
    values = col[~col.mask]
    print("Column {}: {} values".format(col.name, len(values)))
    if not len(values):
        print("  No non-NULL values")

    if col.name=="instrument_name":
        print(textwrap.fill(
            "  Matches from {}".format(
                (b", ".join(set(values))).decode("utf-8")),
            subsequent_indent="    "))
    elif col.name=="access_url":
        pass # URL statistics?  Ah well...
    else:
        print("  Min {:4g}, Max {:4g}, Mean {:4g}".format(
            values.min(), values.max(), values.mean()))
    print("---")


def obtain_image_meta(objects):
    """runs an all VO search for positions of interest
    """
    targets_table = make_targets_table(objects)
    
    results = []
    for svc_rec in pyvo.registry.search(datamodel="obscore"):
        print("Querying {}".format(svc_rec.res_title))
        try:
            svc = pyvo.dal.TAPService(svc_rec.access_url)
            results.append(
                svc.run_sync(QUERY, uploads={"myobjs": targets_table}).table)
        except KeyboardInterrupt:
            # someone lost their patience with a service.  Query next.
            pass
        except Exception as msg:
            # some service is broken; you *should* complain, but
            # then let's be lazy here
            print("  Broken: {} ({})\n".format(
                svc_rec.access_url, msg))
        
    
    return table.vstack(results)


def main():
    if True: # get results from the net
        matches = obtain_image_meta(
            ['Einstein Cross', 'QSO B1803+6737', 'HE 1104-1805'])

        with open("allmatches.vot", "wb") as f:
            matches.write(f, format="votable")

    else:  # use cached results (for development, say)
        with open("allmatches.vot", "rb") as f:
            matches = table.Table.read(f)
    
    for col_name in matches.columns:
        print_col_stats(matches[col_name])
        
	
if __name__=="__main__":
    main()

# vi:et:sw=4:sta
