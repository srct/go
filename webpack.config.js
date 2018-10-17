module.exports = {
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },

        { test: /\.css$/, use: [ 'style-loader', 'css-loader' ] }
        ],
    },
    resolve: {
        extensions: ['*', '.js', '.jsx'],
    },
};
