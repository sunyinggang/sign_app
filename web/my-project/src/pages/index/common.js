// 时间戳转 yyyy-mm-dd格式
export const formatDayTime = (val) => {
    if (val) {
        let date = new Date(val);
        let Y = date.getFullYear();
        let M = date.getMonth() + 1;
        let D = date.getDate();

        if (M < 10) {
            M = '0' + M;
        }
        if (D < 10) {
            D = '0' + D;
        }

        return Y + '-' + M + '-' + D;
    } else {
        return '';
    }
}


// 课表
// import http from '@/request-interceptor/interceptor.js'
// import {
// 	wx
// } from '@/api/index.js'

// // 获取老师课程表
// export const teacherData = (data) => {
// 	return http.request({
// 		url: wx + '/course/teacherCourse',
// 		method:'GET',
// 		data:data.data
// 	})
// }
