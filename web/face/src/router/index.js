import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Test from '@/components/test'
import CourseList from '@/components/course_list'
import CourseCheck from '@/components/check_student'
import CheckDisplay from '@/components/check_display'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
    {
      path: '/course/list',
      name: 'CourseList',
      component: CourseList
    },
    {
      path: '/course/check',
      name: 'CourseCheck',
      component: CourseCheck
    },
    {
      path: '/check/list',
      name: 'CheckDisplay',
      component: CheckDisplay
    },
  ]
})
