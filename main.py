# Programmers:  Laure Patera
# Course:  CS151, Dr. Yalew
# Due Date: 9/18/24
# Programming Assignment:  PA00
# Problem Statement:  What amount will you be reimbursed by the IRS for driving a certain mileage for your job?
# Data In: reimbursement rate by their state, and the mileage they have driven or expect to drive
# Data Out: The amount that they will be reimbursed
# Credits: Code inspired by a problem given by my mom, with the calculation from
# https://mileiq.com/mileage-guide/understanding-mileage-reimbursements-and-rates#toc-how-to-calculate-mileage-reimbursements

# User is asked to input the reimbursement rate of their state and their mileage, before these pieces of info are
# converted to floats
reimbursement_rate = float(input('What is the mileage reimbursement rate of your state?'))
mileage = float(input('What is the mileage that you have driven, or expect to drive for your job?'))

# calculates reimbursement amount from the given inputs
reimbursement_amount = reimbursement_rate * mileage

# outputs the reimbursement amount to the user
print('You will be reimbursed', reimbursement_amount, 'dollars')

