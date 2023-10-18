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
        else:
            pass
        value.append(password)
    return (",".join(value))