### Resources

---

- [Cheatsheet](https://blog.onfvp.com/post/volatility-cheatsheet/)  
- [Hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/windows-forensics/windows-processes)
- [DFIR_Science](https://dfir.science/2022/02/Introduction-to-Memory-Forensics-with-Volatility-3)
- [Github](https://github.com/mzfr/notes/blob/master/ctf/forensics.md)
- 

### Notes 

```py
volatile userassist plugin
python3 vol.py -f mem_search.DUMP windows.filescan | grep -E 'Desktop|Downloads|Documents'
python3 vol.py -f <filename> imageinfo --> --profile <profile name>
Run consoles plugin for cmdline history.
Use memdump to dumpfiles with pid and output directory.
