Looking at what is happening underneath ...

We can use curl to access the web service directly, sending the LANG and QUERY parameters defined in the [TAP](https://www.ivoa.net/documents/TAP/) specification:
```bash
curl --get \
    --silent \
    --data-urlencode 'LANG=ADQL' \
    --data-urlencode 'query=SELECT TOP 5 s_ra, s_dec FROM ivoa.obscore' \
    'http://dc.zah.uni-heidelberg.de/tap/sync'
```

Which sends a basic [HTTP GET](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) request to the web service:
```
GET /tap/sync?LANG=ADQL&query=SELECT%20TOP%205%20s_ra%2C%20s_dec%20FROM%20ivoa.obscore HTTP/1.1
Host: dc.zah.uni-heidelberg.de
User-Agent: curl/7.69.1
Accept: */*
```

The web service responds with a [VOTable](https://ivoa.net/documents/VOTable/) response containing metadata describing each of the columns:
```xml
<FIELD ID="s_ra" datatype="double" name="s_ra" ucd="pos.eq.ra" unit="deg" utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c1">
  <DESCRIPTION>RA of (center of) observation, ICRS</DESCRIPTION>
</FIELD>
<FIELD ID="s_dec" datatype="double" name="s_dec" ucd="pos.eq.dec" unit="deg" utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c2">
  <DESCRIPTION>Dec of (center of) observation, ICRS</DESCRIPTION>
</FIELD>
```

Where the ucd attribute refers to terms in the [UCD](https://ivoa.net/documents/cover/UCD-20050812.html) vocabulary:
```xml
<FIELD .... ucd="pos.eq.ra">
```

and the utype attribute refers to specific elements defined in the [ObsCore](https://ivoa.net/documents/ObsCore/) data model:
```xml
<FIELD .... utype="obscore:char.spatialaxis.coverage.location.coord.position2d.value2.c1">
```

Followed by the data encoded as a binary stream:
```xml
<DATA>
  <BINARY>
    <STREAM encoding="base64">QHYnb1Nr/1dARImFe+0/ykB2J29Ta/9XQESJhXvtP8pAdidvU2v/V0BEiYV77T/KQHYni2aJWrVARIqLuBeqgEB2J4tmiVq1QESKi7gXqoA=</STREAM>
  </BINARY>
</DATA>
```

The PyVO `votable.to_xml` method decodes this binary stream to extract the data :

```xml
<DATA>
  <TABLEDATA>
    <TR>
      <TD>354.464679166665</TD>
      <TD>41.074386111111</TD>
    </TR>
    <TR>
      <TD>354.464679166665</TD>
      <TD>41.074386111111</TD>
    </TR>
    <TR>
      <TD>354.464679166665</TD>
      <TD>41.074386111111</TD>
    </TR>
    <TR>
      <TD>354.47153333334</TD>
      <TD>41.082388888889</TD>
    </TR>
    <TR>
      <TD>354.47153333334</TD>
      <TD>41.082388888889</TD>
    </TR>
  </TABLEDATA>
</DATA>
```
