<template>
<div>

  <div v-if="!post">loading</div>

  <div v-else>

    <B>工作岗位：</B><br />

    级别： {{ level }} <br />

    岗位： {{ post }}

  </div>

</div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      level: '',
      post: ''
    }
  },
  mounted () {
    const url = `http://127.0.0.1:10072/todo/api/v1.0/tasks/`
    axios.get(url, {
      params: {
        name: 'appleyuchi',
        password: 'mima'
      }
    }).then(response => {
      const result = response.data
      const repoRepo = result.jobs[0]
      this.post = repoRepo.post
      this.level = repoRepo.level
    }).catch(error => {
      console.log('Inside error, fetching product line items failed', error)
      alert('请求失败了')
    })
  }}
</script>

<style>

</style>
