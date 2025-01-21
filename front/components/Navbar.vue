<template>
  <nav
    class="navbar navbar-expand-lg navbar-light bg-light"
    :style="{ backgroundColor: brandBackground }"
  >
    <div class="container-fluid">
      <!-- Logo or Brand (Optional, can be passed as a prop or hardcoded) -->
      <router-link to="/" class="navbar-brand" :style="{ color: brandColor }"
        >PaymentApp</router-link
      >

      <!-- Toggle button for mobile view -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navbar links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <!-- Loop through the links passed as a prop -->
          <li class="nav-item" v-for="(link, index) in links" :key="index">
            <NuxtLink
              :to="link.to"
              class="nav-link"
              exact-active-class="active"
              :style="{ color: brandColor }"
            >
              {{ link.label }}
            </NuxtLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { defineProps } from "vue";

// Props: Accept the links to be rendered in the navbar
const props = defineProps({
  links: {
    type: Array,
    required: true,
  },
});

// Accessing CSS custom properties directly
const brandBackground = "var(--zexel-pure-white)";
const brandColor = "var(--zexel-persian-blue)";
</script>

<style scoped>
/* Custom styles for the navbar if needed */
.navbar {
  margin-bottom: 1rem;
}

.navbar-nav .nav-link {
  font-size: 1.1rem;
}

.navbar-toggler-icon {
  background-color: var(--zexel-pure-white); /* Toggler icon color */
}
</style>
