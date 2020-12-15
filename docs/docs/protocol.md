# Protocol

* the protocol based on https-requests
* the data will be send/received as json container 
* the server is meant to be master and synchronize every client or node
* the protocol based on an action based pattern, every requests contains actions that should be executed by the receiver
* every request to the server will be responded by a list of actions for the sender (client or node)
* the list of actions of a server-response are meant to be executed on the client/node
* events on the clients or node will trigger action-requests to the server

## General request structure

An example from the (web-)client to the server:

```
{
    "head" : {
        "version" : "1.0",
        "target" : "roseguarden.fabba.space",
        "source" : "Username",
        "sourcetype" : "client",        
        "timestamp" : "2020-03-24T20:20:58+01:00"
    },
    "actions" : [
        {
            "version" : "1.0",
            "action" : "executeViewAction",
            "workspace" : "users",
            "view" : "userList",
            "viewAction" : "lock",
            "entry" : {
                "email" : "test@test.de",
                "name" : "testuser",
            }
        }
    ]
}
```

An example from the node to the server:

```
{
    "head" : {
        "version" : "1.0",
        "target" : "roseguarden.fabba.space",
        "source" : "Nodename",
        "nodeClass" : "door",
        "nodeAuth" : "CB:D2:F7:62:95:81:3D:68:D4:ED:47:1C:20:03:55:7E",
        "nodeFingerprint" : "43:51:43:a1:b5:fc:8b:b7:0a:3a:a9:b1:0f:66:73:a8"
        "timestamp" : "2020-03-24T20:20:58+01:00",
    },
    "actions" : [
        {
            "version" : "1.0",
            "action" : "checkHeartbeat",          
        },
    ],
}
```

## Head

The `head` section in a request, contains static information of the sender that are not bind to specific action.

## Actions

The `actions` section contain a list of actions that should be executed by the receiver of the request.
See the pages for specific actions for node and client to get further information and a list of available action on each.

## Optionals

In addition to `head` and `action` there are optional sections. 
