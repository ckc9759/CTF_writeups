### Linux 

```py
The first step in looking around a terminal you stumble upon in the wild is actually connecting to it! 
So, adventurer, it is time to connect up and dive into this box so we can start to get some intel. Let’s go!

Log into this machine using ssh with the credentials below:

IP address: 64.227.11.108 User: alien Password: Intergalactic2022

Flag format: XXX{XXXXXXXXXX_XXXXXXXXX}
```

### Soln : 

```py
┌──(ckc9759㉿Kali)-[~/Desktop]
└─$ ssh alien@64.227.11.108    
alien@64.227.11.108's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-125-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Sep  5 14:21:01 UTC 2022

  System load:  0.07               Users logged in:          2
  Usage of /:   35.1% of 24.05GB   IPv4 address for docker0: 172.17.0.1
  Memory usage: 69%                IPv4 address for eth0:    64.227.11.108
  Swap usage:   0%                 IPv4 address for eth0:    10.10.0.5
  Processes:    506                IPv4 address for eth1:    10.116.0.2

0 updates can be applied immediately.

New release '22.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Could not chdir to home directory /home/alien: No such file or directory
Sanity Check Flag: IGE{Conn3ction_Succ3sful}
alien@CX3-IGE:~$ 
```

---
Thank you
