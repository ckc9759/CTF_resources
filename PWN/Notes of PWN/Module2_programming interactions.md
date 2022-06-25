### Notes:

---

### Interactions with programs:

* Linux command line
  * It is also known as `shell`.
  * You type a command and the system executes it showing the output. Example cat flag.txt

* Processes
  * A process is a running program.
  * A program is a file on your computer.
  * Files live in a filesystem.
  * Files are organized into a file system.
  * Files are stored into directories in a file system.
  * `Pwd` command is used to view the current working directory.
  * `Ls` is used to list the files in a particular directory.

* Paths 
  * Absolute path - Starts with a `/` like /user /user/ckc/home etc
  * Relative path - Do not start with a `/` and are relative to the absolute paths.

* Types of files 
  * There are many different types of files. You can use ls -ld /path/to/your/file to check.
    * '-' is a regular file
    * d is a directory (yes, directories are actually just special files!)
    * l is a symbolic link (a file that transparently points to another file or directory)
    * p is a named pipe (also known as a FIFO. You will get very familiar with these this module!)
    * c is a character device file (i.e., backed by a hardware device that produces or receives data streams, such as a microphone)
    * b is a block device file (i.e., backed by a hardware device that stores and loads blocks of data, such as a hard drive)
    * s is a unix socket (essentially a local network connection encapsulated in a file)

---

### Fundamentals : Intro to Binary files.

* /bin/cat
* What is an ELF file ??
* ELF is a binary file format. It contains a program and it's data. Describes how the program should be loaded (program/segment header). It also contains metadata describing program components. (section header)
* INTERP: defines the library that should be used to load this ELF into memory.
* LOAD: defines a part of the file that should be loaded into memory.
* Program headers are the source of info while loading any file.

### Interacting with ELF

* gcc to make your ELF.
* readelf to parse the ELF header.
* objdump to parse the ELF header and disassemble the source code.
* nm to view your ELF's symbols.
* patchelf to change some ELF properties.
* objcopy to swap out ELF sections.
* strip to remove otherwise-helpful information (such as symbols).
* kaitai struct (https://ide.kaitai.io/) to look through your ELF interactively.

Site for challenges: https://dojo.pwn.college/challenges/interaction

#### pwntools

* We can import pwn tools in python using
* from pwn import *

---

