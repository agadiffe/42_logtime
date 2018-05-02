# 42_logtime

## Install
```
pip install -r requirements.txt
```
## config
```
cp config.conf.sample config.conf
```
then add your client_id and client_secret from 42 API
## usage
```
python logtime_tracking.py
```
## know issues
you can get wrong logtime if:
- [end_at] are missing (bug should be fix soon from 42 API team)
- you were connected from 2 different location at the same time (i don't handle it yet)
