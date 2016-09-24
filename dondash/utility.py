class Validator(object):
    def __init__(self):
        return

    @classmethod
    def is_an_id(cls, input):
        result = True
        if type(input) is int:
            return False
        elif len(input) != 32:
            return False
        else:
            return True
