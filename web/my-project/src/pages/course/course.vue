<template>
<view>
  <view class="bg bg-gradual-blue">
    <view class="padding-xl text-white">
      <view class="padding-xs text-lg">
        12月4日
      </view>
      <view class="padding-xs text-xxl text-bold">
        星期五
      </view>
    </view>
    <view class="cu-timeline box">
      <view class="cu-time">今日课程</view>
      <view class="cu-item cur text-green cuIcon-noticefill">
        <view class="content bg-green shadow-blur">
          <text>签到时间</text>
        </view>
      </view>
      <view class="cu-item text-blue">
        <view class="content radius shadow-warp bg-white margin-top">
          <view class="cu-tag line-cyan radius">
            <view class=""><text class="lg text-cyan line-cyan cuIcon-time"></text></view>
            <view class="line-cyan">10:00-12:00</view>
          </view>
          <view class="margin-top text-grey">
            <text class="text-bold">课程：</text>
            <text>数据库</text>
          </view>
          <view class="text-grey">
            <text class="text-bold">地点：</text>
            <text>数据库</text>
          </view>
        </view>
      </view>
      <view class="cu-item text-blue">
        <view class="content radius shadow-warp bg-white margin-top">
          <view class="cu-tag line-cyan radius">
            <view class=""><text class="lg text-cyan line-cyan  cuIcon-time"></text></view>
            <view class="line-cyan">10:00-12:00</view>
          </view>
          <view class="margin-top text-grey">课程：数据库</view>
          <view class="text-grey">地点：数据库</view>
        </view>
      </view>
      <view class="cu-item text-blue">
        <view class="content radius shadow-warp bg-white margin-top">
          <view class="cu-tag line-cyan radius">
            <view class=""><text class="lg text-cyan line-cyan  cuIcon-time"></text></view>
            <view class="line-cyan">10:00-12:00</view>
          </view>
          <view class="margin-top text-grey">课程：数据库</view>
          <view class="text-grey">地点：数据库</view>
        </view>
      </view>
    </view>
  </view>
</view>
</template>

<script>
export default {
name: "course"
}
</script>

<style scoped>
.bg{
  width: 100%;
  height: 100%;
  background-color:#4191ea;
}
.box{
  border-radius: 30upx 30upx 0 0 ;
  background-color:#f1f1f1;;
  padding-bottom: 80upx;
}
</style>
