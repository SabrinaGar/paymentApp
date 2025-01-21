<template>
  <nav
    class="navbar navbar-expand-lg navbar-light bg-light"
    :style="{ backgroundColor: brandBackground }"
  >
    <div class="container-fluid">
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
          <li class="nav-item">
            <div class="d-flex align-items-center">
              <select
                v-model="selectedLanguage"
                @change="changeLanguage"
                class="form-select"
              >
                <option v-for="lang in languages" :key="lang" :value="lang">
                  {{ lang.toUpperCase() }}
                </option>
              </select>
            </div>
          </li>
        </ul>
      </div>
      <!-- Language selector dropdown -->
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { defineProps } from "vue";
import { useI18n } from "vue-i18n";

// Props: Accept the links to be rendered in the navbar
const props = defineProps({
  links: {
    type: Array,
    required: true,
  },
});
const { locale } = useI18n();

const languages = ["en", "es"];
const selectedLanguage = ref("es");

const changeLanguage = () => {
  if (selectedLanguage.value) {
    locale.value = selectedLanguage.value; // Update locale
    localStorage.setItem("language", selectedLanguage.value); // Store language preference);
  }
};

const brandBackground = "var(--zexel-pure-white)";
const brandColor = "var(--zexel-persian-blue)";
onMounted(() => {
  const storedLang = localStorage.getItem("language");
  if (storedLang) {
    selectedLanguage.value = storedLang;
    locale.value = storedLang;
  }
});
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
  background-color: var(--zexel-pure-white);
}
</style>
