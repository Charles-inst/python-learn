"""第 4 课：input() 交互输入"""


def main() -> None:
    # input() 会暂停程序，等待你在终端里输入，按回车确认
    name = input("你叫什么名字？ ")
    print(f"你好, {name}!")

    age_text = input("你今年几岁？ ")
    age = int(age_text)  # 把文字转成数字
    print(f"5 年后你 {age + 5} 岁")

    # TODO: 再问一下你喜欢什么语言，打印一句鼓励的话
    language = input("你想学哪门编程语言？ ")
    print(f"加油，{name}！学好 {language} 一定很有用。")


if __name__ == "__main__":
    main()
