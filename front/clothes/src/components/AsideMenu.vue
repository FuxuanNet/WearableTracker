<script setup>
import { ref } from 'vue'
import { Fold, Expand } from '@element-plus/icons-vue'

const props = defineProps({
    collapse: {             // 折叠
        type: Boolean,
        default: false
    }
})

const emit = defineEmits(['update:collapse'])

const activeIndex = ref('/')

const WebTitle = ref('衣物管理系统')

const handleCollapse = () => {
    emit('update:collapse', !props.collapse)
}

const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
}

const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
}
</script>

<template>
    <div class="aside-container">
        <el-menu :default-active="activeIndex" class="aside-menu" :collapse="collapse" @open="handleOpen"
            @close="handleClose" router>
            <el-menu-item index="/" class="logo-container">
                <el-icon>
                    <House />
                </el-icon>
                <template #title>
                    <span class="logo-text">{{ WebTitle }}</span>
                </template>
            </el-menu-item>

            <el-menu-item index="/">
                <el-icon>
                    <House />
                </el-icon>
                <template #title>概览</template>
            </el-menu-item>

            <el-menu-item index="Clothing">
                <el-icon>
                    <Goods />
                </el-icon>
                <template #title>我的衣橱</template>
            </el-menu-item>

            <el-sub-menu index="3">
                <template #title>
                    <el-icon>
                        <Picture />
                    </el-icon>
                    <span>今日搭配</span>
                </template>
                <el-menu-item index="3-1">当前搭配</el-menu-item>
                <el-menu-item index="3-2">历史搭配</el-menu-item>
                <el-menu-item index="3-3">我的收藏</el-menu-item>
            </el-sub-menu>

            <el-menu-item index="4">
                <el-icon>
                    <Location />
                </el-icon>
                <template #title>位置查询</template>
            </el-menu-item>
        </el-menu>

        <div class="collapse-trigger">
            <el-button :icon="collapse ? Expand : Fold" circle @click="handleCollapse" />
        </div>
    </div>
</template>

<style scoped>
.aside-container {
    height: 100%;
    position: relative;
    overflow: hidden;
}

.aside-menu {
    border-right: none;
    height: 100%;
}

.aside-menu:not(.el-menu--collapse) {
    width: 200px;
}

.logo-container {
    height: 60px;
    display: flex;
    align-items: center;
    padding: 0 20px;
}

.logo-text {
    font-size: 18px;
    font-weight: bold;
    color: var(--el-menu-active-color);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.collapse-trigger {
    position: absolute;
    margin: 20px;
    bottom: 30px;
    z-index: 1;
}
</style>