## Tourstop branch

### Add tourstop app
### Add helpers app
### Install cross-env package
### Add package.json script
* launch Django server
* run webpack
```
"pserver": "cross-env NODE_ENV=development python manage.py runserver localhost:5000",
"dev": "cross-env NODE_ENV=development webpack --config ./config/webpack.config.js"
```
### Settings file
* Add settings.dev.py
* In settings.file
    * configure static folder
    * configure TEMPLATES.DIRS
    * import settings.dev.py
* In settings.dev.py
    * turn debug on
    * set mime types
    * configure TEMPLATES.DIRS
### Nested apps
### Add
### Install NPM modules
* @vlue/cli
* vue-loader
* webpack
* webpack-cli
### Add Webpack config
### Add resources folder
* add App.vue
* add tourstops.js
### Add static folder

