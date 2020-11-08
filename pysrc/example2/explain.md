Looking at what is happening underneath ...

We can use curl to access the web service directly, sending just the RA, DEC and SR parameters:
```bash
curl --get \
    --silent \
    --data-urlencode 'RA=43' \
    --data-urlencode 'DEC=45' \
    --data-urlencode 'SR=3' \
    'http://vo.km3net.de/ant20_01/nu/cone/scs.xml'
```

Which sends a basic HTTP request to the web service:
```
GET /ant20_01/nu/cone/scs.xml?RA=43&DEC=45&SR=3 HTTP/1.1
Host: vo.km3net.de
User-Agent: curl/7.69.1
Accept: */*
```

The web service responds with a VOTable response containing metadata describing each of the columns
defined in the [Cone Search](https://ivoa.net/documents/cover/ConeSearch-20060908.html) specification.
```xml
<FIELD ID="distCol" datatype="double" name="_r" ucd="pos.distance" unit="deg">
  <DESCRIPTION>Distance to cone center</DESCRIPTION>
</FIELD>
<FIELD ID="MJD" datatype="double" name="MJD" ucd="time.epoch">
  <DESCRIPTION>Modified Julian Day</DESCRIPTION>
</FIELD>
<FIELD ID="Beta" datatype="double" name="Beta" ucd="stat.error">
  <DESCRIPTION>angular error estimate on reconstruction</DESCRIPTION>
</FIELD>
<FIELD ID="Nhit" datatype="int" name="Nhit" ucd="phys.energy">
  <DESCRIPTION>number of light signals in photomultipliers</DESCRIPTION>
</FIELD>
<FIELD ID="RA" datatype="double" name="RA" ref="system" ucd="POS_EQ_RA_MAIN">
  <DESCRIPTION>FK5 equatorial right ascension</DESCRIPTION>
</FIELD>
<FIELD ID="Decl" datatype="double" name="Decl" ref="system" ucd="POS_EQ_DEC_MAIN">
  <DESCRIPTION>FK5 equatorial declination</DESCRIPTION>
</FIELD>
<FIELD ID="ID" arraysize="*" datatype="char" name="ID" ucd="ID_MAIN">
  <DESCRIPTION>Event identifier</DESCRIPTION>
</FIELD>
```

Followed by the data encoded as a binary stream:
```xml
<DATA>
  <BINARY>
    <STREAM encoding="base64">P9U8igtjUWZA6sjLfpD/lz/ZmZmZmZmaAAAALkBFmZmZmZmaQEZZmZmZmZoAAAAHQU5UMTM5NA==</STREAM>
  </BINARY>
</DATA>
```

The PyVO `votable.to_xml` method decodes this binary stream to extract the data :

```xml
<DATA>
  <TABLEDATA>
    <TR>
      <TD>0.836538409016823</TD>
      <TD>55592.169</TD>
      <TD>0.3</TD>
      <TD>48</TD>
      <TD>43.3</TD>
      <TD>35.8</TD>
      <TD>ANT3412</TD>
    </TR>
    <TR>
      <TD>1.94262592664262</TD>
      <TD>57258.5917</TD>
      <TD>0.3</TD>
      <TD>35</TD>
      <TD>43.5</TD>
      <TD>36.9</TD>
      <TD>ANT7402</TD>
    </TR>
    <TR>
      <TD>2.52776479777075</TD>
      <TD>55756.7405</TD>
      <TD>0.5</TD>
      <TD>33</TD>
      <TD>44.5</TD>
      <TD>32.8</TD>
      <TD>ANT3846</TD>
    </TR>
    <TR>
      <TD>2.73187906659559</TD>
      <TD>54500.0934</TD>
      <TD>0.5</TD>
      <TD>64</TD>
      <TD>43.5</TD>
      <TD>32.3</TD>
      <TD>ANT0366</TD>
    </TR>
  </TABLEDATA>
</DATA>
```

