# roseguarden frontend


## Getting started on windows

- Install nodejs LTE: https://nodejs.org/en/download/
- We need `node-gyp` to compile some c++ packages (for fibers).  Please install:
   - `npm install -g --production windows-build-tools` (need to be run by a PowerShell with admin privileges)
   - `npm install -g node-gyp`
- Install the node modules from the frontend folder with:
   - `npm install`
- To start the frontend in dev-mode run:
   - `npm run dev`
- Hint: You can change the proxy for the api-requests in the proxy section in `nuxt.config.json`


## Getting started on linux 
- install nodejs LTE and the nodejs packaga manager (npm)
   - Ubuntu/Debian: `sudo apt install nodejs npm`
- We need `node-gyp` to compile some c++ packages (for fibers). Please install:
   - Ubuntu/Debian: `sudo apt install build-essential`
- Install the node modules from the frontend folder with:
   - `npm install`
- To start the frontend run:
   - `npm run dev`
- Hint: You can change the proxy for the api-requests in the proxy section in `nuxt.config.json`

## Getting started with your changes

- We suggest VS code to have a good development environment for beginners
- Here are some tips you might be interested wenn you start development

### Setup the VSCode for vue developement (Vetur, vue-peek)

- open Visual Studio Code in your workspace-folder
- install the Vue Extension Pack (Vetur, vue-peek, etc.) extensions ("Extensions", Ctrl + Shift + X)
- install `Vue.js Extension Pack`

## A overview of useful commands

```bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# Run Python Server SimpleHTTPServer to test it in the dist folder
Python2: 'python -m SimpleHTTPServer 8081'
Python3: 'python3 -m http.server 8081'

# Run json-server for testdata
json-server --watch testdata/fruits.json --port 4000

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

## Issues 

Sometimes the error `Error: ENOSPC: System limit for number of file watchers reached` appears.
Add: `fs.inotify.max_user_watches=524288` to `/etc/sysctl.conf` and run `sudo sysctl -p` afterwards.


## This Template

The project is a fork of https://github.com/tookit/vue-material-admin (0016a5c73ed03dfbe233efb64d344c7a3e79daf3) under MIT License

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
