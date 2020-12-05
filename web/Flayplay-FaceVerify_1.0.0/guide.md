# 引导页

###  腾讯云人脸核验插件

> nativeplugins/Tencent-Face/android 目录下tencentfaceverify-release.aar是对应插件

> WbCloudFaceLiveSdk-v3.0.10-7e6b5f1.aar,WbCloudNormal-v4.0.5-4912a99.aar 是调用腾讯的两个插件

> 因工作繁忙目前该程序金对安卓做了适配，IOS暂未开发，后期将继续开发。谢谢

> main.vue 为示意代码 需要申请腾讯云账号

```javascript
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
```