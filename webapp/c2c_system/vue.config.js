module.exports = {
    configureWebpack: config => {
        config.entry.mondernize = './src/js/modernizr.js'
    },

    devServer: {
        open: process.platform === 'darwin',
        host: '0.0.0.0',
        port: 9090,
        https: false,
        hotOnly: false,
        proxy: null, // 设置代理
        before: app => {}
    },
}