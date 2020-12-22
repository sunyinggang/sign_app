<template>
  <div>
    <van-nav-bar
      title="课程列表"
    />
    <div class="card">
      <div v-if="this.status != ''">
        <van-row>
          <van-col span="8">{{this.status}}</van-col>
        </van-row>
      </div>
      <div v-else>
        <div v-if="this.teacher_name == ''">
          <van-loading type="spinner" vertical>加载中...</van-loading>
        </div>
        <div v-else>
          <van-row>
            <van-col span="8">教师名：{{this.teacher_name}}</van-col>
            <van-col span="8" offset="8">工号：{{this.teacher_num}}</van-col>
          </van-row>
          <van-row>
            <van-col span="16">
              <van-cell-group>
                <van-cell @click="select_course(item.id)" v-for="item in this.tea_course_list"  icon="arrow" :key="item.id" :title="item.course_name" :value="item.start_time+'--'+item.end_time" :label="item.classroom" />
              </van-cell-group>
            </van-col>
          </van-row>
        </div>
      </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "course_list",
  data() {
    return {
      image: '',
      teacher_name: '',
      teacher_num: '',
      tea_course_list:[],
      status:''
    };
  },
  mounted() {
    console.log(this.teacher_name)
    console.log("---")
    this.get_course_list(this.$route.query.image);
    console.log(this.teacher_name)
    console.log("调用结束")
    console.log(this.teacher_name)
  },
  methods: {
    get_course_list(data){
      this.image = this.$route.query.image
      this.$ajax.post('http://192.168.1.140.:5555/teacher/class/list/',{
        image_info:data
      }).then((res) => {
        console.log(res)
        if(res.data["code"] == 200){
          console.log("本人")
          console.log(res.data["course_list"][0])
          this.tea_course_list = res.data["course_list"]
          this.teacher_name = res.data["teacher_name"]
          this.teacher_num = res.data["teacher_num"]
        }else{
          this.status = "教师不存在"
        }
        console.log(res)
      }).catch(function (error) {
        console.log(error);
      });
    },
    select_course(id){
      this.$router.push({
        path: `/course/check`,
        query: {course_id:id}
      })
    }
  }
}
</script>

<style scoped>
.card {
  margin-bottom: 24px;
  margin-top: 24px;
  padding: 24px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 8px 12px #ebedf0;
}
</style>
