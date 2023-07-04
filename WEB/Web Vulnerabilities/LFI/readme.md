### LFI --> Local file inclusion

---

LFI or Local File Inclusion occurs when an attacker is able to get a website to include a file that was not
intended to be an option for this application. A common example is when an application uses the path to a
file as input. If the application treats this input as trusted, and the required sanitary checks are not
performed on this input, then the attacker can exploit it by using the ../ string in the inputted file name
and eventually view sensitive files in the local file system. In some limited cases, an LFI can lead to code
execution as well.

RFI or Remote File Inclusion is similar to LFI but in this case it is possible for an attacker to load a remote
file on the host using protocols like HTTP, FTP etc.
