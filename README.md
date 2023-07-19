aprs_tocall
==

Install
--

```sh
pip install aprs_tocall
```

Usage
--
```python
from aprs_tocall import Parser
tocalls = Parser(offline=False) 
# Setting offline to False will use the online 
# yaml file, while offline=True (default) will 
# use the distributed version
tocalls.lookup("APWEEA")
# returns 
# {
#   'tocall': 'APWEE?',
#   'vendor': 'Tom Keffer and Matthew Wall',
#   'model': 'WeeWX Weather Software',
#   'class': 'software', 
#   'os': 'Linux/Unix'
# }
```

Command line
--

```sh
% python3 -m aprs_tocall APTTAA
tocall=APTT*
vendor=Byonics
model=TinyTrak
class=tracker
```