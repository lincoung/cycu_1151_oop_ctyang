def gcd(a: int, b: int) -> int:
    """使用輾轉相除法（遞迴）計算兩個整數的最大公因數"""
    if b == 0:
        return a
    return gcd(b, a % b)

# 測試範例
x, y = 55, 21
print(f"GCD of {x} and {y} is {gcd(x, y)}")

