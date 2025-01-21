<template>
  <Navbar :links="navbarLinks" />
  <div class="container mt-5 pt-4">
    <h1 class="display-4 mt-2 mb-4">{{ $t("countries") }}</h1>

    <div class="app-description-container text-center mb-5">
      <h2 class="mb-3">{{ $t("app_description") }}</h2>
      <div class="divider"></div>
    </div>

    <div v-if="countries.length">
      <h2>{{ $t("list_countries") }}:</h2>
      <div class="table-responsive">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>{{ $t("name") }}</th>
              <th>{{ $t("iso3") }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="country in countries" :key="country.iso3">
              <td>{{ country.name }}</td>
              <td>{{ country.iso3 }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="alert alert-info">
      {{ $t("no_countries") }}
    </div>

    <Alert ref="alert" />
  </div>
</template>

<script setup>
const countries = ref([]);
const alert = ref(null);
const { t } = useI18n();
const navbarLinks = [
  { to: "/countries/search", label: t("search_countries") },
  { to: "/countries/detail", label: t("detail_countries") },
  { to: "/countries/edit", label: t("edit_countries") },
];

onMounted(async () => {
  try {
    countries.value = await getCountries();
  } catch (e) {
    alert.value.error(e.message);
  }
});
</script>
