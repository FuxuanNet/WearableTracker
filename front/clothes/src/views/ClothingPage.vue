<script setup>
import { ref } from 'vue'
import ClothingCard from '../components/ClothingCard.vue'
import MainMenu from '../components/MainMenu.vue'

const menuItems = [
    {
        name: '我的衣橱', index: '/Clothing'
    }
]
const handleMenuSelect = (index) => {
    console.log('选中的菜单项索引:', index)
}

const activeIndex = '/Clothing' // 设置默认激活的菜单项索引


// 模拟数据
const clothingItems = ref([
    {
        id: 1,
        name: '蓝色条纹T恤',
        image: '/src/assets/clothes/blue-tshirt.jpg',
        category: '半袖',
        thickness: '常规',
        layer: '内层',
        set: '',
        rating: 4,
        special: '',
        note: '很舒适的夏季T恤'
    },
    {
        id: 2,
        name: '黑色休闲裤',
        image: '/src/assets/clothes/black-pants.jpg',
        category: '长裤',
        thickness: '常规',
        layer: '外层',
        set: '搭配蓝色条纹T恤',
        rating: 5,
        special: '',
        note: '百搭款式'
    },
    // 可以添加更多示例数据
])

// 添加新卡片
const handleAdd = () => {
    clothingItems.value.push({
        id: Date.now(), // 临时ID
        name: '',
        image: '',
        category: '',
        thickness: '',
        layer: '',
        set: '',
        rating: 0,
        special: '',
        note: ''
    })
}

// 更新卡片
const handleUpdate = (index, newData) => {
    clothingItems.value[index] = { ...clothingItems.value[index], ...newData }
    // 这里应该调用API更新后端数据
}

// 删除卡片
const handleDelete = (index) => {
    clothingItems.value.splice(index, 1)
    // 这里应该调用API删除后端数据
}
</script>

<template>
    <MainMenu :menuItems="menuItems" :activeIndex="activeIndex" @select="handleMenuSelect" />
    <div class="page-container">
        <div class="header">
            <el-button type="primary" @click="handleAdd">
                添加衣物
            </el-button>
        </div>

        <div class="cards-container">
            <template v-for="(item, index) in clothingItems" :key="item.id">
                <ClothingCard :item="item" @update="(newData) => handleUpdate(index, newData)"
                    @delete="() => handleDelete(index)" />
            </template>
        </div>
    </div>
</template>

<style scoped>
.page-container {
    padding: 20px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.cards-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
</style>