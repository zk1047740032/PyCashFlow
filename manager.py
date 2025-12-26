# manager.py
from models import Income, Expense
import utils

class FinanceManager:
    """账本管理器，负责协调数据模型和文件存储"""

    def __init__(self):
        # 初始化时加载数据
        raw_data = utils.load_data()
        self.transactions = []
        self._load_objects(raw_data)

    def _load_objects(self, raw_data):
        """将字典数据还原为对象"""
        for item in raw_data:
            if item['type'] == 'Income':
                obj = Income(item['amount'], item['category'], item['description'])
            elif item['type'] == 'Expense':
                obj = Expense(item['amount'], item['category'], item['description'])
            else:
                # 兼容旧数据
                if item['type'] == 'income':
                    obj = Income(item['amount'], item['category'], item['description'])
                else:
                    obj = Expense(item['amount'], item['category'], item['description'])

            # 还原时间（覆盖默认生成的当前时间）
            obj.date = item['date']
            self.transactions.append(obj)
        
    def add_transaction(self, t_type, amount, category, desc):
        """添加交易"""
        if t_type == '1':
            new_t = Income(amount, category, desc)
        else:
            new_t = Expense(amount, category, desc)
        
        # 添加到交易列表
        self.transactions.append(new_t)
        # 保存到文件
        self.save()
        print("✅ 交易记录已保存！")

    def get_balance(self):
        """计算总余额"""
        total_income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        total_expense = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        return total_income - total_expense
    
    def show_report(self):
        """打印所有记录"""
        print(f"\n{'=*10'} 账本详情 {'='*10}")
        if not self.transactions:
            print("暂无记录")
            return

        for t in self.transactions:
            symbol = '+' if isinstance(t, Income) else '-'
            print(f"{symbol} {t.date} | {t.category} | {t.description} | ¥{t.amount:.2f}")
        
        print(f"\n💰 当前余额: ¥{self.get_balance():.2f}")
        print("="*30)

    def save(self):
        """将对象列表转换为字典列表并保存"""
        data_to_save = [t.to_dict() for t in self.transactions]
        utils.save_data(data_to_save)