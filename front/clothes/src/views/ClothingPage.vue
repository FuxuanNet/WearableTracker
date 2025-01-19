<script setup>
import { ref } from 'vue'
import MainMenu from '../components/MainMenu.vue'

const menuItems = [
    { name: '全部衣物', index: '/Clothing/' },
    { name: '在洗衣物', index: '/Clothing/Drying' },
    { name: '晾晒衣物', index: '/Clothing/Sunning' },
    { name: '收藏衣物', index: '/Clothing/Favorite' },
]
const handleMenuSelect = (index) => {
    console.log('选中的菜单项索引:', index)
}

const activeIndex = '/Clothing/' // 设置默认激活的菜单项索引

</script>

<template>
    <MainMenu :menuItems="menuItems" :activeIndex="activeIndex" @select="handleMenuSelect" />
    <router-view></router-view>
</template>

<style scoped>
</style>