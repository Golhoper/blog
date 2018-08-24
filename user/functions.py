import Libraries

def reg_fields(name, pasw, email,f_name, l_name):
    if len(name) > 0 and len(pasw) and len(email) and len(f_name) and len(l_name) > 0:
        return True
    else:
        return False