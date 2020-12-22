<template>
  <div>
    <van-nav-bar
      title="签到验证"
    />
    <div v-if="this.status == ''">
      <van-loading type="spinner" vertical>加载中...</van-loading>
    </div>
    <div v-else>
      <div v-if="this.student_name != ''">
        <van-row>
          <van-col span="24">
            <van-cell-group>
              <van-cell title="姓名" :value="this.student_name" />
              <van-cell title="学号" :value="this.student_num" />
              <van-cell title="状态" :value="this.status" />
            </van-cell-group>
          </van-col>
        </van-row>
      </div>
      <div v-else>
        <van-row>
          <van-col span="24">
            <van-cell-group>
              <van-cell title="状态" :value="this.status" />
            </van-cell-group>
          </van-col>
        </van-row>
      </div>
      <van-button type="default" @click="check_agin()">继续签到</van-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "check_display",
  data() {
    return {
      image:'',
      course_id: 0,
      student_name:'',
      student_num:'',
      status: ''
    };
  },
  mounted() {
    this.check()
  },
  methods: {
    check(){
      this.image = this.$route.query.image
      this.course_id = this.$route.query.course_id
      this.$ajax.post('http://192.168.1.140:5555/course/check/',{
        image_info:this.image,course_id:this.course_id
      }).then((res) => {
        console.log(res)
        if(res.data["code"] == 200){
          console.log("签到成功")
          this.student_name = res.data["student_name"]
          this.student_num = res.data["student_num"]
          this.status = "签到成功，按时签到"
        }else if(res.data["code"] == 201){
          console.log("迟到")
          this.student_name = res.data["student_name"]
          this.student_num = res.data["student_num"]
          this.status = "签到成功，迟到"
        }else if(res.data["code"] == 302){
          this.status = "签到失败，未选此门课"
        }else{
          this.status = "签到失败，人员不存在"
        }
      }).catch(function (error) {
        console.log(error);
      });
    },
    check_agin(){
      this.$router.push({
        path: `/course/check`,
        query: {course_id:this.course_id }
      })
    }
  }
}
</script>

<style scoped>

</style>
