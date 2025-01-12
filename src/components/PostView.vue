<template>
    <div>
      <h2 class="heading">My posts</h2>
      <button class="load-btn" @click="fetchPosts">Load Posts</button>
  
      <div class="post-list">
        <div class="post-item" v-for="post in posts" :key="post.id">
          <h3 class="post-title">{{ post.title }}</h3>
          <p class="post-subtitle">posted on {{ post.createdOn }}</p>
          <p class="post-content">{{ post.content }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Posts',
    data() {
      return {
        posts: []
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
  
  .load-btn:hover {
    background-color: #0056b3;
  }
  
  .post-list {
    margin-top: 20px;
  }
  
  .post-item {
    padding: 15px;
    background-color: #f8f9fa;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  
  .post-title {
    font-size: 18px;
    font-weight: bold;
  }
  
  .post-subtitle {
    font-size: 14px;
    color: #555;
  }
  
  .post-content {
    font-size: 16px;
    color: #333;
  }
  </style>
  