
def maxProfit(prices):
    first = prices[0]
    result = 0
    for p in prices:
        if p < first:
            first = p
        result = max(result, p - first)
    return result 

print(maxProfit([10,1,5,6,7,1]))