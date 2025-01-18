<script setup>
import MainMenu from '../components/MainMenu.vue'
import { ref } from 'vue'
import { ElMenuItem } from 'element-plus';

const countdownValue = ref(Date.now() + 40 * 60 * 1000) // 当前时间 + 40 分钟
const dryingClothesCount = ref(9)
const storedClothesCount = ref(9)
const wearingClothesCount = ref(9)

const menuItems = [
  { name: '概览', index: '/' }
]

const activeIndex = '/' // 设置默认激活的菜单项索引

// 监听菜单项的选择
const handleMenuSelect = (index) => {
  console.log('选中的菜单项索引:', index)
}
</script>

<template>
  <MainMenu :menuItems="menuItems" :activeIndex="activeIndex" @select="handleMenuSelect" />
  <div class="box">
    <h2>概览</h2>
    <div class="data-statistics">
      <div>
        <el-countdown title="在洗衣物" :value="countdownValue" />
      </div>
      <div>
        <el-statistic title="晾晒衣物" :value="dryingClothesCount" />
      </div>
      <div>
        <el-statistic title="存储衣物" :value="storedClothesCount" />
      </div>
      <div>
        <el-statistic title="在穿衣物" :value="wearingClothesCount" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.box {
  margin: 20px 0;
  padding-bottom: 40px;
  width: 100%;
  background-color: var(--el-menu-bg-color);
  border-radius: 0px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
}

.box h2 {
  font-size: 18px;
  font-weight: normal;
  padding-left: 7px;
  margin: 20px;
  border-left: 2px solid rgb(50.8, 116.6, 184.5);
}

.box div {
  text-align: center;
}

.box .data-statistics {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>
