<!--本页面由uniapp切片工具生成，uni-app切片-可视化设计工具(一套代码编译到7个平台iOS、Android、H5、小程序)，软件下载地址：http://www.ymznkf.com/new_view_669.htm -->
<template>
	<view class="YmContent">
			<view class="info_96">
				<view class="info_61">
					<text decode="true" class="info_62">头像</text>
					<image v-on:click="photo_63_click()"  src="/static/info/images/info_photo_63.jpg" mode="scaleToFill" border="0"    class="photo"></image>
				</view>
				<view class="info_64">
				</view>
				<view v-on:click="row4_65_click()" class="row4">
					<text decode="true" class="info_66">姓名</text>
					<text decode="true" class="name">吴福林</text>
					<image v-on:click="info_68_68_click()"  src="/static/info/images/info_68_68.jpg" mode="scaleToFill" border="0"    class="info_68"></image>
				</view>
				<view class="info_69">
				</view>
				<view v-on:click="row3_70_click()" class="row3">
					<text decode="true" class="info_71">身份证</text>
					<text decode="true" class="ids">请填写身份证号</text>
					<image v-on:click="info_73_73_click()"  src="/static/info/images/info_73_73.jpg" mode="scaleToFill" border="0"    class="info_73"></image>
				</view>
				<view class="info_74">
				</view>
				<view v-on:click="row2_75_click()" class="row2">
					<text decode="true" class="info_76">手机号码</text>
					<text decode="true" class="mobile">13982056253</text>
				</view>
				<view class="info_79">
				</view>
				<view v-on:click="row1_80_click()" class="row1">
					<text decode="true" class="info_81">科室岗位</text>
					<text decode="true" class="job">外科>主任医生</text>
				</view>
				<view class="info_83">
				</view>
			</view>
		

		<view class="loading">{{loadingText}}</view>
		<view class="ymBbottom"></view>
	</view>
</template>

<script>
import info from "./info.js";
export default info;
</script>

<style lang="scss" scoped>
   @import './info.scss'
</style>