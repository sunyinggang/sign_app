<template>
  <van-nav-bar
    title="签到验证"
  />

</template>

<script>
export default {
  name: "check_display",
  data() {
    return {
      image:'',
      course_id: 0,
      student_name:'',
      student_num:''
    };
  },
  mounted() {
    this.check()
  },
  methods: {
    check(){
      this.image = this.$route.query.image
      this.course_id = this.$route.query.course_id
      this.$ajax.post('http://127.0.0.1:5000/course/check/',{
        image_info:this.image,course_id:this.course_id
      }).then((res) => {
        console.log(res)
        if(res.data["code"] == 200){
          console.log("签到成功")
          this.student_name = res.data["student_name"]
          this.student_num = res.data["student_num"]
        }else if(res.data["code"] == 201){
          console.log("迟到")
          this.student_name = res.data["student_name"]
          this.student_num = res.data["student_num"]
        }else {
          console.log("不匹配")
        }
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>

</style>
