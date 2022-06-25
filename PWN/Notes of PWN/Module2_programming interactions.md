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

* 
