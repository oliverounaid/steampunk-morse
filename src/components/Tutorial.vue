<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
  <div class="tutorial">
    <h1>Tutorial</h1>
    <span>
    Õpi morse koodi nagu töeline meremees. Mänguekraanile kuvatakse ülesanne, millele pead vastama kasutades morse koodi.
    Morse koodi sisestamiseks kasuta 'Space' klahvi või hiirt. (Täpsustus)
    </span>
    <button type="button">Mängi!</button>
  </div>
</template>

<style scoped>

</style>
