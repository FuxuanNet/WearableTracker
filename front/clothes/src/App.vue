<script setup>
import { ref, computed } from 'vue'
import Aside from './components/AsideMenu.vue'

// 侧边栏的展开和收起
const isCollapse = ref(false)
const asideWidth = computed(() => isCollapse.value ? '64px' : '200px')

const handleCollapse = (collapsed) => {
  isCollapse.value = collapsed
}
</script>

<template>
  <el-container class="layout-container">
    <el-aside :width="asideWidth" class="aside" :class="{ 'is-collapsed': isCollapse }">
      <!-- :collapse="isCollapse" 父组件向子组件传递数据（称为 props） -->
      <Aside :collapse="isCollapse" @update:collapse="handleCollapse" />
      <!-- @update:collapse="handleCollapse" 是监听子组件发出的事件 -->

    </el-aside>

    <el-container class="content-container">
      <el-header class="header">
      </el-header>

      <el-main class="main" style="height: 1500px;">
        <router-view></router-view>
        <div>
        </div>
      </el-main>

      <el-footer class="footer">
        Footer
      </el-footer>
    </el-container>
  </el-container>
</template>

<style scoped>
.layout-container {
  height: 100vh;
}

.aside {
  transition: width 0.3s;
  background-color: var(--el-menu-bg-color);
  border-right: 1px solid var(--el-border-color-light);
}

.aside.is-collapsed {
  width: 70px;
}

.content-container {
  height: 100%;
}

.header {
  height: 60px;
  background-color: var(--el-color-primary-light-9);
  border-bottom: 1px solid var(--el-border-color-light);
  display: flex;
  align-items: center;
}

.main {
  padding: 20px;
  background-color: #eee;
  display: flex;
  align-items: flex-start;
  justify-content:flex-start;
  flex-direction: column;
}

.footer {
  height: 60px;
  background-color: var(--el-color-primary-light-9);
  border-top: 1px solid var(--el-border-color-light);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>