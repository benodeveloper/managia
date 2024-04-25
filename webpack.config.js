const path = require('path')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const IgnoreEmitPlugin = require('ignore-emit-webpack-plugin');
const { BuildOutputPlugin } = require('@laravel-mix/webpack-build-output')
const CopyPlugin = require("copy-webpack-plugin");

/** 
 * {@link https://github.com/webpack/webpack/discussions/14280}
 */
module.exports = [
    {
        mode: process.env.NODE_ENV,
        entry: {
            'css/style': path.resolve(__dirname, 'resources/assets/scss/style.scss'),
            'js/index': path.resolve(__dirname, 'resources/assets/js/index.js')
        },
        output: {
            path: path.resolve(__dirname, 'static'),
            filename: '[name].js',
            // assetModuleFilename: "images/[name][ext]",
        },
        module: {
            rules: [
                // {
                //     test: /\.(png|jpe?g|gif|svg)/i,
                //     type: "asset/resource",
                // },
                {
                    test: /\.(s[ac]|c)ss$/i,
                    use: [
                        {
                            loader: MiniCssExtractPlugin.loader,
                            options: { publicPath: "" }
                        },
                        "css-loader", "postcss-loader", "sass-loader"
                    ],
                },
                {
                    test: /\.js?$/,
                    exclude: /node_modules/,
                    use: {
                        loader: "babel-loader",
                    }
                }
            ]
        },
        plugins: [
            // new CleanWebpackPlugin(),
            new MiniCssExtractPlugin({
                filename: "[name].css",
                chunkFilename: "[id].css",
            }),
            new IgnoreEmitPlugin(/css\.js$/),
            new IgnoreEmitPlugin(/images\.js$/),
            new IgnoreEmitPlugin(/js\.js$/),
            new BuildOutputPlugin(),
            // node_modules/flowbite/dist/flowbite.min.js
            new CopyPlugin({
                patterns: [
                  { from: "node_modules/flowbite/dist/flowbite.min.js", to: "js/flowbite.min.js" },
                ],
              }),
        ],
        stats: {
            preset: 'errors-warnings',
          },
        resolve: {
            extensions: [".js"],
        },

        devtool: process.env.NODE_ENV == "development" ? "source-map" : undefined,

    }]
