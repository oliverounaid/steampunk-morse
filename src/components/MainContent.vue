<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)

const mouseDownVal = ref(0);
const mouseUpVal = ref(0);
const myLetter = ref("");


function mouseDown() {
  mouseDownVal.value = Date.now();
}

function mouseUp() {
  mouseUpVal.value = Date.now();
  checkLength();
}
function checkLength() {
  const pressTime = mouseUpVal.value - mouseDownVal.value;

  if (pressTime < 140 ) {
    myLetter.value += ".";
    console.log(".")
  } else {
    myLetter.value += "-";
    console.log("-")
  }
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
    <p id="inputBox">{{myLetter}}</p>
    <div>
      <button id="clicker" @mousedown="mouseDown" @mouseup="mouseUp" class="flex">Space</button>
    </div>
  </section>
  <!-- <section id="gameOver">

  </section> -->
</template>

<style scoped>

</style>
