"""第 3 课：小项目 —— 批量抓取文章标题"""

import requests


def fetch_titles(user_id: int) -> list[str]:
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    posts = response.json()
    return [post["title"] for post in posts]


def save_titles(user_id: int, titles: list[str]) -> str:
    filename = f"user_{user_id}_titles.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for index, title in enumerate(titles, start=1):
            file.write(f"{index}. {title}\n")
    return filename


def main() -> None:
    # TODO: 改成你想查询的用户 ID（1~10 都可以试）
    user_id = 3

    print(f"正在获取用户 {user_id} 的文章...")
    titles = fetch_titles(user_id)

    print(f"共 {len(titles)} 篇:\n")
    for index, title in enumerate(titles, start=1):
        print(f"{index}. {title}")

    output_file = save_titles(user_id, titles)
    print(f"\n已保存到: {output_file}")


if __name__ == "__main__":
    main()
