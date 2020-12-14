<template>
  <div>
    <face :activename="activeName" :isrest='isRest' @restActive='restactive' @responseFun='responseFun' ></face>
<!--    <button id="facelogin" @click="faceLogin">开始签到</button>-->
  </div>
</template>
<script>

export default {
  name: 'check_student',
  data() {
    return {
      msg: '',
      activeName: 'active',
      isRest:false,
      image:'',
      course_id: 0
    };
  },
  methods: {
    // 进入人脸识别页面
    // faceLogin() {
    //   this.activeName = 'active';
    // },
    // 重置插件中的数据
    restactive(val){
      this.activeName = val
      this.isRest = false;
    },
    responseFun(data){
      if(data != ''){
        this.course_id = this.$route.query.course_id
        this.$router.push({
          path: `/check/list`,
          query: {image:data,course_id:this.course_id}
        })
      }
      setTimeout(()=>{
        this.isRest = true;
      },1000)
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
