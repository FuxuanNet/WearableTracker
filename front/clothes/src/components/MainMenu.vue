<script setup>
const props = defineProps({
    // 菜单项数组，每项包含 name（显示文本）和 index（路由或唯一标识）
    menuItems: {
        type: Array,
        required: true,
        // 数组中每一项的格式示例：{ name: '菜单1', index: '1' }
        validator: (value) => {
            return value.every(item => item.name && item.index)
        }
    },
    // 当前激活的菜单项索引
    activeIndex: {
        type: String,
        default: '1'
    }
})

// 菜单项点击事件
const emit = defineEmits(['select'])
const handleSelect = (index) => {
    emit('select', index)
}
</script>

<template>
    <div class="menu-container">
        <el-menu :default-active="activeIndex" class="horizontal-menu" mode="horizontal" @select="handleSelect" router="true">
            <el-menu-item v-for="item in menuItems" :key="item.index" :index="item.index">
                {{ item.name }}
            </el-menu-item>
        </el-menu>
    </div>
</template>

<style scoped>
.menu-container {
    width: 100%;
    /* 固定宽度 */
    height: 60px;
    /* 固定高度 */
    background-color: var(--el-menu-bg-color);
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
}

.horizontal-menu {
    height: 100%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

/* :deep(.el-menu-item) {
    height: 100%;
    display: flex;
    align-items: center;
} */
</style>