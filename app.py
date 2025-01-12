
from flask import Flask, request, jsonify
from service import SocialMediaService

# Inițializarea aplicației Flask
app = Flask(__name__)

# Instanțierea logicii aplicației
service = SocialMediaService()

from flask import render_template

@app.route('/')
def home():
    return render_template('admin_dashboard.html')



# Endpoint pentru căutarea postărilor/comentariilor după un cuvânt-cheie
@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '')
    results = service.get_posts_by_keyword(keyword)
    return jsonify(results), 200

# Endpoint pentru aprobarea unei postări
@app.route('/posts/<int:post_id>/approve', methods=['POST'])
def approve_post(post_id):
    post = service.approve_post(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

# Endpoint pentru ștergerea unei postări
@app.route('/posts/<int:post_id>/remove', methods=['DELETE'])
def remove_post(post_id):
    success = service.remove_post(post_id)
    if success:
        return jsonify({"message": "Post removed"}), 200
    return jsonify({"error": "Post not found"}), 404

# Endpoint pentru trimiterea unui email
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipients = data.get("recipients", [])
    subject = data.get("subject")
    content = data.get("content")
    try:
        # Folosire simplă a SMTP pentru trimiterea emailurilor
        service.send_email(recipients, subject, content)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
