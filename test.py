# -*- coding: utf-8 -*-

import json
from time import time

import urllib3

http = urllib3.PoolManager()


def main():
    query = {
        "query": """mutation {
            create_ticket (name: \"T-0001\", description: \"...\", storyPoints: 5) {
                expectedDateline
            }
        }"""
    }

    start = time()

    for _ in range(2000):
        http.request(
            "POST",
            "http://localhost:3001/graphql",
            headers={"Content-Type": "application/json"},
            body=json.dumps(query)
        )

        # print(r.data.decode("utf-8"))

    print(time() - start)


if __name__ == "__main__":
    main()
