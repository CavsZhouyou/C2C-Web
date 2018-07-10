/*
 * @Author: zhouyou@werun 
 * @Descriptions: COOKIE操作类文件
 * @Date: 2018-03-30 14:32:42 
 * @Last Modified by:   zhouyou@werun 
 * @Last Modified time: 2018-03-30 14:32:42 
 */

const CookieUtils = {

  // get cookie
  getCookie: function (name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
      return (unescape(arr[2]));
    else
      return null;
  },

  //set cookie
  setCookie: function (c_name, value, expiredays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + expiredays);
    document.cookie = c_name + "=" + escape(value) + ((expiredays == null) ? "" : ";expires=" + exdate.toGMTString());
  },

  //delete one cookie
  deleteCookie: function (name) {
    this.setCookie(name, '', -1);
  },

  //delete all cookies
  deleteAllCookies: function () {
    var keys = document.cookie.match(/[^ =;]+(?=\=)/g);
    if (keys) {
      for (var i = keys.length; i--;)
        document.cookie =
        keys[i] + "=0;expires=" + new Date(0).toUTCString();
    }
  }


}


export default CookieUtils;
