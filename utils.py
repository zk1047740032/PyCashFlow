# utils.py
import json
import os

DATA_FILE = "data/ledger.json"

def load_data():
    """读取数据文件"""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(data_list):
    """写入数据文件"""
    # 确保 data 目录存在
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            # indent=4 格式化输出，方便阅读
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        print("✅ 数据保存成功！")
    except Exception as e:
        print("❌ 数据保存失败：{e}")