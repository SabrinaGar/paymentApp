<template>
  <div v-if="showModal" :class="['alert', alertClass]" role="alert">
    {{ alertMessage }}
    <button type="button" class="close" @click="hide" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const showModal = ref(false);
const alertMessage = ref("");
const typeAlert = ref("");

const show = () => {
  showModal.value = true;
};

const hide = () => {
  showModal.value = false;
};

const alertClass = computed(() => {
  return typeAlert.value === "error" ? "alert-danger" : "alert-success";
});

const message = (message, showModal = true) => {
  typeAlert.value = "message";
  __write(message, showModal);
};

const error = (message, showModal = true) => {
  typeAlert.value = "error";
  __write(message, showModal);
};

const __write = (message, showModal = true) => {
  alertMessage.value = message;
  if (showModal) {
    show();
  }
};

defineExpose({
  show,
  hide,
  message,
  error,
});
</script>
