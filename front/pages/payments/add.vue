<template>
  <Navbar :links="navbarLinks" />
  <div class="container mt-5 pt-4">
    <h1 class="display-4 mt-2 mb-4">{{ $t("payments") }}</h1>

    <div class="app-description-container text-center mb-5">
      <h2 class="mb-3">{{ $t("app_description") }}</h2>
      <div class="divider"></div>
    </div>

    <div>
      <h2>{{ $t("add_payments") }}</h2>
      <Alert ref="alert" />
      <form @submit.prevent="submitPayment">
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="sourceAmount" class="form-label">{{
              $t("source_amount")
            }}</label>
            <input
              type="number"
              class="form-control"
              id="sourceAmount"
              v-model="payment.source_amount"
              required
            />
          </div>
          <div class="col-md-4">
            <label for="sourceCurrency" class="form-label">{{
              $t("source_currency")
            }}</label>
            <CountrySelector
              v-model="payment.source_currency"
              id="targetCountry"
              label="target_country"
              :countries="countries"
              :loading="loading"
              value-key="currency"
              text-key="currency"
            />
          </div>
          <div class="col-md-4">
            <label for="sourceCountry" class="form-label">{{
              $t("source_country")
            }}</label>
            <CountrySelector
              v-model="payment.source_country"
              id="targetCountry"
              label="target_country"
              :countries="countries"
              :loading="loading"
              value-key="iso2"
              text-key="name"
            />
          </div>
        </div>
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="targetAmount" class="form-label">{{
              $t("target_amount")
            }}</label>
            <input
              type="number"
              class="form-control"
              id="targetAmount"
              v-model="payment.target_amount"
              required
            />
          </div>
          <div class="col-md-4">
            <label for="targetCurrency" class="form-label">{{
              $t("target_currency")
            }}</label>
            <CountrySelector
              v-model="payment.target_currency"
              id="targetCountry"
              label="target_currency"
              :countries="countries"
              :loading="loading"
              value-key="currency"
              text-key="currency"
            />
          </div>
          <div class="col-md-4">
            <label for="targetCountry" class="form-label">{{
              $t("target_country")
            }}</label>

            <CountrySelector
              v-model="payment.target_country"
              id="targetCountry"
              label="target_country"
              :countries="countries"
              :loading="loading"
              value-key="iso2"
              text-key="name"
            />
          </div>
        </div>
        <div class="row mb-3">
          <div class="col-md-4">
            <label for="concept" class="form-label">{{ $t("concept") }}</label>
            <input
              type="text"
              class="form-control"
              id="concept"
              v-model="payment.concept"
              required
            />
          </div>
          <div class="col-md-4">
            <label for="senderFullName" class="form-label">{{
              $t("sender_full_name")
            }}</label>
            <input
              type="text"
              class="form-control"
              id="senderFullName"
              v-model="payment.sender_full_name"
              required
            />
          </div>
          <div class="col-md-4">
            <label for="receiverFullName" class="form-label">{{
              $t("receiver_full_name")
            }}</label>
            <input
              type="text"
              class="form-control"
              id="receiverFullName"
              v-model="payment.receiver_full_name"
              required
            />
          </div>
        </div>
        <button type="submit" class="btn btn-primary">
          {{ $t("submit") }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import CountrySelector from "~/components/CountrySelector.vue";
import { getCountriesCurrencyAndIso } from "../../utils/client_api_countries";
import Navbar from "~/components/Navbar.vue";
import Alert from "~/components/Alert.vue";

const { t } = useI18n();
const navbarLinks = [{ to: "/payments", label: t("list_payments") }];
const payment = ref({
  source_amount: null,
  source_currency: "",
  source_country: "",
  target_amount: null,
  target_currency: "",
  target_country: "",
  concept: "",
  sender_full_name: "",
  receiver_full_name: "",
});

const errorMessages = ref([]);
const successMessage = ref("");
const alert = ref(null);
const countries = ref([]); // Lista de países
const loading = ref(false); // Estado de carg

onMounted(async () => {
  try {
    loading.value = true;
    countries.value = await getCountriesCurrencyAndIso();
  } catch (e) {
    errorMessages.value.push(e.message);
    alert.value.error(e.message);
  } finally {
    loading.value = false;
  }
});
const submitPayment = async () => {
  try {
    errorMessages.value = [];
    successMessage.value = "";
    const response = await fetch("http://localhost:8000/api/payments/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payment.value),
    });

    if (!response.ok) {
      const errorData = await response.json();
      if (errorData.non_field_errors) {
        errorMessages.value = errorData.non_field_errors;
        alert.value.error(errorData.non_field_errors.join(", "));
      } else {
        errorMessages.value.push(
          t("error_adding_payment", {
            error: errorData.detail || "Unknown error",
          })
        );
        alert.value.error(errorMessages.value.join(", "));
      }
      return;
    }

    const result = await response.json();
    console.log("Payment added:", result);

    successMessage.value(t("payment_added_successfully"));
    alert.value.message(successMessage.value);

    payment.value = {
      source_amount: null,
      source_currency: "",
      source_country: "",
      target_amount: null,
      target_currency: "",
      target_country: "",
      concept: "",
      sender_full_name: "",
      receiver_full_name: "",
    };
  } catch (error) {
    errorMessages.value.push(
      t("error_adding_payment", { error: error.message })
    );
    alert.value.error(errorMessages.value.join(", "));
  }
};
</script>
