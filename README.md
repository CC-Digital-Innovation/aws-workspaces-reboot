# CLI wrapper for Amazon WorkSpaces API 

## Summary
A Python CLI wrapper for Amazon WorkSpaces API; built to schedule weekly Amazon WorkSpaces reboots.

_Note: If you have any questions or comments you can always use GitHub discussions, or DM me on the twitter @rbocchinfuso._

#### Why
Customer request to schedule weekly reboots of all Amazon Workspaces.

#### Todo
- Improve logging and error handling
- Add Slack notifications

## Requirements
- Python 3
	- [Anaconda](https://www.anaconda.com/products/individual) is a good choice, and what I use regardless of platform.
- All other requirements are in the requirements.txt file.
```pip install -r requirements.txt```

## Usage
- Download code from GitHub
```git clone https://github.com/CC-Digital-Innovation/aws-workspaces-reboot.git```
- Note:  If you don't have Git installed you can also just grab the zip:
https://github.com/CC-Digital-Innovation/aws-workspaces-reboot/archive/master.zip

- Copy config.ini.example to config.ini and modify as required

- Run workspaces.py
```
(dev) >>> python workspaces.py -h
Python CLI wrapper for Amazon Workspaces API

Usage:
    workspaces.py get
    workspaces.py getallwsids
    workspaces.py reboot <WorkspaceId>
    workspaces.py test
    workspaces.py nuke

Arguments:
    WorkspaceId     use 'get' to identify a workspace

Options:
    -h --help       Show this screen.
    --version       Show version.

Commands:
    get                           Query workspaces
    getallwsid                    Get all workspace IDs
    reboot <WorkspaceId>          Reboot a specific workspace
    test                          Test run rebooting all workspaces
    nuke                          Reboot all workspaces

```

- Add workspaces.py to crontab
```
0 3 * * 1 /home/user/miniconda3/bin/python /home/user/workspaaces/workspaces.py nuke > /home/user/workspaaces/nuke_log.json 2>&1
```
_Note: The above above crontab entry reboots all Amazon WorkSpaces at 3 AM every Monday._

## Example

### get
```
(dev) >>>python workspaces.py get
[15:40:44] ┌────────────────────── INFO ──────────────────────┐ workspaces.py:90
           │ Getting Workspcaes                               │
           └──────────────────────────────────────────────────┘
           [                                                                                           workspaces.py:94
               {
                   'WorkspaceId': 'ws-w5nx716j6',
                   'DirectoryId': 'd-9067078b83',
                   'UserName': 'foo',
                   'IpAddress': '172.100.100.100',
                   'State': 'AVAILABLE',
                   'BundleId': 'wsb-k3d1dsy0p',
                   'SubnetId': 'subnet-000000000000',
                   'ComputerName': 'EC2AMAZ-000000',
                   'WorkspaceProperties': {
                       'RunningMode': 'ALWAYS_ON',
                       'RootVolumeSizeGib': 80,
                       'UserVolumeSizeGib': 10,
                       'ComputeTypeName': 'PERFORMANCE'
                   },
                   'ModificationStates': []
               }
		   ]
```

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ツ

## History
-  version 0.2.0 (fixed bug in API pagination) - 2021/03/07
-  version 0.1.0 (initial release) - 2021/02/19

## Credits
Rich Bocchinfuso <<rbocchinfuso@gmail.com>>

## License	
MIT License

Copyright (c) [2021] [Richard J. Bocchinfuso]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.