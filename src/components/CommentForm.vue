<template>
    <div>
      <textarea v-model="newComment" placeholder="Write a comment..."></textarea>
      <button @click="submitComment">Submit Comment</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: ['postId'],
    data() {
      return {
        newComment: '',
      };
    },
    methods: {
      async submitComment() {
        try {
          const commentData = {
            post: { id: this.postId },
            content: this.newComment,
            user: { id: 1 }, // Example user ID, change as needed
          };
          await axios.post('http://localhost:8082/comment', commentData);
          this.newComment = ''; // Clear input
          this.$emit('comment-added');
        } catch (error) {
          console.error("Error submitting comment:", error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  textarea {
    width: 100%;
    padding: 10px;
    border-radius: 4px;
    border: 1px solid #ddd;
    margin-top: 10px;
  }
  
  button {
    padding: 10px 20px;
    margin-top: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>
  