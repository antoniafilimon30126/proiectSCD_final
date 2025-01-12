<template>
  <div class="post-management">
    <header class="app-header">
      <h1>Post Management App</h1>
    </header>

    <!-- Formular pentru adăugare/editare postări -->
    <div class="add-post-form">
      <h2>{{ isEditingPost ? "Edit Post" : "Add Post" }}</h2>
      <form @submit.prevent="submitPost" class="form-card">
        <div class="form-group">
          <label for="email">Your Email</label>
          <input
            id="email"
            type="email"
            v-model="currentPost.email"
            placeholder="Enter your email"
            required
          />
        </div>
        <div class="form-group">
          <label for="title">Enter Title</label>
          <input
            id="title"
            type="text"
            v-model="currentPost.title"
            placeholder="Enter title"
            required
          />
        </div>
        <div class="form-group">
          <label for="content">Enter Content</label>
          <textarea
            id="content"
            v-model="currentPost.content"
            placeholder="Enter content"
            required
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">
          {{ isEditingPost ? "Update Post" : "Add Post" }}
        </button>
      </form>
    </div>

    <!-- Afișarea postărilor -->
    <div class="posts">
      <h2>Posts</h2>
      <div class="post-list">
        <div
          v-for="(post, index) in posts"
          :key="index"
          class="post-card"
        >
          <h3>{{ post.title }}</h3>
          <p class="post-author">By: <strong>{{ post.email }}</strong></p>
          <p class="post-content">{{ post.content }}</p>
          <div class="post-actions">
            <button @click="editPost(index)" class="btn btn-secondary">Edit</button>
            <button @click="deletePost(index)" class="btn btn-danger">Delete</button>
            <button @click="viewDetails(index)" class="btn btn-info">View Details</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Detalii postare și comentarii -->
    <div v-if="selectedPostIndex !== null" class="post-details">
      <div class="details-card">
        <h2>{{ posts[selectedPostIndex].title }}</h2>
        <p>
          <strong>Author:</strong> {{ posts[selectedPostIndex].email }}
        </p>
        <p>{{ posts[selectedPostIndex].content }}</p>
        <h3>Comments</h3>
        <ul class="comment-list">
          <li
            v-for="(comment, index) in posts[selectedPostIndex].comments"
            :key="index"
            class="comment-card"
          >
            <p class="comment-text">{{ comment.text }}</p>
            <p class="comment-author">
              By: <strong>{{ comment.email }}</strong>
            </p>
            <div class="comment-actions">
              <button @click="editComment(index)" class="btn btn-secondary">Edit</button>
              <button @click="deleteComment(index)" class="btn btn-danger">Delete</button>
            </div>
          </li>
        </ul>
        <div class="add-comment-form">
          <h4>{{ isEditingComment ? "Edit Comment" : "Add Comment" }}</h4>
          <form @submit.prevent="submitComment" class="form-card">
            <div class="form-group">
              <label for="commentEmail">Your Email</label>
              <input
                id="commentEmail"
                type="email"
                v-model="currentComment.email"
                placeholder="Enter your email"
                required
              />
            </div>
            <div class="form-group">
              <label for="comment">Comment</label>
              <textarea
                id="comment"
                v-model="currentComment.text"
                placeholder="Enter your comment here"
                required
              ></textarea>
            </div>
            <button type="submit" class="btn btn-primary">
              {{ isEditingComment ? "Update Comment" : "Add Comment" }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: [],
      currentPost: { title: "", content: "", email: "", comments: [] },
      isEditingPost: false,
      selectedPostIndex: null,
      currentComment: { text: "", email: "" },
      isEditingComment: false,
      editingCommentIndex: null,
    };
  },
  methods: {
    savePostsToLocalStorage() {
      localStorage.setItem("posts", JSON.stringify(this.posts));
    },
    loadPostsFromLocalStorage() {
      const savedPosts = localStorage.getItem("posts");
      if (savedPosts) {
        this.posts = JSON.parse(savedPosts);
      }
    },
    submitPost() {
  if (this.isEditingPost) {
    // Actualizează postarea selectată folosind atribuirea directă
    this.posts[this.selectedPostIndex] = {
      ...this.currentPost,
      comments: this.posts[this.selectedPostIndex].comments, // Păstrează comentariile existente
    };
    this.isEditingPost = false;
  } else {
    // Adaugă o postare nouă
    this.posts.push({ ...this.currentPost, comments: [] });
  }

  // Salvează postările în localStorage
  this.savePostsToLocalStorage();

  // Resetează formularul postării
  this.resetPostForm();
}
,
    editPost(index) {
      this.currentPost = { ...this.posts[index] };
      this.isEditingPost = true;
      this.selectedPostIndex = index;
    },
    deletePost(index) {
      this.posts.splice(index, 1);
      this.savePostsToLocalStorage();
    },
    viewDetails(index) {
      this.selectedPostIndex = index;
      this.currentComment = { text: "", email: "" };
      this.isEditingComment = false;
    },
    resetPostForm() {
      this.currentPost = { title: "", content: "", email: "", comments: [] };
      this.isEditingPost = false;
      this.selectedPostIndex = null;
    },
    submitComment() {
      if (this.selectedPostIndex === null) return;

      if (this.isEditingComment) {
        this.posts[this.selectedPostIndex].comments[this.editingCommentIndex] = {
          ...this.currentComment,
        };
        this.isEditingComment = false;
        this.editingCommentIndex = null;
      } else {
        this.posts[this.selectedPostIndex].comments.push({
          ...this.currentComment,
        });
      }

      // Resetează formularul de comentariu
      this.currentComment = { text: "", email: "" };
      this.savePostsToLocalStorage();
    },
    editComment(index) {
      this.currentComment = {
        ...this.posts[this.selectedPostIndex].comments[index],
      };
      this.isEditingComment = true;
      this.editingCommentIndex = index;
    },
    deleteComment(index) {
      this.posts[this.selectedPostIndex].comments.splice(index, 1);
      this.savePostsToLocalStorage();
    },
  },
  mounted() {
    this.loadPostsFromLocalStorage();
  },
};
</script>

<style>
/* Stil general */
body {
  font-family: 'Arial', sans-serif;
  background-color: #f4f6f9;
  color: #333;
  margin: 0;
  padding: 0;
}

.post-management {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.app-header {
  background-color: #007bff;
  color: white;
  text-align: center;
  padding: 20px 0;
  margin-bottom: 20px;
}

.add-post-form,
.post-details {
  margin-bottom: 20px;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.post-list,
.comment-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

.post-card,
.comment-card {
  background: white;
  padding: 15px;
  margin: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.btn {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff;
}

.btn-secondary {
  background-color: #6c757d;
}

.btn-danger {
  background-color: #dc3545;
}

.btn-info {
  background-color: #17a2b8;
}

.form-group {
  margin-bottom: 15px;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
