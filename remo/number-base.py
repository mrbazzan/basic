
class NumberBaseConverter:

    @staticmethod
    def return_result(result):
        if not result:
            return '0'
        return ''.join(result)

    @classmethod
    def base_three(cls, number):
        result = []
        while number > 0:
            remainder = number % 3
            result.insert(0, str(remainder))
            number = number // 3

        return cls.return_result(result)

    @classmethod
    def base_five(cls, number):
        result = []
        while number > 0:
            remainder = number % 5
            result.insert(0, str(remainder))
            number = number // 5

        return cls.return_result(result)

    @classmethod
    def base_seven(cls, number):
        result = []
        while number > 0:
            remainder = number % 7
            result.insert(0, str(remainder))
            number = number // 7
        return cls.return_result(result)

    @classmethod
    def base_four(cls, number):
        result = []
        while number > 0:
            remainder = number % 4
            result.insert(0, str(remainder))
            number = number // 4
        return cls.return_result(result)

    @classmethod
    def base_six(cls, number):
        result = []
        while number > 0:
            remainder = number % 6
            result.insert(0, str(remainder))
            number = number // 6
        return cls.return_result(result)



