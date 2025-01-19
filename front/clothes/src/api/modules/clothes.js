import request from '../config/axios'

export const clothesApi = {
    /**
     * 获取所有衣物列表
     * @returns {Promise<ClothesItem[]>}
     */
    getAll() {
        return request({
            url: '/clothes',
            method: 'get'
        })
    },

    /**
     * 添加新衣物
     * @param {ClothesItem} clothes - 衣物数据
     * @returns {Promise<ClothesItem>}
     */
    add(clothes) {
        return request({
            url: '/clothes',
            method: 'post',
            data: clothes
        })
    },

    /**
     * 更新衣物信息
     * @param {number} id - 衣物ID
     * @param {Partial<ClothesItem>} clothes - 要更新的衣物数据
     * @returns {Promise<ClothesItem>}
     */
    update(id, clothes) {
        return request({
            url: `/clothes/${id}`,
            method: 'put',
            data: clothes
        })
    },

    /**
     * 删除衣物
     * @param {number} id - 衣物ID
     * @returns {Promise<void>}
     */
    delete(id) {
        return request({
            url: `/clothes/${id}`,
            method: 'delete'
        })
    },

    /**
     * 更新衣物状态
     * @param {number} id - 衣物ID
     * @param {string} status - 新状态
     * @returns {Promise<ClothesItem>}
     */
    updateStatus(id, status) {
        return request({
            url: `/clothes/${id}/status`,
            method: 'put',
            data: { status }
        })
    },

    /**
     * 更新收藏状态
     * @param {number} id - 衣物ID
     * @param {boolean} isFavorite - 收藏状态
     * @returns {Promise<ClothesItem>}
     */
    updateFavorite(id, isFavorite) {
        return request({
            url: `/clothes/${id}/favorite`,
            method: 'put',
            data: { isFavorite }
        })
    }
}