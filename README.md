<!--
 * @Author: Vincent Young
 * @Date: 2022-10-12 04:52:04
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-10-13 01:46:43
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

**~~You must be aware that an `Unregistered` status does not mean that you are truly unregistered. The program cannot determine whether Gmail is unregistered or blocked.~~**

**Determining whether a state is truly unregistered is already supported in the `Enhanced Mode`.**


## Update
### 0.0.8
- Hide `Chrome` Windows, using no-browser.
- Record results to `result.txt` file.

### 0.0.6
- Fixed bug

### 0.0.5
- Add Enhanced Mode
- Support for truly unregistered judgments

## Usage
**You need to install `GmailChecker` before.**
```bash
pip install GmailChecker
```
### Lite Mode
1. Create a new `.py` file with the following codes.
```python
from GmailChecker import GmailChecker
# Only Print Unregistered Result
GmailChecker.verify("admin@gmail.com")
# Print Alive Result
GmailChecker.verify("admin@gmail.com", 1)
```
2. If you want to scan Gmails in bulk, you can use the following codes.
```python
from GmailChecker import GmailChecker
for i in range(1000000, 9999999):
    email = str(i) + '@gmail.com'
    GmailChecker.verify(email)
```

### Enhanced Mode
1. You should download `chromedriver` to file directory.

2. Create a new `.py` file with the following codes.
```python
from GmailChecker import GmailCheckerEnhanced
for i in range(9960001, 9969999):
    # By default only unregistered results will be output
    GmailCheckerEnhanced.scan(i)
```

## PyPi
<a href="https://pypi.org/project/GmailChecker/"><img src="https://img.shields.io/badge/Pypi-000000?style=for-the-badge&logo=pypi&logoColor=red" /></a>

## Reference Articles
[Abusing Gmail to get previously unlisted e-mail addresses](https://blog.0day.rocks/abusing-gmail-to-get-previously-unlisted-e-mail-addresses-41544b62b2)

## Author

**GmailValidChecker** © [Vincent Young](https://github.com/missuo), Released under the [MIT](./LICENSE) License.<br>

