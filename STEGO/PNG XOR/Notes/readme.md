### PNG 

First 8 hex codes are the png signature : following it the next 8 hex codes are the IHDR and it's chunk.

Then the next 4 hex codes are the image width and the very next 4 hex codes are image height.

Then the next 5 hex codes aren't that relevant.

After these 5 hex codes, we have the CRC check sum.


```py
After the header come a series of chunks. Each chunk starts with 4 bytes for the length of the chunk, 4 bytes for the type, then the chunk content itself (with the length declared earlier) and 4 bytes of a checksum.
```
