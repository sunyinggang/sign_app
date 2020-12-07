<template>
  <view class="zai-box">
    <image src="../../static/login.png" mode='aspectFit' class="zai-logo"></image>
    <view class="zai-title">LOGO区域</view>
    <view class="zai-form">
      <input class="zai-input" placeholder="请输入用户名" />
      <input class="zai-input" password placeholder="请输入密码"/>
      <view class="zai-input">
        <picker @change="PickerChange" :value="index" :range="picker">
          <view class="picker">
            {{index>-1?picker[index]:'身份'}}
          </view>
        </picker>
      </view>
      <view class="zai-label">忘记密码？</view>
      <button @click="login" class="zai-btn">立即登录</button>
      <navigator url="register" hover-class="none" class="zai-label">还没有账号？点此注册.</navigator>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      index: -1,
      picker: ['学生', '教师'],
    }
  },
  name: "login",
  methods: {
    PickerChange(e) {
      this.index = e.detail.value
    },
    login() {
      if(this.picker[this.index] == '学生'){
        uni.navigateTo({
          url: '/pages/index/index',
        });
      }
    }
  }
}
</script>

<style>
.zai-box{
  padding: 0 100upx;
  position: relative;
}
.zai-logo{
  width: 100%;
  width: 100%;
  height: 310upx;
}
.zai-title{
  position: absolute;
  top: 0;
  line-height: 360upx;
  font-size: 68upx;
  color: #fff;
  text-align: center;
  width: 100%;
  margin-left: -100upx;
}
.zai-form{
  margin-top: 300upx;
}
.zai-input{
  background: #e2f5fc;
  margin-top: 30upx;
  border-radius: 100upx;
  padding: 0 40upx;
  font-size: 36upx;
}
.input-placeholder, .zai-input{
  color: #94afce;
}
.zai-label{
  padding: 60upx 0;
  text-align: center;
  font-size: 30upx;
  color: #a7b6d0;
}
.zai-btn{
  background: #ff65a3;
  color: #fff;
  border: 0;
  border-radius: 100upx;
  font-size: 36upx;
}
.zai-btn:after{
  border: 0;
}
/*按钮点击效果*/
.zai-btn.button-hover{
  transform: translate(1upx, 1upx);
}
</style>
