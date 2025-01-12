<template>
  <div>
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <CommentSection
      :comments="post.comments"
      @add-comment="addComment"
      @update-comment="updateComment"
      @delete-comment="deleteComment"
    />
  </div>
</template>

<script>
import CommentSection from "./CommentSection.vue";

export default {
  components: { CommentSection },
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  methods: {
    addComment(newComment) {
      this.post.comments.push(newComment);
    },
    updateComment({ index, text }) {
      this.$set(this.post.comments, index, text);
    },
    deleteComment(index) {
      this.post.comments.splice(index, 1);
    },
  },
};
</script>
