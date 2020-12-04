<template>
  <view>
    <course v-if="PageCur=='course'"></course>
    <curriculum v-if="PageCur=='curriculum'"></curriculum>
    <user v-if="PageCur=='user'"></user>
    <view class="cu-bar tabbar bg-white shadow foot">
      <view class="action" @click="NavChange" data-cur="course">
        <view class='cuIcon-cu-image'>
          <image :src="'/static/tabbar/course' + [PageCur=='course'?'_cur':''] + '.png'"></image>
        </view>
        <view :class="PageCur=='course'?'text-green':'text-gray'">课程</view>
      </view>
      <view class="action" @click="NavChange" data-cur="curriculum">
        <view class='cuIcon-cu-image'>
          <image :src="'/static/tabbar/curriculum' + [PageCur == 'curriculum'?'_cur':''] + '.png'"></image>
        </view>
        <view :class="PageCur=='curriculum'?'text-green':'text-gray'">课表</view>
      </view>
      <view class="action" @click="NavChange" data-cur="user">
        <view class='cuIcon-cu-image'>
          <image :src="'/static/tabbar/user' + [PageCur == 'user'?'_cur':''] + '.png'"></image>
        </view>
        <view :class="PageCur=='user'?'text-green':'text-gray'">个人 </view>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      PageCur: 'course'
    }
  },
  methods: {
    NavChange: function(e) {
      this.PageCur = e.currentTarget.dataset.cur
    }
  }
}
</script>

<style>

</style>
