### Chall Desc : 

I convert plain text to cipher text by using Cryptocode library . Always Remember BDSEC is a KEY .

Attachments

[cipher.txt](c.txt)

### Soln :

After some research, we find out that cryptocode is a python library.

We will install it using `pip install cryptocode` and then use it to write python script.

```py
>>> import cryptocode
>>> c="c00EtfL9GPq2EItQrkFyPKIMfVFZy0O4ssXtr/V2Io7NMbNS*Brue6Cex4JuWkWU0lUEK2w==*f8EsezuHu2WBstRDlWZiLg==*CZ/4FNMavWZu3kznPrAyeg=="
>>> d=cryptocode.decrypt(c,"BDSEC")
>>> print(d)
BDSEC{cryp70_and_pyth0n_ar3_aw3s0me}
```

### THE FLAG : BDSEC{cryp70_and_pyth0n_ar3_aw3s0me}

Thank you
