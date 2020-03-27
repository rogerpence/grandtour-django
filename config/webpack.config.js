const { VueLoaderPlugin } = require('vue-loader');
const path = require('path');

module.exports = {
    mode: 'development',
    entry: {
        tourstops: './resources/tourstops.js',
    },
    output: {
        path: path.join(__dirname, '../static'),
        filename: '[name].build.js'
    },
    devtool: 'false',
    module: {
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader',
        }, ]
    },
    plugins: [
        new VueLoaderPlugin(),
    ]
}