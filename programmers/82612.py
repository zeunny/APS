def solution(price, money, count):
    total_price = (count * (count+1) // 2) * price

    return 0 if money-total_price > 0 else -(money-total_price)