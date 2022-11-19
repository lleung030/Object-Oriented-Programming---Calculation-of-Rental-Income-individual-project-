class Rental_Income():
    def __init__(self, name):
        self.name = name
        self.balance_sheet = {}
        self.investment_sheet = {}

        
        
        
    def add_income(self):
        response = input(f'What is your annual income?: ')
        print("\n")
        {'Income':response}
        self.balance_sheet.update({'Income':response})
        print(f'{self.balance_sheet}')
        
        
    def add_expense(self):
        response = input(f'What is your total expense?: ')
        print("\n")
        {'Total Expense':response}
        self.balance_sheet.update({'Total Expense':response})
        print(f'{self.balance_sheet}')
    
    def cash_flow_calc(self, income):
        print(self.balance_sheet)
        print("\n")
        if income in self.balance_sheet:
            x = self.balance_sheet['Income']
            y = self.balance_sheet['Total Expense']
            cash_flow = int(x) - int(y)
            print(f"Your income of ${x} minus an expense of ${y} comes out to be... ${cash_flow}!")
            print("\n")
            self.balance_sheet.update({'Cash Flow':cash_flow})
            print(f'{self.balance_sheet}')
        else:
            print('Error: Please call Customer Service at 1-800-this_is_not_working...')
        
    def investment(self):
        answer_1 = input(f'What is your Down Payment?: ')
        {'Down Payment':answer_1}
        self.investment_sheet.update({'Down Payment':answer_1})
        print(self.investment_sheet)
        print("\n")
        
        answer_2 = input(f'What is your Closing Costs?: ')
        {'Closing Costs':answer_2}
        self.investment_sheet.update({'Closing Costs':answer_2})
        print(self.investment_sheet)
        print("\n")
        
        answer_3 = input(f'What is your Rehab budget?: ')
        {'Rehab budget':answer_3}
        self.investment_sheet.update({'Rehab budget':answer_3})
        print(self.investment_sheet)
        print("\n")
        
        answer_4 = input(f'What is your Misc. Costs?: ')
        {'Misc. Costs':answer_4}
        self.investment_sheet.update({'Misc. Costs':answer_4})
        print(self.investment_sheet)
        
        print("\n")
        
        total_investment = int(answer_1) + int(answer_2) + int(answer_3) + int(answer_4)
        self.balance_sheet.update({'Investments':total_investment})
        
        print("CALCULATING . . .")
        print('\n')
        
        print("Your Investment Breakdown:")
        print(self.investment_sheet)
        print('\n')
        
        print("Your Balance Sheet:")
        print(self.balance_sheet)
        
    def roi(self):
        pass
    
    def main(self):
        pass