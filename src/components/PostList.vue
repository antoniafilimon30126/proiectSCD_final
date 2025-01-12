<template>
    <div class="post-list">
      <h2 class="heading">My Posts</h2>
      <button class="load-btn" @click="fetchPosts">Load Posts</button>
  
      <div v-for="post in posts" :key="post.id" class="post-item">
        <h3 class="post-title">{{ post.title }}</h3>
        <p class="post-content">{{ post.content }}</p>
        <p class="post-subtitle">Posted on: {{ post.createdOn }}</p>
  
        <div class="comments">
          <h4>Comments</h4>
          <div v-for="comment in post.comments" :key="comment.id" class="comment">
            <p>{{ comment.content }} - by {{ comment.user.name }}</p>
          </div>
          <CommentForm :postId="post.id" />
        </div>
  
        <div class="actions">
          <button @click="deletePost(post.id)" class="delete-btn">Delete Post</button>
          <button @click="openEditPost(post)" class="edit-btn">Edit Post</button>
        </div>
      </div>
  
      <div v-if="editPostModal" class="modal">
        <div class="modal-content">
          <h3>Edit Post</h3>
          <input v-model="editPost.title" placeholder="Title" />
          <textarea v-model="editPost.content" placeholder="Content"></textarea>
          <button @click="savePost">Save Changes</button>
          <button @click="closeModal">Cancel</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import CommentForm from './CommentForm.vue';
  
  export default {
    components: { CommentForm },
    data() {
      return {
        posts: [],
        newComment: '',
        editPostModal: false,
        editPost: {},
      };
    },
    methods: {
      async fetchPosts() {
        try {
          const response = await axios.get('http://localhost:8082/post');
          this.posts = response.data;
        } catch (error) {
          console.error("Error fetching posts:", error);
        }
      },
      async addComment(postId) {
        try {
          const commentData = {
            post: { id: postId },
            content: this.newComment,
            user: { id: 1 }, // Example user ID, change as needed
          };
          await axios.post('http://localhost:8082/comment', commentData);
          this.newComment = '';
          this.fetchPosts();
        } catch (error) {
          console.error("Error adding comment:", error);
        }
      },
      async deletePost(postId) {
        try {
          await axios.delete(`http://localhost:8082/post/${postId}`);
          this.fetchPosts();
        } catch (error) {
          console.error("Error deleting post:", error);
        }
      },
      openEditPost(post) {
        this.editPost = { ...post };
        this.editPostModal = true;
      },
      closeModal() {
        this.editPostModal = false;
      },
      async savePost() {
        try {
          await axios.put(`http://localhost:8082/post/${this.editPost.id}`, this.editPost);
          this.editPostModal = false;
          this.fetchPosts();
        } catch (error) {
          console.error("Error saving post:", error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .heading {
    font-size: 24px;
    font-weight: bold;
  }
  
  .load-btn {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin: 20px 0;
  }
  
  .post-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .post-item {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .post-title {
    font-size: 20px;
    font-weight: bold;
  }
  
  .comments {
    margin-top: 20px;
  }
  
  .comment {
    background-color: #ececec;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 5px;
  }
  
  textarea {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    border-radius: 4px;
    border: 1px solid #ddd;
  }
  
  button {
    padding: 10px 15px;
    margin-top: 10px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .delete-btn {
    background-color: red;
    color: white;
  }
  
  .edit-btn {
    background-color: orange;
    color: white;
  }
  
  .edit-btn:hover, .delete-btn:hover {
    opacity: 0.8;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
  }
  </style>
  