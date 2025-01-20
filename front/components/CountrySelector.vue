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
        v-for="(country, key) in $props.countries"
        :key="key"
        :value="country[$props.valueKey]"
      >
        {{ country[$props.textKey] }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  props: {
    modelValue: String,
    id: String,
    label: String,
    countries: Array,
    loading: Boolean,
    valueKey: {
      type: String,
      default: "iso2", // Default to 'iso' if not provided
    },
    textKey: {
      type: String,
      default: "name", // Default to 'country' if not provided
    },
  },
  methods: {
    onInput(event) {
      // Emit the update:modelValue event to update the parent component
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>
