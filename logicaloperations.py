#if an applicant has high income AND good credit, then they are eligible for loans
has_good_credit = True
has_high_income = False
if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")
#if an applicant has high income OR good credit, then they are eligible for loans
has_good_credit = True
has_high_income = False
if has_good_credit or has_high_income:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")
#if an applicant has high income and doesn't have criminal reocords, then they are eligible for loans
has_criminal_record = False
has_high_income = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

