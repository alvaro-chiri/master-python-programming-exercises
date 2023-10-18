# def valid_password(text):
#     pass_list = text.split(',')
#     approved_pass = []
#     lower_check = None
#     upper_check = None
#     one_alpha = None
#     one_digit = None
#     one_char = None
#     for password in pass_list:
#         if len(password) > 5 and len(password) < 13:
#             for char in password:
#                 if char.islower() == True:
#                     lower_check = True
#                 if char.isupper() == True:
#                     upper_check = True
#                 if char.isalpha() == True:
#                     one_alpha = True
#                 if char.isdigit() == True:
#                     one_digit = True
#                 if '$' in char or '#' in char or '@' in char:
#                     one_char = True
#             if lower_check == True and upper_check == True and one_alpha == True and one_digit == True and one_char == True:
#                 approved_pass.append(password)
#         lower_check = None
#         upper_check = None
#         one_alpha = None
#         one_digit = None
#         one_char = None
#     return ','.join(approved_pass)
# print(valid_password('ABd1234@1,a F1#,2w3E*,2We3345'))


import re
def valid_password(text):
    value = []
    pass_list=[x for x in text.split(',')]
    for password in pass_list:
        if len(password)<6 or len(password)>12:
            continue
        else:
            pass
        if not re.search("[a-z]",password):
            continue
        elif not re.search("[0-9]",password):
            continue
        elif not re.search("[A-Z]",password):
            continue
        elif not re.search("[$#@]",password):
            continue
        elif re.search("\s",password):
            continue
        value.append(password)
    return (",".join(value))

print(valid_password('ABd1234@1,a F1#,2w3E*,2We3345'))