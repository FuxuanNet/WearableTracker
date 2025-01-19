<script setup>
import { ref } from 'vue';
import ClothingCard from '@/components/ClothingCard.vue';

// 模拟数据
const clothingItems = ref([
    {
        id: 1,
        name: '蓝色条纹T恤',
        image: '/src/assets/clothes/blue-tshirt.jpg',
        category: '半袖',
        thickness: '常规',
        layer: '内层',
        set: '无',
        rating: 4,
        special: '',
        note: '很舒适的夏季T恤',
        status: 'stored', // 'stored' | 'washing' | 'drying' | 'wearing'
        isFavorite: false
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
        note: '',
        status: 'stored',
        isFavorite: false
    })
}

// 更新卡片
const handleUpdate = (index, newData) => {
    clothingItems.value[index] = { ...clothingItems.value[index], ...newData }
    // TODO: 调用后端API更新数据
    // await updateClothing(clothingItems.value[index])
}

// 删除卡片
const handleDelete = (index) => {
    clothingItems.value.splice(index, 1)
    // TODO: 调用后端API删除数据
    // await deleteClothing(id)
}

// 更新衣物状态
const handleStatusUpdate = (index, status) => {
    clothingItems.value[index] = {
        ...clothingItems.value[index],
        status
    }
    // TODO: 调用后端API更新状态
    // await updateClothingStatus(id, status)
}

// 更新收藏状态
const handleFavoriteUpdate = (index, isFavorite) => {
    clothingItems.value[index] = {
        ...clothingItems.value[index],
        isFavorite
    }
    // TODO: 调用后端API更新收藏状态
    // await updateClothingFavorite(id, isFavorite)
}
</script>

<template>
    <div class="page-container">
        <div class="header">
            <el-button type="primary" @click="handleAdd" plain>添加衣物</el-button>
        </div>
        <div class="cards-container">
            <template v-for="(item, index) in clothingItems" :key="item.id">
                <ClothingCard :item="item" @update="(newData) => handleUpdate(index, newData)"
                    @delete="() => handleDelete(index)" @status-update="(status) => handleStatusUpdate(index, status)"
                    @favorite-update="(isFavorite) => handleFavoriteUpdate(index, isFavorite)"></ClothingCard>
            </template>
        </div>
    </div>
</template>

<style scoped>
.page-container {
    padding: 20px 0;
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