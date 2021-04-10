#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:25:15 2021

@author: tinatina
"""
import pandas as pd
employee_data = pd.read_csv('/Users/tinatina/Documents/Boot Camp/Homework/Homework3/Bonus/PyBoss/employee_data.csv')
employee_data.head()
employee_data[['First Name','Last Name']] \
    = employee_data['Name'].loc[\
      employee_data['Name'].str.split().str.len() == 2]\
        .str.split(expand=True)
#data format
employee_data['DOB'].dtype
employee_data['DOB'] = pd.to_datetime(employee_data['DOB'])
employee_data['DOB_str'] = employee_data['DOB'].dt.strftime('%m/%d/%Y')
#SSN format
import re
employee_data.SSN = employee_data.SSN.apply(lambda x: re.sub(r'\d', '*', x, count=5))
#state
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

def map_state(full_name):
    return us_state_abbrev[full_name]
map_state('California')
employee_data['State_abbr']\
    = employee_data['State'].apply(map_state)

employee_data = employee_data.drop(columns=['Name','DOB','State',])
employee_data = employee_data[['Emp ID','First Name','Last Name','DOB_str','SSN','State_abbr']]
employee_data = employee_data.rename(columns = {'DOB_str':'DOB','State_abbr':'State'})
employee_data.to_csv('/Users/tinatina/Documents/Boot Camp/Homework/Homework3/Bonus/PyBoss/reformated_employee_data.csv')