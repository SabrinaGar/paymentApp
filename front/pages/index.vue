<template>
  <Navbar :links="navbarLinks" />
  <div class="container mt-5 pt-4">
    <h1 class="display-4 mt-2 mb-4">{{ $t("hi") }}</h1>

    <div class="app-description-container text-center mb-5">
      <h2 class="mb-3">{{ $t("app_description") }}</h2>
      <div class="divider"></div>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from "vue-i18n";
import Navbar from "../components/Navbar.vue";
const { t } = useI18n();
const navbarLinks = [
  { to: "/payments", label: t("payments") },
  { to: "/countries", label: t("countries") },
];
</script>
