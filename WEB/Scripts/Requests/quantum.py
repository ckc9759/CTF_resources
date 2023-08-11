# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:52:19 2023

@author: CHKRISH
"""

import requests

base = "https://nessus-quantumcrypto.chals.io"

payload = {
    "state_list": [[0, 1]]*1024,
    "base_list": ["X"]*1024,
}

print(payload)

r = requests.post(base+"/quantum_key", json=payload, verify=False)

print(r.text)
