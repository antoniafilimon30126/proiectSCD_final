import requests

BASE_URL = "http://127.0.0.1:8083/api"

# Testarea endpoint-ului pentru adăugarea unei postări
def test_add_post():
    payload = {
        "title": "Test Title",
        "content": "Test Content",
        "email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print(response.status_code, response.json())

# Testarea endpoint-ului pentru obținerea tuturor postărilor
def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print(response.status_code, response.json())

# Testarea endpoint-ului pentru aprobarea unei postări
def test_approve_post(post_id):
    response = requests.post(f"{BASE_URL}/posts/{post_id}/approve")
    print(response.status_code, response.json())

# Testarea endpoint-ului pentru ștergerea unei postări
def test_remove_post(post_id):
    response = requests.post(f"{BASE_URL}/posts/{post_id}/remove")
    print(response.status_code, response.json())

# Testarea endpoint-ului pentru adăugarea unui comentariu la o postare aprobată
def test_add_comment(post_id):
    payload = {
        "content": "This is a test comment",
        "email": "commenter@example.com"
    }
    response = requests.post(f"{BASE_URL}/posts/{post_id}/comments", json=payload)
    print(response.status_code, response.json())

# Testarea endpoint-ului pentru obținerea comentariilor unei postări
def test_get_comments(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    print(response.status_code, response.json())

if __name__ == "__main__":
    test_add_post()  # Adaugă o postare nouă
    test_get_posts()  # Obține toate postările
    test_approve_post(1)  # Aprobă postarea cu ID-ul 1
    test_add_comment(1)  # Adaugă un comentariu la postarea aprobată
    test_get_comments(1)  # Obține comentariile postării
    test_remove_post(1)  # Șterge postarea cu ID-ul 1
