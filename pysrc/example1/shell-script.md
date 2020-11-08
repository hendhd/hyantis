We can use curl to access the web service directly, sending just the LANG and QUERY parameters:

    curl --get \
        --silent \
        --data-urlencode 'LANG=ADQL' \
        --data-urlencode 'query=SELECT TOP 5 s_ra, s_dec FROM ivoa.obscore' \
        'http://dc.zah.uni-heidelberg.de/tap/sync'

Which sends a basic HTTP request:

    GET /tap/sync?LANG=ADQL&query=SELECT%20TOP%205%20s_ra%2C%20s_dec%20FROM%20ivoa.obscore HTTP/1.1
    Host: dc.zah.uni-heidelberg.de
    User-Agent: curl/7.69.1
    Accept: */*

The server responds with the a VOTable response:

    <?xml version="1.0" encoding="utf-8"?>
    <VOTABLE xmlns="http://www.ivoa.net/xml/VOTable/v1.3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.4" xsi:schemaLocation="http://www.ivoa.net/xml/VOTable/v1.3 http://vo.ari.uni-heidelberg.de/docs/schemata/VOTable-1.4.xsd">
      <DESCRIPTION>Definition and support code for the ObsCore data model and table.</DESCRIPTION>
      <RESOURCE type="results">
        <INFO name="server" value="http://dc.zah.uni-heidelberg.de"/>
        <INFO name="sql_query" value="SELECT s_ra, s_dec FROM ivoa.obscore LIMIT 5"/>
        <INFO name="query" value="SELECT TOP 5 s_ra, s_dec FROM ivoa.obscore"/>
        <INFO name="src_res" value="Contains traces from resource __system__/obscore">Definition and support code for the ObsCore data model and table.</INFO>
        <INFO name="src_table" value="Contains traces from table ivoa.ObsCore">The IVOA-defined obscore table, containing generic metadata for
    datasets within this datacenter.</INFO>
        <INFO name="QUERY_STATUS" value="OK">Query successful</INFO>
        <INFO name="citation" ucd="meta.bib" value="http://dc.zah.uni-heidelberg.de/tableinfo/ivoa.ObsCore">For advice on how to cite the resource(s) that contributed to this result, see http://dc.zah.uni-heidelberg.de/tableinfo/ivoa.ObsCore</INFO>
        <TABLE name="ObsCore">
          <DESCRIPTION>The IVOA-defined obscore table, containing generic metadata for
    datasets within this datacenter.</DESCRIPTION>
          <FIELD ID="s_ra" datatype="double" name="s_ra" ucd="pos.eq.ra" unit="deg" utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c1">
            <DESCRIPTION>RA of (center of) observation, ICRS</DESCRIPTION>
          </FIELD>
          <FIELD ID="s_dec" datatype="double" name="s_dec" ucd="pos.eq.dec" unit="deg" utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c2">
            <DESCRIPTION>Dec of (center of) observation, ICRS</DESCRIPTION>
          </FIELD>
          <DATA>
            <BINARY>
              <STREAM encoding="base64">QHYnb1Nr/1dARImFe+0/ykB2J29Ta/9XQESJhXvtP8pAdidvU2v/V0BEiYV77T/KQHYni2aJWrVARIqLuBeqgEB2J4tmiVq1QESKi7gXqoA=</STREAM>
            </BINARY>
          </DATA>
        </TABLE>
      </RESOURCE>
    </VOTABLE>




