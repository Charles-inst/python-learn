"""第 2 课：用 requests 发网络请求"""

import requests


def main() -> None:
    url = "https://jsonplaceholder.typicode.com/posts/1"

    print(f"正在请求: {url}")
    response = requests.get(url, timeout=10)

    print("状态码:", response.status_code)
    print("响应类型:", response.headers.get("content-type"))

    data = response.json()
    print("文章 ID:", data["id"])
    print("标题:", data["title"])
    print("正文前 50 字:", data["body"][:50], "...")

    # TODO: 把 user_id 改成 2，再运行看标题会不会变
    user_id = 3
    user_url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response2 = requests.get(user_url, timeout=10)
    posts = response2.json()
    print(f"\n用户 {user_id} 的文章数量:", len(posts))
    print("第一篇标题:", posts[0]["title"])


if __name__ == "__main__":
    main()
