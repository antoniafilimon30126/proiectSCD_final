// A form component to add or edit a post.

<template>
  <div>
    <h1>Add or Edit Post</h1>
    <form @submit.prevent="submitPost">
      <input v-model="post.title" placeholder="Enter title" required />
      <textarea v-model="post.content" placeholder="Enter content" required></textarea>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  props: ['editingPost'],
  data() {
    return {
      post: this.editingPost || { title: '', content: '' }
    };
  },
  methods: {
    submitPost() {
      this.$emit('submit-post', this.post);
      this.post = { title: '', content: '' }; // Reset form after submission
    }
  }
};
</script>
