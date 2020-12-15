# Actions of the server requested by a node

!!! important "The description of this actions is written from the perspektive of action requested by a node. <br> The actions meant to be executed by the server." 

## General actions

This actions every node have to implement.

### Startup ( registerNodeStartup )

Triggered on: Startup of the node

### Update the node ( requestNodeUpdate )

Triggered on: Interval (default is 1 minute) when authetification was successfull.

### Update the node errors ( syncNodeLog )

### Update the node status ( syncNodeSettings )

### Update the node status ( syncNodeIdentification )

Request the server to sync or update the node identification

The following properties have to be included:

  * `nodename` : The name of the node
  * `classname` :  The node class tag
  * `classworkspace` :  The nodes workspace it should work from
  * `classid` :  The nodes class identification represented as 6 bytes in the form of "00:01:AB:EF:19:D8:00:11" (hex, colon-seperated)
  * `firmware_version` : The firmware version
  * `firmware_compiled_at` : The timestamp when the firmware was compiled, in the form of  "2007-12-22T18:21:01"
  * `firmware_flashed_at` : the timestamp when the firmware was flashed, in the form of "2007-12-24T11:31:02"
  * `hardware_version` : The firmware version

Additional properties can be send.

**Example:**

    ``` json

    {
    "header": {
        "source": "Door 1",
        "version": "1.0.0",
        "target": "roseguarden.fabba.spcae",
        "fingerprint": "43:51:43:A1:B5:FC:8B:B7:0A:3A:A9:B1:0F:66:73:A8:73:A8:19:B1",
        "authentification": "Kol-Bi-Hop-Ban-Gan-To-Sep+129",
        "uptime": 15,
        "logcounter": 2,
        "timestamp": "2020-11-23T16:14:19.108Z"
    },
    "actions": [
        {
            "version": "1.0.0",
            "action": "syncNodeIdentification",
            "actionid": 1,
            "nodename": "Door 1",
            "classname": "Door",
            "classworkspace": "Access",
            "classid": "00:01:AB:EF:19:D8:00:11",
            "firmware_version": "0.1.2",
            "firmware_compiled_at": "2007-12-22T18:21:01",
            "firmware_flashed_at": "2007-12-24T11:31:02",
            "hardware_version": "0.1.0"
        }
    ]
    }

    ```

## Node specific actions 

In addition every node can supply further actions handled by the server.