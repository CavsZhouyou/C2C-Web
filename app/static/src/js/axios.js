/*
 * @Author: zhouyou@werun 
 * @Descriptions: axios 配置文件 
 * @Date: 2018-03-30 14:32:10 
 * @Last Modified by:   zhouyou@werun 
 * @Last Modified time: 2018-03-30 14:32:10 
 */

import axios from 'axios';

axios.defaults.headers.common['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8";

// configure axios response interceptors
axios.interceptors.response.use(
  response => {
    if (response.data.message === "未登录或登录超时") {
      alert("您已登录超时，请重新登陆！");
    }
    return response;
  }
)


export default axios;
