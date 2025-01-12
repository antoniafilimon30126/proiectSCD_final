import requests

BASE_URL = "http://localhost:8080/api"  # URL-ul backend-ului


# Funcție pentru obținerea tuturor postărilor
def fetch_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        if response.status_code == 200:
            posts = response.json()
            print("Postări disponibile:")
            for post in posts:
                print(f"ID: {post['id']}, Titlu: {post['title']}, Aprobat: {post['approved']}")
        else:
            print(f"Eroare la obținerea postărilor: {response.status_code}")
    except Exception as e:
        print(f"Eroare la conectare: {e}")


# Funcție pentru aprobare postare
def approve_post(post_id):
    try:
        response = requests.post(f"{BASE_URL}/posts/{post_id}/approve")
        if response.status_code == 200:
            print(f"Postarea cu ID {post_id} a fost aprobată!")
        else:
            print(f"Eroare la aprobarea postării: {response.status_code}")
    except Exception as e:
        print(f"Eroare la conectare: {e}")


# Funcție pentru ștergerea unei postări
def remove_post(post_id):
    try:
        response = requests.post(f"{BASE_URL}/posts/{post_id}/remove")
        if response.status_code == 200:
            print(f"Postarea cu ID {post_id} a fost ștearsă!")
        else:
            print(f"Eroare la ștergerea postării: {response.status_code}")
    except Exception as e:
        print(f"Eroare la conectare: {e}")


# Funcție pentru trimiterea unui email
def send_email(recipients, subject, content):
    try:
        payload = {
            "recipients": recipients,
            "subject": subject,
            "content": content
        }
        response = requests.post(f"{BASE_URL}/send-email", json=payload)
        if response.status_code == 200:
            print("Emailul a fost trimis cu succes!")
        else:
            print(f"Eroare la trimiterea emailului: {response.status_code}")
    except Exception as e:
        print(f"Eroare la conectare: {e}")


# Meniul aplicației
def main():
    while True:
        print("\n1. Afișează toate postările")
        print("2. Aproba o postare")
        print("3. Șterge o postare")
        print("4. Trimite email")
        print("5. Ieșire")
        
        choice = input("Alege o opțiune: ")
        
        if choice == "1":
            fetch_posts()
        elif choice == "2":
            post_id = input("Introdu ID-ul postării: ")
            approve_post(post_id)
        elif choice == "3":
            post_id = input("Introdu ID-ul postării: ")
            remove_post(post_id)
        elif choice == "4":
            recipients = input("Introdu destinatarii (separați prin virgulă): ")
            subject = input("Introdu subiectul emailului: ")
            content = input("Introdu conținutul emailului: ")
            send_email(recipients, subject, content)
        elif choice == "5":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Încearcă din nou.")


if __name__ == "__main__":
    main()
