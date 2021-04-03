#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:51:51 2021

@author: tinatina
"""
import pandas as pd
budget_data = pd.read_csv('./Resources/budget_data.csv')
n = budget_data['Date'].nunique()
# print(n)
m = budget_data['Profit/Losses'].sum()
# print(m)
budget_data['profit_shift'] = budget_data['Profit/Losses'].shift(1)
budget_data['profit_change'] = budget_data['Profit/Losses'] - budget_data['profit_shift']
profit_change_mean = budget_data['profit_change'].mean()
# print(profit_change_mean)
s = budget_data['Profit/Losses'].argmax()
s1 = budget_data.loc[s,"Date"]
# print(s1)
s2 = budget_data.loc[s,"profit_change"]
# print(s2)
d = budget_data['Profit/Losses'].argmin()
d1 = budget_data.loc[d,"Date"]
d2 = budget_data.loc[d,"profit_change"]
# print(d1)
# print(d2)

result = f'''Financial Analysis
----------------------------
Total Months: {n}
Total: ${m}
Average  Change: ${profit_change_mean:.2f}
Greatest Increase in Profits: {s1} (${s2:.0f})
Greatest Decrease in Profits: {d1} (${d2:.0f})'''

print(result)
with open('./analysis/' + "analysis.txt" , "w") as text_file:
    text_file.write(result)