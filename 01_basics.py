"""第 1 课：Python 基础"""


def main() -> None:
    # 1. 变量
    name = "Python"
    age = 3
    print(f"我在学 {name}，学了 {age} 年")

    # 2. 列表
    fruits = ["apple", "banana", "orange"]
    print("第一个水果:", fruits[0])

    # 3. 循环
    print("水果列表:")
    for fruit in fruits:
        print(f"  - {fruit}")

    # 4. 条件判断
    score = 85
    if score >= 90:
        print("优秀")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")

    # 5. 函数
    def greet(person: str) -> str:
        return f"Hello, {person}!"

    print(greet("World"))

    # --- 下面留给你练习 ---
    # TODO: 把 your_name 改成你的名字
    your_name = "chang"
    print(f"你好, {your_name}")

    # TODO: 计算 1 到 5 的和，结果应该是 15
    total = 0
    for n in range(1, 6):
        total += n
    print("1 到 5 的和:", total)


if __name__ == "__main__":
    main()
