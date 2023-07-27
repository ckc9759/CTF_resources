### Dom-based XSS

---

- Happens when JS takes data from an attacker-controllable source. URL -> example
- Enter a random string and then find where that string is used

- Suppose it is used in `<img src="` tag, then just break it usin `">`
