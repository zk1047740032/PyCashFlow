# models.py
from datetime import datetime

class Transaction:
    """ 交易基类 """
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """将对象转换为字典，方便后续JSON序列化"""
        return{
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
            "type": "General"
        }
    
    def __str__(self):
        """魔术方法，决定print(对象)时的显示内容"""
        return f"[{self.date}] {self.description} {self.amount}"

class Income(Transaction):
    """收入类，继承自 Transaction"""
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Income"
        return data
    
class Expense(Transaction):
    """支出类，继承自 Transaction"""
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Expense"
        return data
