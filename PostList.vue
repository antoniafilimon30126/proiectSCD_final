<template>
  <div>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <div>
          <h3>{{ post.title }}</h3>
          <p>{{ post.content }}</p>
        </div>

        <div>
          <button @click="$emit('view-post', post.id)">View Details</button>
          <button @click="$emit('remove-post', post.id)">Delete</button>
        </div>

        <!-- Comentarii -->
        <div v-if="post.comments && post.comments.length > 0" class="comments-section">
          <h4>Comments:</h4>
          <ul>
            <li v-for="(comment, index) in post.comments" :key="index">
              {{ comment }}
            </li>
          </ul>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
};
</script>

<style>
.comments-section {
  margin-top: 10px;
  padding: 10px;
  border-top: 1px solid #ccc;
}

.comments-section h4 {
  margin-bottom: 5px;
  color: #1e90ff;
}

.comments-section ul {
  list-style-type: none;
  padding: 0;
}

.comments-section li {
  background: #f9f9f9;
  padding: 5px;
  border-radius: 4px;
  margin-bottom: 5px;
}
</style>
