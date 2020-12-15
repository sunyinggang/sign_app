<template>
  <div>
    {{ msg }}
    <face :activename="activeName" :isrest='isRest' @restActive='restactive' @responseFun='responseFun' ></face>
    <div style="margin-top: 250px;background-color: #fff">
      <button class="btn" id="facelogin" @click="faceLogin">开始签到</button>
    </div>
  </div>
</template>
<script>

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: '',
      activeName: '',
      isRest:false
    };
  },
  methods: {
    // 进入人脸识别页面
    faceLogin() {
      this.activeName = 'active';
    },
    // 重置插件中的数据
    restactive(val){
      this.activeName = val
      this.isRest = false;
    },
    responseFun(data){
      if(data != ''){
        console.log(data)
        this.$router.push({
          path: `/course/list`,
          query: {image:data}
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
<style scoped>
.btn{
  color: #323233;
  height: 50px;
  width: 100px;
  background-color: #e0dbdb;
  border: 1px solid #ebedf0;
}
</style>
