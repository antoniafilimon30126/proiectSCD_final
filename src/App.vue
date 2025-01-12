<template>
  <div id="app">
    <!-- PostForm component to create new posts -->
    
    
    <!-- PostList component to display the posts -->
    <PostList :posts="posts" />
    <PostForm @post-added="fetchPosts" />
  </div>
</template>

<script>
import PostForm from './components/PostForm.vue';
import PostList from './components/PostList.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    PostForm,
    PostList
  },
  data() {
    return {
      posts: []  // This will store the list of posts
    };
  },
  methods: {
    async fetchPosts() {
      try {
        // Fetch the posts from the backend
        const response = await axios.get('http://localhost:8082/post');
        this.posts = response.data;  // Update posts data
      } catch (error) {
        console.error("Error fetching posts:", error);
      }
    }
  },
  created() {
    // Fetch posts when the app is created
    this.fetchPosts();
  }
};
</script>

<style>
#app {
  font-family: 'Arial', sans-serif;
  background-color: #f4f6f9;
  padding: 20px;
}
</style>
