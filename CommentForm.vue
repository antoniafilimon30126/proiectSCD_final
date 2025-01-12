// Allows adding or editing comments.

<template>
  <div>
    <form @submit.prevent="submitComment">
      <textarea v-model="comment.content" placeholder="Add your comment here" required></textarea>
      <button type="submit">{{ editing ? 'Update' : 'Add' }} Comment</button>
    </form>
  </div>
</template>

<script>
export default {
  props: ['editing', 'existingComment'],
  data() {
    return {
      comment: this.existingComment || { content: '' }
    };
  },
  methods: {
    submitComment() {
      this.$emit('submit-comment', this.comment);
      this.comment = { content: '' }; // Reset form after submission
    }
  }
};
</script>