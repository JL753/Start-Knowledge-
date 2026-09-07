# -*- coding: utf-8 -*-
"""模型连通性自检：python check_models.py（先设置好环境变量）"""
import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from config.models import MODELS, JUDGE_MODEL
from openai import OpenAI

def ping(name, cfg):
    key = os.environ.get(cfg["api_key_env"])
    if not key:
        return f"x {name}: 缺少环境变量 {cfg['api_key_env']}"
    try:
        c = OpenAI(api_key=key, base_url=cfg["base_url"], timeout=30)
        r = c.chat.completions.create(model=cfg["model"], max_tokens=8,
                                      messages=[{"role": "user", "content": "只回复两个字母: OK"}])
        return f"v {name} ({cfg['model']}) -> {r.choices[0].message.content.strip()[:20]}"
    except Exception as e:
        return f"x {name} ({cfg['model']}): {str(e)[:160]}"

for n, c in MODELS.items():
    print(ping(n, c))
print(ping("裁判模型", JUDGE_MODEL))
