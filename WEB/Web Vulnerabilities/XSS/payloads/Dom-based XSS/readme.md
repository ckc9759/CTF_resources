### Dom-based XSS

---

- Happens when JS takes data from an attacker-controllable source. URL -> example
- Enter a random string and then find where that string is used

- Suppose it is used in `<img src="` tag, then just break it usin `">`
- `location.search` --> alphanumeric string and test
- XSS will fail if URL encoding is done before input processing so it won't be possible to break out of the attribute and inject scripts.

- For breaking JS, use breakpoints and see where the data is travelling or getting processed. (assignment)
- Find the sink

- 
