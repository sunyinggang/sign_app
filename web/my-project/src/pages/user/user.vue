<template>
  <view>
    <view class="header">
      <view class="bg">
        <view class="box">
          <view class="box-hd">
            <view class="avator">
              <img src="../../static/user/face.jpg">
            </view>
            <view class="phone-number">张三</view>
          </view>
          <view class="box-bd">
            <view class="item">
              <view class="text">11</view>
              <view class="text-sm">已选课程</view>
            </view>
            <view class="item">
              <view class="text">0</view>
              <view class="text-sm">迟到次数</view>
            </view>
            <view class="item">
              <view class="text-center text-blue text">
                <text class=" cuIcon-roundcheckfill text-green"></text>
              </view>
              <view class="text-sm">认证状态</view>
            </view>
          </view>
        </view>
      </view>
    </view>
    <view class="list-content">
      <view class="list">
        <view class="li noborder" >
        </view>
      </view>
      <view class="list">
        <view class="list">
          <view class="li noborder" >
            <view class="icon"><image src="../../static/user/card.png"></image></view>
            <view class="text">认证信息</view>
            <image class="to" src="../../static/user/to.png"></image>
          </view>
        </view>
        <view class="li " >
          <view class="icon"><image src="../../static/user/help.png"></image></view>
          <view class="text">选课中心</view>
          <image class="to" src="../../static/user/to.png"></image>
        </view>
        <view class="li " >
          <view class="icon"><image src="../../static/user/about.png"></image></view>
          <view class="text">关于我们</view>
          <image class="to" src="../../static/user/to.png"></image>
        </view>
        <view class="li " >
          <view class="icon"><image src="../../static/user/opinion.png"></image></view>
          <view class="text">意见反馈</view>
          <image class="to" src="../../static/user/to.png"></image>
        </view>
      </view>
      <view class="list">
        <view class="li noborder" >
          <view class="icon"><image src="../../static/user/set.png"></image></view>
          <navigator url="../index/index"  class="text">设置</navigator>
          <image class="to" src="../../static/user/to.png"></image>
        </view>
      </view>
    </view>
  </view>
</template>
<script>
export default {
  name: "user",
  data() {
    return {
    };
  },
  onLoad() {
  }
}
</script>

<style lang="scss">
page{
  background-color:#f1f1f1;
  font-size: 30upx;
}
.header{
  background: #fff;
  height: 290upx;
  padding-bottom: 110upx;
  .bg{
    width: 100%;
    height:200upx;
    padding-top:140upx;
    background-color:#4191ea;
  }
}
.box{
  width: 650upx;
  height: 280upx;
  border-radius: 20upx;
  margin: 0 auto;
  background: #fff;
  box-shadow: 0 5upx 20upx 0upx rgba(0, 0, 150, .2);
  .box-hd{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: center;
    .avator{
      width: 160upx;
      height: 160upx;
      background: #fff;
      border: 5upx solid #fff;
      border-radius: 50%;
      margin-top: -80upx;
      overflow: hidden;
      img{
        width: 100%;
        height: 100%;
      }
    }
    .phone-number{
      width: 100%;
      text-align: center;
    }
  }
  .box-bd{
    display: flex;
    flex-wrap: nowrap;
    flex-direction: row;
    justify-content: center;
    .item{
      flex: 1 1 auto;
      display: flex;
      flex-wrap: wrap;
      flex-direction: row;
      justify-content: center;
      border-right: 1px solid #f1f1f1;
      margin: 15upx 0;
      &:last-child{
        border: none;
      }
      .icon{
        width: 60upx;
        height: 60upx;
        img{
          width: 100%;
          height: 100%;
        }
      }
      .text{
        width: 100%;
        text-align: center;
        margin-top: 10upx;
      }
    }
  }
}
.list-content{
  background: #fff;
}
.list{
  width:100%;
  border-bottom:15upx solid  #f1f1f1;
  background: #fff;
  &:last-child{
    border: none;
  }
  .li{
    width:92%;
    height:100upx;
    padding:0 4%;
    border-bottom:1px solid rgb(243,243,243);
    display:flex;
    align-items:center;
    &.noborder{
      border-bottom:0
    }
    .icon{
      flex-shrink:0;
      width:50upx;
      height:50upx;
      image{
        width:50upx;
        height:50upx;
      }
    }
    .text{
      padding-left:20upx;
      width:100%;
      color:#666;
    }
    .to{
      flex-shrink:0;
      width:40upx;
      height:40upx;
    }
  }
}
</style>

