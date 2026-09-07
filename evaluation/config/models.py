# -*- coding: utf-8 -*-
"""被测模型配置。全部走 OpenAI 兼容接口，改这里即可增删模型。
API Key 通过环境变量注入，严禁写进代码提交到 git。
若智谱报"模型不存在"：glm-4.7-flash → glm-4-flash-250414，glm-4.7 → glm-4-plus"""

MODELS = {
    "glm-4.7-flash": {
        "api_key_env": "ZHIPU_API_KEY",
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4.7-flash",
        "provider": "智谱",
        "price_per_1k": 0.0,
    },
    "qwen-plus": {
        "api_key_env": "DASHSCOPE_API_KEY",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-plus",
        "provider": "阿里云百炼",
        "price_per_1k": 0.0008,
    },
    "deepseek-chat": {
        "api_key_env": "DEEPSEEK_API_KEY",
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-chat",
        "provider": "DeepSeek",
        "price_per_1k": 0.002,
    },
}

# 裁判模型：选账号内可用的强模型（与被测模型同源会带偏好，报告中需披露）
JUDGE_MODEL = {
    "api_key_env": "ZHIPU_API_KEY",
    "base_url": "https://open.bigmodel.cn/api/paas/v4",
    "model": "glm-4.7",
    "temperature": 0.1,
}
