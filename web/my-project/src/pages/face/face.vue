<template>
  <view>
    <face :activename="activeName" :isrest='isRest' @restActive='restactive' @responseFun='responseFun' ></face>
    <button id="facelogin" @click="faceLogin">开始签到</button>
  </view>
</template>

<script>
export default {
name: "face",
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
      console.log(data)
      setTimeout(()=>{
        this.isRest = true;
      },1000)
    }
  },
}
</script>

<style scoped>

</style>
