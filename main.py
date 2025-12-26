# main.py
from manager import FinanceManager
import sys

def main():
    manager = FinanceManager()
    
    while True:
        print("\n" + "*"*30)
        print("   PyCashFlow 个人记账系统")
        print("*"*30)
        print("1. 记收入")
        print("2. 记支出")
        print("3. 查看账本")
        print("4. 退出系统")
        
        choice = input("👉 请选择功能 (1-4): ")

        if choice in ['1', '2']:
            try:
                amount = float(input("请输入金额: "))
                category = input("请输入分类 (如: 餐饮, 工资): ")
                desc = input("请输入备注: ")
                manager.add_transaction(choice, amount, category, desc)
            except ValueError:
                print("⚠️ 输入错误，金额必须是数字！")
        
        elif choice == '3':
            manager.show_report()
            
        elif choice == '4':
            print("👋 感谢使用，再见！")
            sys.exit()
            
        else:
            print("⚠️ 无效的选择，请重试。")

if __name__ == "__main__":
    main()
