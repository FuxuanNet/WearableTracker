import axios from 'axios'

// 创建 axios 实例
const service = axios.create({
    baseURL: '/api', // API 基础路径
    timeout: 15000,  // 请求超时时间
})

// 请求拦截器
service.interceptors.request.use(
    config => {
        // 可以在这里添加 token 等通用 header
        return config
    },
    error => {
        console.error('Request error:', error)
        return Promise.reject(error)
    }
)

// 响应拦截器
service.interceptors.response.use(
    response => {
        return response.data
    },
    error => {
        console.error('Response error:', error)
        // 统一错误处理
        if (error.response) {
            switch (error.response.status) {
                case 400:
                    console.error('请求参数错误')
                    break
                case 404:
                    console.error('请求资源不存在')
                    break
                case 500:
                    console.error('服务器内部错误')
                    break
                default:
                    console.error('未知错误')
            }
        }
        return Promise.reject(error)
    }
)

export default service
