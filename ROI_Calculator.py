from babel.numbers import format_currency

def print_greeting():
    print('****** ROI Calculator for Rental Properties ******\n')

def str_to_dollars(input_str):
    return format_currency(input_str, "USD", locale='en_US')

def get_income():
    print('\n\n1. INCOME')
    rental_income = float(input('Monthly rental income: '))
    additional_income = float(input('Additional monthly income ($0): ') or '0')
    total_monthly_income = float(rental_income) + float(additional_income)
    print(f'\nTotal monthly income: {str_to_dollars(total_monthly_income)}\n\n')
    input('Press [Enter] to continue')
    return total_monthly_income

def get_expenses():
    print('\n\n2. EXPENSES')
    taxes = float(input('Monthly taxes ($250.00): ') or '250')
    insurance = float(input('Monthly insurance ($0): ') or '0')
    utilities = float(input('Monthly utilities ($0): ') or '0')
    hoa = float(input('Monthly HOA fees ($0): ') or '0')
    lawn = float(input('Monthly lawn maintenance ($0): ') or '0')
    vacancy = float(input('Monthly vacancy ($100): ') or '100')
    repairs = float(input('Monthly repairs ($100): ') or '100')
    capex = float(input('Monthly capital expenditures ($100): ') or '100')
    property_mgmt = float(input('Monthly property management ($0): ') or '0')
    mortgage = float(input('Monthly mortgage payment: '))

    expenses = (taxes
        + insurance
        + utilities
        + hoa
        + lawn
        + vacancy
        + repairs
        + capex
        + property_mgmt
        + mortgage)

    print(f'\nTotal monthly expenses: {str_to_dollars(expenses)}\n\n')
    input('Press [Enter] to continue')
    return expenses
        
def calc_cash_flow(income: float, expenses: float):
    print('\n\n3. CASH FLOW')
    print(f'Income: {str_to_dollars(income)}\nExpenses: {str_to_dollars(expenses)}')
    cash_flow = income - expenses
    print('Income - Expenses = Cash Flow')
    print(f'Total monthly cash flow: {str_to_dollars(cash_flow)}\n\n')
    input('Press [Enter] to continue')
    return cash_flow

def calc_roi(cash_flow: float):
    print('\n\n4. CASH ON CASH RETURN')
    down_payment = float(input('Down payment ($6,000): ') or '6000')
    closing_costs = float(input('Total closing costs ($10,000): ') or '10000')
    rehab = float(input('Rehab/repairs budget ($2,000): ') or '2000')
    misc = float(input('Misc costs ($5000): ') or '5000')

    total_investment = (down_payment
        + closing_costs
        + rehab
        + misc)

    annual_cash_flow = cash_flow * 12

    roi = annual_cash_flow / total_investment
    print(f'\nTotal investment: {str_to_dollars(total_investment)}')    
    print(f'Annual cash flow: {str_to_dollars(annual_cash_flow)}')
    print(f'Annual cash on cash retrun: {round(roi*100, 4)}\n\n')
    input('Press [Enter] to continue')
    return roi

def print_report(income: float,
                 expenses: float,
                 cash_flow: float,
                 roi: float):
    roi_formatted = round(roi*100, 4)
    print('\n\n****** ROI Report *******')
    print(f'Total monthly income: {str_to_dollars(income)}')
    print(f'Total monthly expenses: {str_to_dollars(expenses)}')
    print(f'Monthly cash flow: {str_to_dollars(cash_flow)}')
    print(f'Annual ROI: {roi_formatted}%')
    if roi_formatted < 0:
        print('This investment is not an investment, it is a liability. Lol.')
    elif roi_formatted > 0 and roi_formatted < 2.5:
        print('This is a bad investment. Doesn\'t keep pace with inflation.')
    elif roi_formatted >= 2.5 and roi_formatted < 5:
        print('This is a mediocre investment. Look elsewhere.')
    elif roi_formatted >= 5 and roi_formatted < 7.5:
        print('This is a good investment. Should consider.')
    elif roi_formatted >= 7.5 and roi_formatted < 10:
        print('This is a great investment! Send it.')
    else:
        print('This is a fantastic investment.')
    input('Press [Enter] to exit')

def main():
    print_greeting()
    
    monthly_income = get_income()
    monthly_expenses = get_expenses()
    monthly_cash_flow = calc_cash_flow(
        income=monthly_income,
        expenses=monthly_expenses
    )
    annual_roi = calc_roi(cash_flow = monthly_cash_flow)
    print_report(income=monthly_income,
                 expenses=monthly_expenses,
                 cash_flow=monthly_cash_flow,
                 roi=annual_roi)


if __name__ == '__main__':
    main()
    
    
