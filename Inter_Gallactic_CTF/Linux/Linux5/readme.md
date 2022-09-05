### Linux5

```py
On the provided SSH server, get the name of the group your user is a part of that stands out.

What’s the name of the group?

In Scope: Logged into the SSH machine.

Flag format: IGE{XXXXXXXXXXX}
```

### Soln :

```py
alien@CX3-IGE:~$ ls 
PWN1  PWN2  PWN3  PWN4  PWN5  RE1  level_up.txt
alien@CX3-IGE:~$ ls -a
.  ..  .bash_logout  .bashrc  .profile  .secret_coords.txt  .ssh  PWN1  PWN2  PWN3  PWN4  PWN5  RE1  level_up.txt
alien@CX3-IGE:~$ /etc/psswd
bash: /etc/psswd: No such file or directory
alien@CX3-IGE:~$ cat /etc/psswd
cat: /etc/psswd: No such file or directory
alien@CX3-IGE:~$ /etc/group
bash: /etc/group: Permission denied
alien@CX3-IGE:~$ groups
alien spaceRogues
alien@CX3-IGE:~$ 
```

#### THE FLAG : IGE{spaceRogues}

---
Thank you
