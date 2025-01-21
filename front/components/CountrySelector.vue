<template>
  <div class="col-md-12">
    <select
      @input="onInput"
      :value="modelValue"
      :id="id"
      class="form-control"
      required
    >
      <option value="" disabled selected>{{ $t("select_placeholder") }}</option>
      <option
        v-for="(country, key) in countries"
        :key="key"
        :value="country[valueKey]"
      >
        {{ country[textKey] }}
      </option>
    </select>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
const props = defineProps({
  modelValue: {
    type: String,
    required: true,
  },
  id: String,
  label: String,
  countries: {
    type: Array,
    required: true,
  },
  loading: Boolean,
  valueKey: {
    type: String,
    default: "iso2",
  },
  textKey: {
    type: String,
    default: "name",
  },
});

const emit = defineEmits(["update:modelValue"]);

const onInput = (event) => {
  emit("update:modelValue", event.target.value);
};
</script>
