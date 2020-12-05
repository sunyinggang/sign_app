<template>
	<view class="content">
		<view class="input-group">
			<view class="input-row border">
				<text class="title">姓名：</text>
				<m-input class="m-input" type="text" clearable focus v-model="name" placeholder="请输入姓名"></m-input>
			</view>
			<view class="input-row">
				<text class="title">身份证号：</text>
				<m-input type="text" clearable focus v-model="cardnum" placeholder="请输入身份证号"></m-input>
			</view>
		</view>
		<view class="btn-row">
			<button type="primary" class="primary" @click="goFaceVerify">启动核验</button>
		</view>
	</view>
</template>

<script>
	import {
		mapState,
		mapMutations
	} from 'vuex'
	import mInput from '../../components/m-input.vue'

	export default {
		components: {
			mInput
		},
		data() {
			return {
				name: '',
				cardnum: '',
				appId:'TIDA0001', 	// appId 腾讯云注册分配
									//keyLicence 腾讯云注册分配
				keyLicence:'NwKivlx4CuaA0r1Ri/x7VGugcN5bfIUm9Q0ZfUHmr2R6mjwuZUGRUNL+ydQhfRjaCl4s+YdUnVPxGGBfxCeSYpHk0AZIRUHUy5TETKUlSKrolSR+svPde8ZImxQhXIK5Tyr+zweHGZpPzOsuYglLuPeECYNGtDfw+4pTEIXFkwBbUMuoAt/RcLBxGpjB8Ol5meMP/8A10YfWJwPvuhVttMxXX7fIqPVxrC7bMRG8Y0AXUJQtJmFR8u35BvCY1YZYrQ3puOHTVvAdOJH53+w+kKVt1sMzVaa/1qnjgNHtC8DkHJ6+FJx5nOn2Etah7oWKE4dQrd+HOjXQeWFRdb9/ww==',
				userId:'',
				nonce:'',
				sign:'',
				//data_mode_act_desense 	动作活体
				//data_mode_num 			数字活体
				//data_mode_reflect_desense 光线活体
				facetype:'data_mode_num'				
			}
		},
		methods: {
			goFaceVerify(){
				try{				
					if (this.name === '' || this.cardnum === '') {
						uni.showModal({
							content: '输入姓名和身份证号',
							showCancel: false
						});
						return;
					}
					if (!(/(^\d{15}$)|(^\d{17}([0-9]|X)$)/i.test(this.cardnum))) {
						uni.showToast({
							title: '身份证号校验失败!',
							icon: 'none'
						});
						return
					}					
					this.userId= this.guid();
					this.nonce='52014832029547845621032584562012'; 
					//测试签名请使用这个地址拼接获取 直接浏览器中获取
					//var url='https://ida.webank.com/ems-partner/cert/signature?appid=' + this.appId + '&nonce=' + this.nonce + '&userid=' + this.userId;
					//如   https://ida.webank.com/ems-partner/cert/signature?appid=TIDA0001&nonce=52014832029547845621032584562012&userid=415469909ac54e48be47a1eb00e8e337
					//结果 {"code":null,"msg":null,"sign":"300392346177BC1BC97B94F39040D16263FE6636","faceId":null}
					this.sign="300392346177BC1BC97B94F39040D16263FE6636";
					//引入插件
					const tencentFace = uni.requireNativePlugin('Tencent-Face');
					tencentFace.goFaceVerify({
						sign:  	this.sign,
						appid: 	this.appId,
						userid:	this.userId,
						nonce: 	this.nonce,
						name:  	this.name,
						cardnum:	this.cardnum,
						facetype:	this.facetype ,
						keyLicence:	this.keyLicence
					}, data => {								
						if(data.result.success === true) {
							uni.showModal({
								content: '核验通过',
								showCancel: false
							});
						}
						else {
							uni.showModal({
								content: '核验不通过',
								showCancel: false
							});
						}								
					});
				}catch(e){
					//TODO handle the exception
					uni.showModal({
						content: e.message,
						showCancel: false
					});
				}
				
			},
			 guid(){
				return 'xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
					var r = Math.random() * 16 | 0,
						v = c == 'x' ? r : (r & 0x3 | 0x8);
					return v.toString(16);
				});
			}
		}
	}
</script>

<style>
	.action-row {
		display: flex;
		flex-direction: row;
		justify-content: center;
	}

	.action-row navigator {
		color: #007aff;
		padding: 0 20upx;
	}

	.oauth-row {
		display: flex;
		flex-direction: row;
		justify-content: center;
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
	}

	.oauth-image {
		width: 100upx;
		height: 100upx;
		border: 1upx solid #dddddd;
		border-radius: 100upx;
		margin: 0 40upx;
		background-color: #ffffff;
	}

	.oauth-image image {
		width: 60upx;
		height: 60upx;
		margin: 20upx;
	}
</style>
