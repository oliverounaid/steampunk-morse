<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
function changeContent() {
  document.getElementById("playButton")
}
</script>

<template>
  <!-- <section id="tutorial">
    <h1>Tutorial</h1>
    <span>
    Õpi morse koodi nagu töeline meremees. Mänguekraanile kuvatakse ülesanne, millele pead vastama kasutades morse koodi.
    Morse koodi sisestamiseks kasuta 'Space' klahvi või hiirt. (Täpsustus)
    </span>
    <button id="playButton" type="button">Mängi!</button>
  </section> -->
  <section id="gameMain" class="flex flex-col">
    <div>
      <h2 id="question">A</h2>
    </div>
    <input class="inputBox" type="text" value="">
    <div>
       <button class="flex" onclick="morseClick()">Space</button>
    </div>
    <div>
      
    </div>
   
  </section>
  <section id="gameOver">

  </section>
</template>

<style scoped>

</style>
