class ProductOfNumbers:

    def __init__(self):
        self._numbers = []
        

    def add(self, num: int) -> None:
        self._numbers += [num]
        

    def getProduct(self, k: int) -> int:
        last_k_nums = self._numbers[-k:]
        if 0 in last_k_nums:
            return 0
        elif last_k_nums.count(1) == k:
            return 1
        prod = 1
        for num in last_k_nums:
            prod *= num
        return prod
