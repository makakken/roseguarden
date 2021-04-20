const pkg = require('./package')

import colors from 'vuetify/lib/util/colors'
const VuetifyLoaderPlugin = require('vuetify-loader/lib/plugin')

module.exports = {
  ssr: false,

  /*
  ** Headers of the page
  */
  head: {
    title: 'Roseguarden',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description', name: 'description', content: 'Roseguarden is a management tool for shared spaces'
      }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/konglo_logo.png' }
    ],
    script: [
      {} //src: 'https://cdnjs.cloudflare.com/ajax/libs/echarts/4.0.4/echarts-en.min.js' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: {
    color: "#5218fa"
  },

  /*
  ** Global CSS
  */
  css: [
    '~/assets/style/app.sass',
    'vuetify/src/styles/styles.sass',
    '@mdi/font/scss/materialdesignicons.scss',
    'font-awesome/css/font-awesome.css',
    'roboto-fontface/css/roboto/roboto-fontface.css',
    'material-design-icons/iconfont/material-icons.css',
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    //'@/plugins/vuetify',
    '@/plugins/vee-validate',
  ],

  router: {
    extendRoutes(routes, resolve) {
      routes.push({
        path: "/actionlink/:actionhash",
        component: resolve(__dirname, 'pages/actionlink.vue'),
        name: "actionlink",
        props: true
      }, {
        path: "/:section",
        component: resolve(__dirname, 'pages/section.vue'),
        name: "section",
        props: true
      }, {
        path: "/:group/:section",
        component: resolve(__dirname, 'pages/section.vue'),
        name: "section-grouped",
        props: true
      }
      )
    }
  },

  server: {
    port: 3333 // default: 3000
  },

  /*
  ** Nuxt.js modules
  */
  modules: [
    // Simple usage
    '@nuxtjs/proxy',
    ['@nuxtjs/vuetify', { defaultAssets: false, }],
  ],

  /*
  ** Build configuration
  */
  build: {
    loaders: {
      sass: {
        indentedSyntax: true,
      }
    },
    extractCSS: true,
    defaultAssets: {
      font: {
        family: 'Roboto'
      },
      icons: 'mdi'
    },
    /*
    ** You can extend webpack config here
    */
    extend(config, { isClient }) {
      // Extend only webpack config for client-bundle
      if (isClient) {
        //config.devtool = '#source-map'
      }
    }
  },

  vuetify: {
    customVariables: ['~/assets/style/vueify_custom.sass'],
    theme: {

      options: {
        customProperties: true,
        minifyTheme(css) {
          return process.env.NODE_ENV === 'production'
            ? css //.replace(/(?<!v-application)[\s|\r\n|\r|\n]/g, '')
            : css
        },
      },
      light: true,
      dark: false,
      themes: {
        light: {
          info: "#5218fa",
          primary: "#7fffd4",
          secondary: "#ffa07a",
          accent: colors.shades.black,
          error: "#ff5252",
        },
        dark: {
          info: "#5218fa",
          primary: "#7fffd4",
          secondary: "#ffa07a",
          accent: colors.shades.black,
          error: "#ff5252",
        }
      }
    }
  },

  proxy: {
    // Simple proxy
    //'/api': 'https://www.roseguarden.fabba.space/api/log',

    // With options
    '/api/v1/log': {
      target: 'http://localhost:5000',
      // target: 'https://www.roseguarden.fabba.space',
      ws: true,
      secure: true,
      changeOrigin: true
    },
    '/api/v1': {
      target: 'http://localhost:5000',
      // target: 'https://www.roseguarden.fabba.space',
      ws: true,
      secure: false,
      changeOrigin: true
    },
  },

  env: {
    baseUrl: process.env.BASE_URL || 'http://localhost:3000',
    FRONTENDVERSION: escape(JSON.stringify(require('./package.json').version))
  }
}
