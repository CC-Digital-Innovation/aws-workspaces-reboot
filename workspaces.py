# -*- coding: utf-8 -*-
'''
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
    getallwsids                   Get all workspace IDs
    reboot <WorkspaceId>          Reboot a specific workspace
    test                          Test run rebooting all workspaces
    nuke                          Reboot all workspaces
'''

from docopt import docopt
from rich.console import Console
from rich.panel import Panel
import boto3
from botocore.config import Config
import configparser

# owned
__author__ = 'Rich Bocchinfuso'
__copyright__ = 'Copyright 2021, Python CLI wrapper for Amazon Workspaces API'
__credits__ = ['Rich Bocchinfuso']
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Rich Bocchinfuso'
__email__ = 'rbocchinfuso@gmail.com'
__status__ = 'Dev'


def main():
    """Things start here."""
    arguments = docopt(
        __doc__,
        version='Python CLI wrapper for Amazon Workspaces API - v0.1.0')
    if arguments['get']:
        get()
    elif arguments['getallwsids']:
        getallwsids()
    elif arguments['reboot']:
        reboot(arguments['<WorkspaceId>'])
    elif arguments['test']:
        test()
    elif arguments['nuke']:
        nuke()
    else:
        exit("{0} is not a command. \
            See 'workspaces.py --help'.".format(arguments['<command>']))


def aws():
    """Read and parse config file and create AWS API connection."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.sections()

    my_config = Config(region_name=config['aws']['region'],
                       signature_version='v4',
                       retries={
                           'max_attempts': 10,
                           'mode': 'standard'
    })

    client = boto3.client(
        'workspaces',
        config=my_config,
        aws_access_key_id=config['aws']['access_key_id'],
        aws_secret_access_key=config['aws']['secret_access_key'])

    return (client)


def get():
    """Get AWS Workspace instances."""
    client = aws()
    console.log(Panel('Getting Workspcaes', title='INFO', style=info_fmt))
    workspaces = client.describe_workspaces()['Workspaces']
    # workspaceIds = [workspace['WorkspaceId'] for workspace in workspaces]

    console.log(workspaces)
    # console.log(workspaceIds)


def getallwsids():
    """Get all AWS Workspace instance IDs."""
    client = aws()
    paginator = client.get_paginator("describe_workspaces")
    workspaceIds = []
    for result in paginator.paginate():
        if "Workspaces" not in result:
            continue
        for workspace in result["Workspaces"]:
            # yield workspace['WorkspaceId']
            workspaceIds.append(workspace['WorkspaceId'])
    # console.log(workspaceIds)
    return (workspaceIds)


def reboot(WorkspaceId):
    """Reboot a specific AWS Workspace instance."""
    client = aws()
    console.log(
        Panel('Attemptng reboot of workspaceId: ' + WorkspaceId,
              title='INFO',
              style=info_fmt))
    response = client.reboot_workspaces(RebootWorkspaceRequests=[
        {
            'WorkspaceId': WorkspaceId
        },
    ])
    console.log(response)


def test():
    """Test run reboot all AWS Workspace instances."""
    console.log(Panel('Test run rebooting All Workspcaes', title='INFO',
                      style=info_fmt))
    workspaceIds = getallwsids()
    for x in range(len(workspaceIds)):
        WorkspaceId = (workspaceIds[x])
        console.log('Test run reboot of WorkspaceId: ' +
                    WorkspaceId, style=info_fmt)


def nuke():
    """Reboot all AWS Workspace instances."""
    client = aws()
    console.log(Panel('Rebooting All Workspcaes', title='INFO',
                      style=info_fmt))
    workspaceIds = getallwsids()
    for x in range(len(workspaceIds)):
        WorkspaceId = (workspaceIds[x])
        console.log('Rebooting WorkspaceId: ' + WorkspaceId, style=info_fmt)
        response = client.reboot_workspaces(RebootWorkspaceRequests=[
            {
                'WorkspaceId': WorkspaceId
            },
        ])
        console.log(response)


if __name__ == '__main__':
    console = Console()
    info_fmt = 'yellow'
    main()
