<script setup>
import { ref, onMounted } from 'vue';
import ClothingCard from '@/components/ClothingCard.vue';
import { clothesApi } from '@/api';
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

// 获取所有衣物数据
const fetchClothes = async () => {
    try {
        const data = await clothesApi.getAll()
        clothingItems.value = data
    } catch (error) {
        console.error('获取衣物数据失败:', error)
    }
}

// 添加新衣物
const handleAdd = async () => {
    const newClothes = {
        name: '新衣物', // 默认名称
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
    }
    try {
        const addedClothes = await clothesApi.add(newClothes)
        clothingItems.value.push(addedClothes)
        ElMessage.success('添加衣物成功')
    } catch (error) {
        console.error('添加衣物失败:', error)
        ElMessage.error('添加衣物失败')
    }
}



// 更新卡片
const handleUpdate = async (index, newData) => {
    try {
        const updatedClothes = await clothesApi.update(newData.id, newData)
        clothingItems.value[index] = updatedClothes
    } catch (error) {
        console.error('更新衣物失败:', error)
    }
}

// 删除卡片
const handleDelete = async (index) => {
    const id = clothingItems.value[index].id
    try {
        await clothesApi.delete(id)
        clothingItems.value.splice(index, 1)
    } catch (error) {
        console.error('删除衣物失败:', error)
    }
}

// 更新衣物状态
const handleStatusUpdate = async (index, status) => {
    const id = clothingItems.value[index].id
    try {
        const updatedClothes = await clothesApi.updateStatus(id, status)
        clothingItems.value[index] = updatedClothes
    } catch (error) {
        console.error('更新状态失败:', error)
    }
}

// 更新收藏状态
const handleFavoriteUpdate = async (index, isFavorite) => {
    const id = clothingItems.value[index].id
    try {
        const updatedClothes = await clothesApi.updateFavorite(id, isFavorite)
        clothingItems.value[index] = updatedClothes
    } catch (error) {
        console.error('更新收藏状态失败:', error)
    }
}


// 组件挂载时获取数据
onMounted(() => {
    fetchClothes()
})

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