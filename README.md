<!--
 * @Author: Vincent Young
 * @Date: 2022-10-12 04:52:04
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-10-12 06:15:17
 * @FilePath: /GmailValidChecker/README.md
 * @Telegram: https://t.me/missuo
 * 
 * Copyright © 2022 by Vincent, All Rights Reserved. 
-->
# GmailValidChecker
Gmail validity checker

## Description

The program will return only two results:

- `Alive`: means that everything is fine with this Gmail and is being used.
- `Unregistered`: It means that the Gmail is not registered or is **blocked**.

**You must be aware that an `Unregistered` status does not mean that you are truly unregistered. The program cannot determine whether Gmail is unregistered or blocked.**

## Usage
1. You need to install `GmailChecker` before.
```bash
pip install GmailChecker
```
2. Create a new `.py` file with the following codes.
```python
from GmailChecker import GmailChecker
GmailChecker.verify("admin@gmail.com")
```
3. If you want to sweep Gmails in bulk, you can use the following codes.
```python
from GmailChecker import GmailChecker
for i in range(1000000, 9999999):
    email = str(i) + '@gmail.com'
    GmailChecker.verify(email)
```

## PyPi
<a href="https://pypi.org/project/GmailChecker/"><img src="https://img.shields.io/badge/Pypi-000000?style=for-the-badge&logo=pypi&logoColor=red" /></a>

## Reference Articles
[Abusing Gmail to get previously unlisted e-mail addresses](https://blog.0day.rocks/abusing-gmail-to-get-previously-unlisted-e-mail-addresses-41544b62b2)

## License
MIT License

