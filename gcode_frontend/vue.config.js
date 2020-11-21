module.exports = {
  publicPath: "http://0.0.0.0:8080/",
  outputDir: "./dist/",
  
  transpileDependencies: [
    'vuetify'
  ],

  chainWebpack: (config) => {
    config.devServer
      .public("http://127.0.0.1:8080")
      .host("127.0.0.1")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .historyApiFallback(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  },
};
