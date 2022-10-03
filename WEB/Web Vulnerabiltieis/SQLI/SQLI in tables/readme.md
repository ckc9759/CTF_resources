### N o T e S

---

Sometimes, we are given a database and not a login portal which is vulnerable to SQLi.

- Use of `UNION` operator.
- Use of `AS` keyword. --> It renames a coloumn or table of the query result.

### Example : Book Search database

Example of Sqli in database : 

```sql
Feeling%' UNION SELECT NULL NULL NULL --
```
