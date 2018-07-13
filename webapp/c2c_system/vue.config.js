module.exports = {
    baseUrl: './',

    configureWebpack: config => {
        config.entry.mondernize = './src/js/modernizr.js'
    },

    devServer: {
        open: process.platform === 'darwin',
        host: '0.0.0.0',
        port: 9090,
        https: false,
        hotOnly: false,
        proxy: {
            "/c2c/*": {
                target: "http://www.xblame.top:5000",
                secure: false
            },
        }, // 设置代理
        before: app => {}
    },
}