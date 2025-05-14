const path = require('path');

module.exports = {
  entry: './src/client/index.js',
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: {
          loader: '@sucrase/webpack-loader',
          options: {
            transforms: ['jsx'],
          },
        },
      },
    ],
  },
  mode: 'development',
};
