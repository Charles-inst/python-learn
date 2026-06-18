"""第 5 课：交互式小项目 —— 运行时输入用户 ID 抓取标题"""

import requests


def fetch_titles(user_id: int) -> list[str]:
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return [post["title"] for post in response.json()]


def save_titles(user_id: int, titles: list[str]) -> str:
    filename = f"user_{user_id}_titles.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for index, title in enumerate(titles, start=1):
            file.write(f"{index}. {title}\n")
    return filename


def ask_user_id() -> int:
    while True:
        text = input("请输入用户 ID（1~10），直接回车默认 1: ").strip()

        if text == "":
            return 1

        if text.isdigit():
            user_id = int(text)
            if 1 <= user_id <= 10:
                return user_id

        print("输入无效，请输入 1 到 10 之间的数字。")


def main() -> None:
    print("=== 文章标题抓取器 ===\n")
    user_id = ask_user_id()

    print(f"\n正在获取用户 {user_id} 的文章...")
    titles = fetch_titles(user_id)

    print(f"共 {len(titles)} 篇，前 3 篇标题：\n")
    for index, title in enumerate(titles[:3], start=1):
        print(f"{index}. {title}")

    save = input("\n要保存到文件吗？(y/n): ").strip().lower()
    if save == "y":
        filename = save_titles(user_id, titles)
        print(f"已保存到: {filename}")
    else:
        print("未保存文件。")


if __name__ == "__main__":
    main()
