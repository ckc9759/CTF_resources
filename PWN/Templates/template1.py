import pwn
import time
import warnings

warnings.filterwarnings(action='ignore',category=BytesWarning)

elf=pwn.ELF("./go2win")
pwn.context.binary=elf
pwn.context.log_level='DEBUG'
pwn.context(terminal=['tmux','split-window','-h'])

libc=elf.libc
p=pwn.remote()
