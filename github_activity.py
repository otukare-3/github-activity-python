"""
以下のプロジェクトを作成。
https://roadmap.sh/projects/github-user-activity
"""
import argparse
import json
import pprint
import textwrap

import requests


def get_github_activity(user_name: str) -> list:
    """
    githubから指定したuser_nameのeventsを取得する
    :param user_name: ユーザー名
    :return: 取得結果
    """
    response = requests.get(f"https://api.github.com/users/{user_name}/events",
                            timeout=5)

    if response.status_code != 200:
        print(response.text)
        print(f"Error getting github activity for {user_name}")
        return []

    json_str = json.dumps(response.json())
    return json.loads(json_str)


def main():
    """
    コマンドライン用の準備
    """
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""
            GitHub User Activity Roadmap
            https://roadmap.sh/projects/github-user-activity"""),
        epilog="Thank You!!")
    parser.add_argument("user_name", type=str, help="GitHub User Name")
    args = parser.parse_args()

    result = get_github_activity(args.user_name)

    if result is not None:
        pprint.pprint(result)


if __name__ == "__main__":
    main()
