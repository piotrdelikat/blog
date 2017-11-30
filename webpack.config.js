var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: './src/js/main.js',
    output: {
      path: __dirname + '/home/static',
      filename: 'js/bundle.js'
    },
    module: {
      rules: [
              {
                  test:/\.css$/,
                  use: ExtractTextPlugin.extract({
                          fallback:'style-loader',
                          use:['css-loader'],
                  })
              },
              {
                  test: /\.(eot|svg|ttf|woff|woff2)$/,
                  loader: "file-loader",
                  options: {
                    name: "fonts/[name].[ext]",
                  },
              },
            ]
          },
      plugins: [
         new webpack.ProvidePlugin({
           $: 'jquery',
           jQuery: 'jquery',
           'window.jQuery': 'jquery',
           Popper: ['popper.js', 'default'],
           }),
         new ExtractTextPlugin("css/styles_bundle.css"),
  ]
}
