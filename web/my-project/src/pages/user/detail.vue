<template>
<view>
  <view class="cu-bar bg-white solid-bottom" style="height: 160upx;">
    <view class="action">
      <text class='cuIcon-title text-blue'></text>认证信息
    </view>
  </view>
  <view v-if="info">
    <form>
      <view class="cu-form-group margin-top">
        <view class="title">姓名</view>
        <input placeholder="请输入真实姓名" name="input"></input>
      </view>
      <view class="cu-form-group">
        <view class="title">学号</view>
        <input placeholder="" name="input"></input>
      </view>
      <view class="cu-form-group">
        <view class="title">学校</view>
        <input placeholder="" name="input"></input>
      </view>
      <view class="cu-form-group">
        <view class="title">院系</view>
        <input placeholder="" name="input"></input>
      </view>
      <view class="cu-form-group">
        <view class="title">班级</view>
        <input placeholder="" name="input"></input>
      </view>
      <view class="cu-form-group">
        <view class="title">身份证号</view>
        <input placeholder="输入18位身份证号" name="input"></input>
      </view>
      <view class="cu-form-group">
        <view class="title">生源地</view>
        <input placeholder="输入框带个图标" name="input"></input>
        <text class='cuIcon-locationfill text-orange'></text>
      </view>
      <view class="cu-form-group">
        <view class="title">手机号码</view>
        <input placeholder="" name="input"></input>
        <view class="cu-capsule radius">
          <view class='cu-tag bg-blue '>
            +86
          </view>
          <view class="cu-tag line-blue">
            中国大陆
          </view>
        </view>
      </view>
      <view class="cu-bar bg-white margin-top">
        <view class="action">
          头像上传
        </view>
      </view>
      <view class="cu-form-group">
        <view class="grid col-4 grid-square flex-sub">
          <view class="bg-img" v-for="(item,index) in imgList" :key="index" @tap="ViewImage" :data-url="imgList[index]">
            <image :src="imgList[index]" mode="aspectFill"></image>
            <view class="cu-tag bg-red" @tap.stop="DelImg" :data-index="index">
              <text class='cuIcon-close'></text>
            </view>
          </view>
          <view class="solids" @tap="ChooseImage" v-if="imgList.length<4">
            <text class='cuIcon-cameraadd'></text>
          </view>
        </view>
      </view>
    </form>
    <view class="padding flex flex-direction">
      <button class="cu-btn bg-blue lg">确认提交</button>
    </view>
  </view>
  <view v-else>
    <view class="padding flex flex-direction">
      <button class="cu-btn bg-grey lg" @click="writeInfo()">未添加认证信息，点击添加</button>
    </view>
  </view>
</view>
</template>

<script>
export default {
  name: "detail",
  data() {
    return {
      info: false,
      imgList: [],
    }
  },
  methods: {
    writeInfo() {
      this.info = true
    },
    ChooseImage() {
      uni.chooseImage({
        count: 4, //默认9
        sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
        sourceType: ['album'], //从相册选择
        success: (res) => {
          if (this.imgList.length != 0) {
            this.imgList = this.imgList.concat(res.tempFilePaths)
          } else {
            this.imgList = res.tempFilePaths
          }
        }
      });
    },
    ViewImage(e) {
      uni.previewImage({
        urls: this.imgList,
        current: e.currentTarget.dataset.url
      });
    },
    DelImg(e) {
      uni.showModal({
        title: '提醒',
        content: '确定要删除此照片？',
        cancelText: '再看看',
        confirmText: '删除',
        success: res => {
          if (res.confirm) {
            this.imgList.splice(e.currentTarget.dataset.index, 1)
          }
        }
      })
    },
  }
}
</script>

<style scoped>

</style>
