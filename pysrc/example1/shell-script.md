Looking at what is happening underneath ...

We can use curl to access the web service directly, sending just the LANG and QUERY parameters:
```bash
    curl --get \
        --silent \
        --data-urlencode 'LANG=ADQL' \
        --data-urlencode 'query=SELECT TOP 5 s_ra, s_dec FROM ivoa.obscore' \
        'http://dc.zah.uni-heidelberg.de/tap/sync'
```

Which sends a basic HTTP request:
```
    GET /tap/sync?LANG=ADQL&query=SELECT%20TOP%205%20s_ra%2C%20s_dec%20FROM%20ivoa.obscore HTTP/1.1
    Host: dc.zah.uni-heidelberg.de
    User-Agent: curl/7.69.1
    Accept: */*
```

The server responds with the a VOTable response which contains some metadata describing each of the columns:
```xml
  <FIELD ID="s_ra" datatype="double" name="s_ra" ucd="pos.eq.ra" unit="deg" utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c1">
    <DESCRIPTION>RA of (center of) observation, ICRS</DESCRIPTION>
  </FIELD>
  <FIELD ID="s_dec" datatype="double" name="s_dec" ucd="pos.eq.dec" unit="deg" utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c2">
    <DESCRIPTION>Dec of (center of) observation, ICRS</DESCRIPTION>
  </FIELD>
```

Where the ucd attributes refer to terms in the [UCD](https://ivoa.net/documents/cover/UCD-20050812.html) vocabulary:
```xml
  <FIELD .... ucd="pos.eq.ra">
     ....
  </FIELD>
```

and the utype attributes refer to specific elements defined in the [ObsCore](https://ivoa.net/documents/ObsCore/) data model:
```xml
  <FIELD .... utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c1">
     ....
  </FIELD>
```

Followed by the data encoded as a binary stream:
```xml
   <DATA>
    <BINARY>
      <STREAM encoding="base64">QHYnb1Nr/1dARImFe+0/ykB2J29Ta/9XQESJhXvtP8pAdidvU2v/V0BEiYV77T/KQHYni2aJWrVARIqLuBeqgEB2J4tmiVq1QESKi7gXqoA=</STREAM>
    </BINARY>
   </DATA>
```

PyVO expands the binary stream to extract the data :



