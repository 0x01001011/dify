<template>
  <div id="app">
    <!-- Other UI elements -->
    <section id="plugin-configurations">
      <external-api-plugin-config></external-api-plugin-config>
    </section>
    <!-- Other UI elements -->
  </div>
</template>

<script>
import ExternalAPIPluginConfig from './components/ExternalAPIPluginConfig.vue';

export default {
  name: 'App',
  components: {
    ExternalAPIPluginConfig
  }
};
</script>

<style>
/* Existing styles */
</style>
