buf = open('unopenable.gif', 'rb').read()
buf = b"\x47\x49\x46\x38" + buf
with open('unopenable-fix.gif', 'wb') as fd:
    fd.write(buf)
