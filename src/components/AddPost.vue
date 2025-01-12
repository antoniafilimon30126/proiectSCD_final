<template>
    <div>
      <!-- Modal Dialog -->
      <div v-if="showDialog" class="modal">
        <div class="modal-content">
          <span class="close-btn" @click="closeDialog">&times;</span>
          <h3>Welcome, {{ currentUser }}!</h3>
          <label for="title">Post title</label>
          <input type="text" id="title" v-model="post.title" placeholder="Enter post title" />
          
          <label for="content">Post content</label>
          <textarea id="content" v-model="post.content" placeholder="Enter post content"></textarea>
          
          <div class="buttons">
            <button class="create-btn" @click="createPost">Create</button>
            <button class="cancel-btn" @click="closeDialog">Cancel</button>
          </div>
        </div>
      </div>
  
      <!-- Button to open the modal -->
      <button @click="openDialog">Create new post</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'PostForm',
    props: {
      currentUser: String
    },
    data() {
      return {
        showDialog: false,
        post: {
          title: '',
          content: '',
        }
      }
    },
    methods: {
      openDialog() {
        this.showDialog = true;
      },
      closeDialog() {
        this.showDialog = false;
        this.post = { title: "", content: "" }; // Clear form fields
      },
      async createPost() {
        try {
          const response = await axios.post('http://localhost:8082/post', this.post);
          console.log("Post created successfully:", response.data);
          this.showDialog = false;
        } catch (error) {
          console.error("Error creating post:", error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Modal styling */
  .modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
  }
  
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    cursor: pointer;
  }
  
  label {
    font-size: 14px;
    margin-top: 10px;
    display: block;
  }
  
  input, textarea {
    width: 100%;
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  textarea {
    min-height: 100px;
  }
  
  .buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }
  
  button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .create-btn {
    background-color: green;
    color: white;
  }
  
  .cancel-btn {
    background-color: red;
    color: white;
  }
  
  button:hover {
    opacity: 0.8;
  }
  </style>
  