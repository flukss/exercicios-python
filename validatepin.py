import re
def validate_pin(pin):
    if "\n" in pin:
        return False
    if re.findall('^[0-9]{4}$|^[0-9]{6}$', pin):
        return True
    else:
        return False

validate_pin('1234')