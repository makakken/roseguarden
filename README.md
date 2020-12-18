# roseguarden

Roseguarden is an access and management system for spaces.

## Live demo

You can find our live server here : https://roseguarden.fabba.space .
There is also a emulator available to test the full workflow without a need for own hardware.
If you find bugs or have feature requests, please start with an issue [here](https://gitlab.com/roseguarden/roseguarden/-/issues). 
The demo server is a public. Please be aware that all data is visible to anybody.
It's meant to be only for test purposes. The data can be reset at any time. 

## How to run roseguarden

### By using the release packages

* Download and unzip the latest release `roseguarden-X.Y.Z` [here](https://gitlab.com/roseguarden/roseguarden/-/releases) 
* Go to the folder and run the following commands in a terminal
    * Install the requirements with `pip3 -r requirements.txt`
    * Create a `config.ini` with your settings (see `config.template`) 
    * Run 'flask run'

### By using or forking the repository

* Clone or fork the repository
* Have a look in the `backend` and `frontend` folder for details to setup your development enviroment
* run `backend` and `frontend` from your development environment (e.g. we use vs code)
+ alternativly you can use the `script/pack.py`-script to build your own package 

## News

You can find news about the project [on patreon](https://www.patreon.com/roseguarden)

## Support 

Support us on patreon : https://www.patreon.com/roseguarden 

## Contribute

You are welcome to contribute. Make a merge request or add issues.
Help is needed in every area e.g. frontend, backend, hardware and documentation.

## License

The different parts of roseguarden are license as followed:

* frontend : MIT license
* backend : GPLv3 license
* docs : Creative Commons

Have a look in the LICENSE files in the folders for details.
