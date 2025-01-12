<template>
    <div class="post-form">
      <h3>Create New Post</h3>
  
      <!-- Form for post creation -->
      <form @submit.prevent="submitPost">
        <div class="form-group">
          <label for="title">Title:</label>
          <input
            type="text"
            id="title"
            v-model="post.title"
            placeholder="Enter post title"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="content">Content:</label>
          <textarea
            id="content"
            v-model="post.content"
            placeholder="Enter post content"
            required
          ></textarea>
        </div>
  
        <div class="form-group">
          <button type="submit" class="submit-btn">Submit Post</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        post: {
          title: '',
          content: '',
        },
      };
    },
    methods: {
      // Submit the post to the backend
      async submitPost() {
        try {
          // Send the POST request to the backend
          const response = await axios.post('http://localhost:8082/post', this.post);
          
          console.log('Post created successfully:', response.data);
          
          // Emit an event to notify the parent component to refresh the posts list
          this.$emit('post-added');
          
          // Reset the form fields after successful submission
          this.post.title = '';
          this.post.content = '';
        } catch (error) {
          console.error('Error creating post:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Post form container */
  .post-form {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: 0 auto;
  }
  
  /* Heading */
  h3 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  /* Form group for input fields */
  .form-group {
    margin-bottom: 15px;
  }
  
  /* Label styling */
  label {
    font-size: 14px;
    font-weight: 600;
  }
  
  /* Input and textarea styling */
  input,
  textarea {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }
  
  /* Specific styling for textarea */
  textarea {
    height: 150px;
  }
  
  /* Button styling */
  button {
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  /* Button hover effect */
  button:hover {
    background-color: #218838;
  }
  </style>
  