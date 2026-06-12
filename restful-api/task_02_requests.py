#!/usr/bin/python3

import requests
import json
import csv

def fetch_and_print_posts():
    """fetches and prints all post from JSONPlaceholder"""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        print("Status Code:",response.status_code)
        data = response.json()
        if not isinstance(data, list):
              print("Unexpected JSON format: Expected a list of posts.")
              return
        for idx, post in enumerate(data, start=1):
                title = post.get("title")
                if title:
                    print(f"{title}")
                else:
                    print(f"{idx}. [No title found]")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Error parsing JSON response.")

def fetch_and_save_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        posts = response.json()
        # Structure data: only keep id, title, body
        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts saved successfully to posts.csv")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError:
        print("Error parsing JSON response.")
        
