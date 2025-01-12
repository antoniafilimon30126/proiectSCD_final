// Displays a single post and its comments.

<template>
  <div v-if="post">
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>

    <h2>Comments</h2>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <p>{{ comment.content }}</p>
        <button @click="editComment(comment)">Edit</button>
        <button @click="deleteComment(comment.id)">Delete</button>
      </li>
    </ul>

    <comment-form @submit-comment="addOrUpdateComment" />
  </div>
</template>

<script>
import CommentForm from './CommentForm.vue';

export default {
  components: { CommentForm },
  props: ['post', 'comments'],
  methods: {
    editComment(comment) {
      this.$refs.commentForm.comment = comment;
    },
    deleteComment(commentId) {
      this.$emit('delete-comment', commentId);
    },
    addOrUpdateComment(comment) {
      this.$emit('add-update-comment', comment);
    }
  }
};
</script>
