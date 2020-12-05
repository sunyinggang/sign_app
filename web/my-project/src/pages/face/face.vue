<template>
  <view>
    <div class="custom" :style="{height: CustomBar+'px'}">
      <view class="navcontent" :style="[{top:statusBar + 'px'}]">
        <text style="color: #FFFFFF;font-size: 16px;line-height: 45px;" class="iconfont icon-xiangzuo" @click="BackPage">返回</text>
        <text style="color: #FFFFFF;font-size: 16px;line-height: 45px;">人脸识别</text>
        <text></text>
      </view>
    </div>

    <div class="livefater">
      <div style="width: 350px;height: 350px;border-radius: 350px;overflow: hidden;background-color: #CCCCCC;">
        <live-pusher id='livePusher' ref="livePusher" class="livePusher" url=""
                     mode="SD" :muted="true" :enable-camera="true" :auto-focus="true" :beauty="1" whiteness="2"
                     aspect="1:1" @statechange="statechange" @netstatus="netstatus" @error = "error"
        ></live-pusher>
      </div>
      <cover-image src="/static/gai.png" class="gaiimg"></cover-image>
    </div>
    <button class="btn" @click="startPreview">打开摄像头进行人脸识别</button>
  </view>
</template>

<script>
export default {
  data() {
    return{
    fil: true,
    imgList:[""],
    statusBar:'',
    CustomBar: 0
  }
  },
  onLoad(){
    // this.startPreview()
  },
  onReady() {
    // 注意：需要在onReady中 或 onLoad 延时
    this.context = uni.createLivePusherContext("livePusher", this);
    var that = this
    uni.getSystemInfo({
      success:function(e){
        // 计算导航栏高度
        that.statusBar = e.statusBarHeight
        // #ifndef MP
        if(e.platform == 'android') {
          that.CustomBar = e.statusBarHeight + 50
        }else {
          that.CustomBar = e.statusBarHeight + 45
        }
        console.log(that.statusBar)
        // #endif
        // #ifdef MP-WEIXIN
        let custom = wx.getMenuButtonBoundingClientRect()
        that.CustomBar = custom.bottom + custom.top - e.statusBarHeight

        // #endif

        // #ifdef MP-ALIPAY
        that.CustomBar = e.statusBarHeight + e.titleBarHeight
        // #endif
      }
    })
  },
  methods: {
    Timer(){},
    statechange(e) {
      console.log("statechange:" + JSON.stringify(e));
    },
    netstatus(e) {
      console.log("netstatus:" + JSON.stringify(e));
    },
    error(e) {
      console.log("error:" + JSON.stringify(e));
    },
    start: function() {
      this.context.start({
        success: (a) => {
          console.log("livePusher.start:" + JSON.stringify(a));
        }
      });
    },
    close: function() {
      this.context.close({
        success: (a) => {
          console.log("livePusher.close:" + JSON.stringify(a));
        }
      });
    },
    // 拍照事件
    snapshot: function() {
      var that = this
      this.context.snapshot({
        success: (e) => {
          console.log(JSON.stringify(e));
          that.getMinImage(e.message.tempImagePath)
        }
      });
    },
    // 开启摄像头
    startPreview() {
      console.log("1")
      var that = this
      this.context.startPreview({
        success: (a) => {
          console.log("livePusher.startPreview:" + JSON.stringify(a));
          that.Timer = setInterval(function(){
            that.snapshot()
            if(that.imgList.length>3){
              console.log("3")
              clearInterval(that.Timer)
            }
          },2000)
        }
      });
    },
    // 使用plus.zip.compressImage压缩图片并转换成base64
    getMinImage(imgPath) {
      plus.zip.compressImage(
          {
            src: imgPath,
            dst: imgPath,
            overwrite: true,
            quality: 40
          },
          zipRes => {
            setTimeout(() => {
              var reader = new plus.io.FileReader();
              reader.onloadend = res => {
                var speech = res.target.result; //base64图片
                console.log(speech);
                this.imgList.push(speech);
              };
              //一定要使用plus.io.convertLocalFileSystemURL将target地址转换为本地文件地址，否则readAsDataURL会找不到文件
              reader.readAsDataURL(plus.io.convertLocalFileSystemURL(zipRes.target));
            }, 1000);
          },
          function(error) {
            console.log('Compress error!', error);
          }
      );
    },
    BackPage() {
      uni.navigateBack({
        delta: 1
      });
    }

  }
}
</script>

<style scoped>
.custom{
  background-color: #2C65F7;
}
.navcontent{
  height: 45px;
  display: -ms-flex;
  display: -webkit-flex;
  display: flex;
  justify-content:space-around;
  flex-direction:row;
  color:#FFFFFF;
}
.livePusher{
  width: 350px;
  height: 350px;
}
.livefater{
  display: -ms-flex;
  display: -webkit-flex;
  display: flex;
  justify-content:center;
  flex-direction:column;
  align-items:center;
  margin-top: 50rpx;
  margin-bottom: 50rpx;
  height: 350px;
}
.gaiimg{
  width: 350px;
  height: 350px;
  margin-top: -350px;
}
</style>
