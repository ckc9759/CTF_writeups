### Linux2

```py
You’re in. It’s time to find secrets that may have been hidden. You can use a command to find hidden files and folders.

What is the hidden file that you find?

In Scope: Logged into the SSH machine.

Flag format: XXX{.XXXXXX_XXXXXX.XXX}
```

### Soln :

```py
alien@CX3-IGE:~$ ls
PWN1  PWN2  PWN3  PWN4  PWN5  RE1  level_up.txt
alien@CX3-IGE:~$ ls -a
.  ..  .bash_logout  .bashrc  .profile  .secret_coords.txt  .ssh  PWN1  PWN2  PWN3  PWN4  PWN5  RE1  level_up.txt
alien@CX3-IGE:~$ 
```

#### THE FLAG : IGE{.secret_coords.txt}

---
Thank you
