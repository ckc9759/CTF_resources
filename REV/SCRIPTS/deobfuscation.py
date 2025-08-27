import importlib._bootstrap_external

_ = lambda __: __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])))

import importlib, sys

iteration = 2
while True:
    try:
        data = b""
        with open(f"code{iteration}.pyc", "rb") as f:
            data = f.read()
        payload = data.split(b"\x4e\x29\x02\xda\x04\x65\x78\x65\x63")[0].split(b"\x00")[-1]
        pyc_data = importlib._bootstrap_external._code_to_timestamp_pyc(_(payload))
        iteration += 1
        with open(f"code{iteration}.pyc", "wb") as f:
            f.write(pyc_data)
        print(f"wrote code{iteration}.pyc")
    except Exception as e:
        print(f"crashed at iteration {iteration}")
        print(e)
        break
