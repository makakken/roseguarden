
# Actions of a node actions requested by the server

!!! important "The description of this actions is written from the perspektive of action-requests by the server. <br> The actions meant to be executed by the node and will be a send in form of a reply to an request from the node." 

## General actions

This actions every node have to implement.
The node have to reply to this general actions send by the server.

### Identify ( sendIdentification )

Request the node to send a `syncNodeIdentification` action to the server.

### Get node log ( sendLogs )

**Example:**


The node should send a list of `updateNodeHistory`-actions to the server.
The actions contains actual history informations. The last n (min. 5) actions have to be stored in the nodes ram.
The history wont be reset after send.

```
{
    "head" : {
        ...
    },
    "actions" : [
        {
            "action" : "syncNodeHistory",          
            "historyid" : 22,
            "historyaction" : "openDoor",          
            "timestamp" : "2020-03-24T20:21:58+01:00",
            "source" : "roseguarden.fabba.space"
        },        
        {
            "action" : "syncNodeHistory",          
            "historyid" : 21,
            "historyaction" : "readRfid", 
            "timestamp" : "2020-03-24T20:22:58+01:00",
            "source" : "internal"
        },
    ],
}
```

### Time update ( updateTime )

Properties to update:

  * `nodeTime` :

### Update settings ( updateSettings )

The server will send a action to update the list of node settings.
The action contain all properties
The list can be empty to trigger a `syncNodeSettings`-action with the actual possible settings avalable.

E.g.: 

```
    "head" : {
        ...
    },
    "actions" : [
        {
            "action": "updateSettings",
            "settingA": "a",
            "settingB": "b",
        }
    ]
```

The list can be empty to trigger a `syncNodeSettings`-action with the actual possible settings avalable.

```
    "head" : {
        ...
    },
    "actions" : [
        {
            "action": "updateSettings",
        }
    ]
```



The node have to respond with a `syncNodeSettings`-action to the server as fast as possible.

E.g.:

```
    "head" : {
        ...
    },
    "actions" : [
        {
            "action": "syncNodeSettings",
        }
    ]
```

### Trigger neighbour ( triggerNeighbour )


## Node specific actions 