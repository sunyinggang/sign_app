<template>
  <view>
    <view class="cu-bar search bg-white" style="height: 180upx;">
      <view class="search-form round">
        <text class="cuIcon-search"></text>
        <input @focus="InputFocus" @blur="InputBlur" :adjust-position="false" type="text" placeholder="搜索课程" confirm-type="search"></input>
      </view>
      <view class="action">
        <button class="cu-btn bg-green shadow-blur round">搜索</button>
      </view>
    </view>
    <view class="cu-list menu">
      <view class="cu-item margin radius" style="height: 140upx;">
        <view class="content">
          <view>
            <text class="cuIcon-tagfill text-red  margin-right-xs"></text>
            <text class="text-grey">高级计算机网络</text>
          </view>
          <view class="text-gray text-sm">
            <text class="cuIcon-time margin-right-xs"></text> 8:00-10:00
            <view class="cu-tag sm round bg-orange light">F501</view>
            <view class="cu-tag sm round bg-olive light">周三</view>
          </view>
        </view>
        <view class="action">
          <view class="cu-tag round bg-blue light" @tap="showModal"  data-target="DialogModal1">选择</view>
        </view>
      </view>
      <view class="cu-item margin radius" style="height: 140upx;">
        <view class="content">
          <view>
            <text class="cuIcon-tagfill text-red  margin-right-xs"></text>
            <text class="text-grey">高级计算机网络</text>
          </view>
          <view class="text-gray text-sm">
            <text class="cuIcon-time margin-right-xs"></text> 8:00-10:00
            <view class="cu-tag sm round bg-orange light">F501</view>
            <view class="cu-tag sm round bg-olive light">周三</view>
          </view>
        </view>
        <view class="action">
          <view class="cu-tag round bg-blue light" @tap="showModal"  data-target="DialogModal1">选择</view>
        </view>
      </view>
      <view class="cu-item margin radius" style="height: 140upx;">
        <view class="content">
          <view>
            <text class="cuIcon-tagfill text-red  margin-right-xs"></text>
            <text class="text-grey">高级计算机网络</text>
          </view>
          <view class="text-gray text-sm">
            <text class="cuIcon-time margin-right-xs"></text> 8:00-10:00
            <view class="cu-tag sm round bg-orange light">F501</view>
            <view class="cu-tag sm round bg-olive light">周三</view>
          </view>
        </view>
        <view class="action">
          <view class="cu-tag round bg-blue light" @tap="showModal"  data-target="DialogModal1">选择</view>
        </view>
      </view>
      <view class="cu-item margin radius" style="height: 140upx;">
        <view class="content">
          <view>
            <text class="cuIcon-tagfill text-red  margin-right-xs"></text>
            <text class="text-grey">高级计算机网络</text>
          </view>
          <view class="text-gray text-sm">
            <text class="cuIcon-time margin-right-xs"></text> 8:00-10:00
            <view class="cu-tag sm round bg-orange light">F501</view>
            <view class="cu-tag sm round bg-olive light">周三</view>
          </view>
        </view>
        <view class="action">
          <view class="cu-tag round bg-blue light" @tap="showModal"  data-target="DialogModal1">选择</view>
        </view>
      </view>
      <view class="cu-item margin radius" style="height: 140upx;">
        <view class="content">
          <view>
            <text class="cuIcon-tagfill text-red  margin-right-xs"></text>
            <text class="text-grey">高级计算机网络</text>
          </view>
          <view class="text-gray text-sm">
            <text class="cuIcon-time margin-right-xs"></text> 8:00-10:00
            <view class="cu-tag sm round bg-orange light">F501</view>
            <view class="cu-tag sm round bg-olive light">周三</view>
          </view>
        </view>
        <view class="action">
          <view class="cu-tag round bg-blue light" @tap="showModal"  data-target="DialogModal1">选择</view>
        </view>
      </view>
    </view>
    <view class="cu-modal" :class="modalName=='DialogModal1'?'show':''">
      <view class="cu-dialog">
        <view class="cu-bar bg-white justify-end">
          <view class="content">提醒</view>
          <view class="action" @tap="hideModal">
            <text class="cuIcon-close text-red"></text>
          </view>
        </view>
        <view class="padding-xl">
          课程选择后无法修改，是否确认选择此课程
        </view>
        <view class="cu-bar bg-white justify-end">
          <view class="action">
            <button class="cu-btn line-green text-green" @tap="hideModal">取消</button>
            <button class="cu-btn bg-green margin-left" @tap="hideModal">确定</button>
          </view>
        </view>
      </view>
    </view>
  </view>

</template>

<script>
export default {
  name: "select",
  data() {
    return {
      modalName: null,
    }
  },
  methods: {
    showModal(e) {
      this.modalName = e.currentTarget.dataset.target
    },
    hideModal(e) {
      this.modalName = null
    },
  }
}
</script>

<style scoped>

</style>
