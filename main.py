import os
import base64
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    docversion = os.environ["INPUT_DOCVERSION"]
    apikey = os.environ["INPUT_APIKEY"]
    slug = os.environ["INPUT_SLUG"]
    category_id = os.environ["INPUT_CATEGORYID"]
    markdown_path = os.environ["INPUT_PATH"]

    apikey_changed = apikey+":"
    b64_apikey = base64.b64encode(apikey_changed.encode("ascii"))

    with open(markdown_path, "r") as md:
        markdown = md.read()

    url = f"https://dash.readme.com/api/v1/docs/{slug}"

    headers = {
        "Accept": "application/json",
        "x-readme-version": docversion,
        "Content-Type": "application/json",
        "Authorization": f"Basic {b64_apikey}"
    }

    payload = {
        "hidden": True,
        "catgory": category_id,
        "order": 999,
        "body": markdown

    }

    response = requests.put(url, json=payload, headers=headers)

    print(response.text)


if __name__ == "__main__":
    main()
