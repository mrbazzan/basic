
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

