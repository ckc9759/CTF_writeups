### Chall Desc : Pretty Good Privacy

```py
The Bentlys recently received files in their email from an unknown source.   
They checked to see if there was anything suspicious, 
but all they found was encrypted text.  
Use the following two files to see the message.

Are you able to decrypt their message and retrieve the flag?

Flag format: IGE{XXX_XX_XXXXXX_XXXX}

Credit: Byrch B.
```

---

### Soln : 

I simply used the pre-installed gpg software in Kali Linux Vm. 

The challenge name also directed us to something like gpg or pgp including the file extension.


```bash
──(ckc9759㉿Kali)-[~/Desktop]
└─$ gpg --import private.asc
gpg: key BCA2845189B5BACD: "Jeff Bez0z" not changed
gpg: key BCA2845189B5BACD: secret key imported
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:  secret keys unchanged: 1
                                                                                                                                                                                                                                           
┌──(ckc9759㉿Kali)-[~/Desktop]
└─$ gpg --decrypt data.gpg  
gpg: encrypted with 255-bit ECDH key, ID 368A41834CC66C87, created 2022-06-19
      "Jeff Bez0z"
IGE{gPg_1s_pR31ty_c0ol}gpg: Signature made Sat 18 Jun 2022 08:17:35 PM EDT
gpg:                using EDDSA key 24EAF1B082F96F215D273039BCA2845189B5BACD
gpg: Good signature from "Jeff Bez0z" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 24EA F1B0 82F9 6F21 5D27  3039 BCA2 8451 89B5 BACD
```

#### THE FLAG : IGE{gPg_1s_pR31ty_c0ol}

---

Thank you
