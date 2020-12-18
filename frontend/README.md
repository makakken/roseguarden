## roseguarden frontend

### Prequisites:
- the following desciption is a wrap up of needed prequisites
- install nodejs LTE and the nodejs packaga manager (npm)
   - Windows: Packages installation here https://nodejs.org/en/download/
   - Linux: `sudo apt install nodejs npm`
- install the VSCode
   - Windows: ---fail
   - Linux: https://code.visualstudio.com/docs/setup/linux
- install the the vue client vue-client
   - Windows, Linux: `npm install -g @vue/cli`
   - check the version: `vue -V` should be > 3.0.0 otherwise deinstall old versions with npm uninstall vue-cli -g

### Setup the VSCode for vue developement (Vetur, vue-peek)

- open Visual Studio Code in your workspace-folder
- install the Vue Extension Pack (Vetur, vue-peek, etc.) extensions ("Extensions", Ctrl + Shift + X)
- install `Vue.js Extension Pack`

### Install useful tools 

#### JSON-Server

The json-server is useful to make requests while developing.

Install json-server with `sudo npm install -g json-server`

### Import and run a this vue application

- `git clone` the repository
- install packages with `npm install`
- see the README.md for running and build the app


### Template project Structure
```bash
├── build
├── config (Webpack)
├── src
│   ├── api
│   ├── components
│   ├── mixins
│   ├── pages (or views)
│   ├── router
│   ├── util
│   ├── theme
│   │   ├── default.styl
│   └── App.vue
│   └── event.js
│   └── main.js
├── dist
├── release
├── static (or asset)
├── mock (or script to build mock data)
├── node_modules
├── test
├── README.md
├── package.json
├── index.html
└── .gitignore

### Build Setup

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
