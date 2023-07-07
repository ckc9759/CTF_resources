#### Sqli

---

SQL databases are a type of relational database widely utilised in web applications. There are several implementations of SQL servers available from vendors such as Microsoft and Oracle, as well as open-source products such as MariaDB.

SQL (Structured Query Language) queries are fairly straightforward and offer an English-like syntax. For example, you could query a table called ‘Customers’ and retrieve the customer names and the cities they reside in using the following query:
```sql
SELECT CustomerName, City FROM Customers;
```

An example of SQLI 

The query will only return entries if the email column matches the email input provided by the user. OR we could use our quotation mark in combination with the knowledge of 1=1 to create a completely different SQL statement:

```sql
SELECT * FROM users WHERE email='$email’OR WHERE 1=1--'
```

You’d have noticed the additional dashes -- appended to that statement. This is sometimes necessary. The double dash comments out the rest of the existing SQL query that exists after our injected query, this double dash ensures our query is a valid SQL query and there aren’t any mismatched quotation marks (remember we inserted an additional one before).

---

#### From Portswigger

SQLi refers to retrieving directly inaccesible data from SQL database such as passwd, credentials, personal info.




