// 引入Vue框架
import Vue from 'vue'
// 引入资源请求插件
import axios from 'axios'
 
// 使用axios插件
// 每个 Vue 对象都会新增一个 axios 对象
Vue.prototype.axios = axios;
 
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
  // 在发送请求之前
  return config;
},function (error) {
  // 请求错误时
  return Promise.reject(error);
});
 
// 添加响应拦截器
// 拦截器可以对请求做一些公共的处理，比如异常、返回数据的格式
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 500:
          // do something
          break
        case 402:
          // do something
          break
      }
    }
    return Promise.reject(error.response.data);   // 返回接口返回的错误信息
  });
export default ({
})
