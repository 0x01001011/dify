<template>
  <div class="external-api-plugin-config">
    <form @submit.prevent="submitConfiguration">
      <div class="form-group">
        <label for="apiUrl">API URL</label>
        <input type="text" id="apiUrl" v-model="apiUrl" required>
      </div>
      <div class="form-group">
        <label for="parameters">Parameters (JSON format)</label>
        <textarea id="parameters" v-model="parameters"></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ExternalAPIPluginConfig',
  data() {
    return {
      apiUrl: '',
      parameters: '{}',
    };
  },
  methods: {
    async submitConfiguration() {
      try {
        const payload = {
          api_url: this.apiUrl,
          parameters: JSON.parse(this.parameters),
        };
        await axios.post('/ui/configure_external_api', payload);
        alert('Configuration saved successfully.');
      } catch (error) {
        console.error('Error saving configuration:', error);
        alert('Failed to save configuration.');
      }
    },
  },
};
</script>

<style scoped>
.external-api-plugin-config {
  max-width: 600px;
  margin: auto;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: .5rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: .5rem;
  font-size: 1rem;
}

button {
  padding: .5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}
</style>
