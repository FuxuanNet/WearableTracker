<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
    // 卡片数据
    item: {
        type: Object,
        required: true
    },
    // 是否处于编辑模式
    isEditing: {
        type: Boolean,
        default: false
    }
})

const emit = defineEmits(['update', 'delete', 'status-update', 'favorite-update'])

// 编辑状态
const isEditMode = ref(false)

// 编辑状态的临时数据
const editData = ref({ ...props.item })

// 类别选项
const categoryOptions = ['半袖', '长袖', '短裤', '长裤']

// 厚度选项
const thicknessOptions = ['薄款', '常规', '加厚']

// 层数选项
const layerOptions = ['内层', '中层', '外层']

// 特殊属性选项
const specialOptions = ['睡衣', '睡裤', '泳衣', '泳裤', '线衣', '线裤']

// 计算属性：按钮状态
const wearingButtonText = computed(() => {
    return props.item.status === 'wearing' ? '在穿' : '穿着'
})

const washingButtonText = computed(() => {
    return props.item.status === 'washing' ? '在洗' : '洗涤'
})

const dryingButtonText = computed(() => {
    return props.item.status === 'drying' ? '在晒' : '晾晒'
})

const favoriteButtonText = computed(() => {
    return props.item.isFavorite ? '已收藏' : '收藏'
})

// 保存编辑
const handleSave = () => {
    emit('update', { ...editData.value })
    isEditMode.value = false
}

// 取消编辑
const handleCancel = () => {
    editData.value = { ...props.item }
    isEditMode.value = false
}

// 删除卡片
const handleDelete = () => {
    emit('delete')
}

// 处理图片上传
const handleImageUpload = (event) => {
    const file = event.target.files[0]
    if (file) {
        // 这里应该调用上传API，现在只是预览
        const reader = new FileReader()
        reader.onload = (e) => {
            editData.value.image = e.target.result
        }
        reader.readAsDataURL(file)
    }
}

// 处理状态更新
const handleStatusUpdate = (status) => {
    if (props.item.status === status) {
        emit('status-update', 'stored')
    } else {
        emit('status-update', status)
    }
}

// 处理收藏更新
const handleFavoriteUpdate = () => {
    emit('favorite-update', !props.item.isFavorite)
}
</script>

<template>
    <el-card class="clothing-card">
        <!-- 查看模式 -->
        <template v-if="!isEditMode">
            <div class="image-container">
                <img :src="item.image" :alt="item.name">
            </div>
            <div class="info-container">
                <h3>{{ item.name }}</h3>
                <div class="tags">
                    <el-tag size="small">{{ item.category }}</el-tag>
                    <el-tag size="small" type="success">{{ item.thickness }}</el-tag>
                    <el-tag size="small" type="warning">{{ item.layer }}</el-tag>
                    <el-tag v-if="item.status !== 'stored'" size="small" type="info">
                        {{
                        {
                        'wearing': '正在穿着',
                        'washing': '正在洗涤',
                        'drying': '正在晾晒'
                        }[item.status]
                        }}
                    </el-tag>
                </div>
                <div class="rating">
                    <span>好看等级：</span>
                    <el-rate v-model="item.rating" disabled show-score text-color="#ff9900" />
                </div>
                <div v-if="item.set" class="set-info">
                    套装：{{ item.set }}
                </div>
                <div v-if="item.special" class="special-attr">
                    特殊属性：{{ item.special }}
                </div>
                <div class="note">
                    {{ item.note }}
                </div>
                <div class="actions">
                    <el-button type="primary" :disabled="item.status === 'wearing'" link
                        @click="handleStatusUpdate('wearing')">
                        {{ wearingButtonText }}
                    </el-button>
                    <el-button type="warning" :disabled="item.status === 'washing'" link
                        @click="handleStatusUpdate('washing')">
                        {{ washingButtonText }}
                    </el-button>
                    <el-button type="info" :disabled="item.status === 'drying'" link
                        @click="handleStatusUpdate('drying')">
                        {{ dryingButtonText }}
                    </el-button>
                    <el-button :type="item.isFavorite ? 'default' : 'success'" link @click="handleFavoriteUpdate">
                        {{ favoriteButtonText }}
                    </el-button>
                    <el-button type="primary" link @click="isEditMode = true">
                        编辑
                    </el-button>
                    <el-button type="danger" link @click="handleDelete">
                        删除
                    </el-button>
                </div>
            </div>
        </template>

        <!-- 编辑模式 -->
        <template v-else>
            <el-form label-position="top">
                <div class="image-container">
                    <img v-if="editData.image" :src="editData.image" :alt="editData.name">
                    <el-upload class="upload-btn" accept="image/*" :auto-upload="false" @change="handleImageUpload">
                        <el-button type="primary">更换图片</el-button>
                    </el-upload>
                </div>

                <el-form-item label="名称">
                    <el-input v-model="editData.name" />
                </el-form-item>

                <el-form-item label="类别">
                    <el-select v-model="editData.category">
                        <el-option v-for="option in categoryOptions" :key="option" :label="option" :value="option" />
                    </el-select>
                </el-form-item>

                <el-form-item label="厚度">
                    <el-select v-model="editData.thickness">
                        <el-option v-for="option in thicknessOptions" :key="option" :label="option" :value="option" />
                    </el-select>
                </el-form-item>

                <el-form-item label="层数">
                    <el-select v-model="editData.layer">
                        <el-option v-for="option in layerOptions" :key="option" :label="option" :value="option" />
                    </el-select>
                </el-form-item>

                <el-form-item label="好看等级">
                    <el-rate v-model="editData.rating" show-score />
                </el-form-item>

                <el-form-item label="套装">
                    <el-input v-model="editData.set" placeholder="不是套装可留空" />
                </el-form-item>

                <el-form-item label="特殊属性">
                    <el-select v-model="editData.special" clearable>
                        <el-option v-for="option in specialOptions" :key="option" :label="option" :value="option" />
                    </el-select>
                </el-form-item>

                <el-form-item label="备注">
                    <el-input v-model="editData.note" type="textarea" rows="2" />
                </el-form-item>

                <div class="actions">
                    <el-button type="primary" @click="handleSave">保存</el-button>
                    <el-button @click="handleCancel">取消</el-button>
                </div>
            </el-form>
        </template>
    </el-card>
</template>

<style scoped>
.clothing-card {
    width: 340px;
    /* margin: 10px; */
}

.image-container {
    width: 100%;
    height: 300px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f5f7fa;
}

.image-container img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}

.info-container {
    padding: 10px 0;
}

.tags {
    margin: 10px 0;
}

.tags .el-tag {
    margin-right: 5px;
}

.rating {
    margin: 10px 0;
}

.set-info,
.special-attr {
    margin: 5px 0;
    color: #606266;
}

.note {
    margin: 10px 0;
    color: #909399;
}

.actions {
    margin-top: 15px;
    display: flex;
    justify-content: center;
    gap: 8px;
}

.upload-btn {
    margin: 10px 0;
}
</style>



