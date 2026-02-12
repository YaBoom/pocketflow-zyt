"""
PocketFlow 公共配置文件
用于管理模型 API 配置，方便切换不同模型
"""

# 智谱 AI 配置
ZHIPU_API_KEY = "xxxxxxxxxxxxx"
ZHIPU_MODEL = "glm-5"

# Kimi AI 配置
KIMI_API_KEY = "xxxxxxxxxxxxxxxxxx"
KIMI_MODEL = "moonshot-v1-8k"
KIMI_BASE_URL = "https://api.moonshot.cn/v1"

# OpenAI 配置（备用）
# OPENAI_API_KEY = "your-openai-api-key"
# OPENAI_MODEL = "gpt-4o-mini"

# 当前使用的模型配置
CURRENT_API_KEY = KIMI_API_KEY
CURRENT_MODEL = KIMI_MODEL
CURRENT_BASE_URL = KIMI_BASE_URL


def call_llm(prompt: str, model: str = None, api_key: str = None, base_url: str = None) -> str:
    """
    统一的 LLM 调用接口
    
    Args:
        prompt: 提示词
        model: 模型名称，默认使用配置中的模型
        api_key: API 密钥，默认使用配置中的密钥
        base_url: API 基础 URL，默认使用配置中的 URL
    
    Returns:
        模型响应文本
    """
    if model is None:
        model = CURRENT_MODEL
    if api_key is None:
        api_key = CURRENT_API_KEY
    if base_url is None:
        base_url = CURRENT_BASE_URL
    
    try:
        if base_url:
            from openai import OpenAI
            client = OpenAI(api_key=api_key, base_url=base_url)
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        else:
            from zhipuai import ZhipuAI
            client = ZhipuAI(api_key=api_key)
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM API: {str(e)}"


def update_config(api_key: str = None, model: str = None, base_url: str = None):
    """
    更新配置
    
    Args:
        api_key: 新的 API 密钥
        model: 新的模型名称
        base_url: 新的 API 基础 URL
    """
    global CURRENT_API_KEY, CURRENT_MODEL, CURRENT_BASE_URL
    
    if api_key:
        CURRENT_API_KEY = api_key
    if model:
        CURRENT_MODEL = model
    if base_url:
        CURRENT_BASE_URL = base_url


def use_kimi():
    """切换到 Kimi 模型"""
    update_config(
        api_key=KIMI_API_KEY,
        model=KIMI_MODEL,
        base_url=KIMI_BASE_URL
    )


def use_zhipu():
    """切换到智谱模型"""
    update_config(
        api_key=ZHIPU_API_KEY,
        model=ZHIPU_MODEL,
        base_url=None
    )
