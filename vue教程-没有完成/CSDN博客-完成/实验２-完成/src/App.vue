<template>
    <div>
        <li v-for = "(item,key) in obj">{{ key }}:{{ item }}<br></li>
        <button @click="getData">get提交数据</button>
        <button @click="postData">post提交数据</button>
        <button @click="getJson">json请求</button>
    </div>
</template>

<script>
import axios from 'axios'

export default 
{
  name: 'my-first-vue',
data(){
    return{
        obj:null
    }
},


  methods: 
  {

      //------------------------------------------------get------------------------------------------------------------------------------

    getData () {
      var that = this
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const url = 'api/message'
      axios.get(url,

{  //params参数必写 , 如果没有参数传{}也可以
    params: {  
       id: 12345,
       name: "appleyuchi"
    }
}



      ).then(function (response) {
        // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
        // 可以直接通过 response.data 取key-value
        // 坑一：这里不能直接使用 this 指针，不然找不到对象
        var msg = response.data.msg
        // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
        that.serverResponse = msg

        that.obj=response.data;

        alert('Success ' + response.status + ', ' + response.data + ', ' + msg)
      }).catch(function (error) {
        alert('Error ' + error)
      })
    }

,



    //----------------------------------------------------------post--------------------------------------------------------------------
        postData () {
      var that = this
      // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，本地则为127.0.0.1，外网则为 your_ip_address
      const url = 'api/post_message'
      axios.post(url,

{  //params参数必写 , 如果没有参数传{}也可以
    params: {  
       id: 12345,
       name: "appleyuchi"
    }
}



      ).then(function (response) {
        // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
        // 可以直接通过 response.data 取key-value
        // 坑一：这里不能直接使用 this 指针，不然找不到对象
        var msg = response.data.msg
        // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
        that.serverResponse = msg

        that.obj=response.data;

        alert('Success ' + response.status + ', ' + response.data + ', ' + msg)
      }).catch(function (error) {
        alert('Error ' + error)
      })
    },
//----------------------------------------------------------json--------------------------------------------------------------------
      getJson () {
      var that = this
axios.get('api/work/data.json').then(function (response) {
        // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
        // 可以直接通过 response.data 取key-value
        // 坑一：这里不能直接使用 this 指针，不然找不到对象
        var msg = response.data.msg
        console.log("msg=",msg)
        // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
        that.serverResponse = msg

        that.obj=response.data;

        alert('Success ' + response.status + ', ' + response.data + ', ' + msg)
      }).catch(function (error) {
        alert('Error ' + error)
      })
    }

 
  }
}
</script>
