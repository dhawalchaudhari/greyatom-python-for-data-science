# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file

bank = pd.read_csv(path)
bank.shape
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
#Code starts here

#Step 2

banks = bank.drop('Loan_ID', axis = 1)
banks.isnull().sum()
bank_mode = banks.mode()
banks.fillna(bank_mode, inplace = True)
banks.isnull().sum()

#Step 3

avg_loan_amount = banks.pivot_table(index = ['Gender','Married','Self_Employed'],values = ['LoanAmount'], aggfunc = 'mean')
print(round(avg_loan_amount['LoanAmount'][1],2))

#Step 4

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()

percentage_se = round((loan_approved_se/banks['Loan_Status'].count())*100,2)

percentage_nse = round((loan_approved_nse/(banks['Loan_Status'].count()))*100,2)

print(percentage_se)
print(percentage_nse)

#Step 5

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12) 
big_loan_term = loan_term[loan_term>=25].count()

#Step 6

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = round(loan_groupby.mean(),2)

print(mean_values)



