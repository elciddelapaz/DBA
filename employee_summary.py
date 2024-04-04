new_male = int(input('Enter the number of newly hired males: '))
new_female = int(input('Enter the number of newly hired females: '))
perm_male = int(input('Enter the number of permanent position males: '))
perm_female = int(input('Enter the number of permanent position females: '))
resigned_male = int(input('Enter the number of resigned males: '))
resigned_female = int(input('Enter the number of resigned females: '))

total_new = new_male + new_female
total_perm = perm_male + perm_female
total_resigned = resigned_male + resigned_female

def get_percentage(number, total):
    percentage = number / total
    return format(percentage, '.2%')

print("===")
print("Thank you for the Information")
print("===")
print("Here is the Summary !!!")
print("Number of Hired employee = ", total_new)
print("Male = " , get_percentage(new_male, total_new))
print("Female = ", get_percentage(new_female, total_new))
print("Number of Pemanent employee = ", total_perm)
print("Male = ", get_percentage(perm_male, total_perm))
print("Female = ", get_percentage(perm_female, total_perm))
print("Number of Resigned employee = ", total_resigned)
print("Male = ", get_percentage(resigned_male, total_resigned))
print("Female = ", get_percentage(resigned_female, total_resigned) )
