<script setup>
import { ref } from 'vue'
import alphabet from '../assets/alphabet.json'

defineProps({
  msg: String
})

// Socket.io server configuration
const isOnline = true;

const serverURL = "https://kak-socketio-server.herokuapp.com";
// serverURL = "http://localhost:8000";

if ( isOnline ) {
  const socket = io(serverURL);
  
  socket.on("connect", () => {
    console.log("Client connected to: " + socket.id);
    // online = true;
  });
  
  socket.on("send-data", res => {
    console.log(res);
    if ("t" in res) { 
      signalCheck(res.t);
    }
  });
  
  socket.on("disconnect", () => {
    console.log("Client disconnected from" + socket.id); 
  });
}

const count = ref(0)

const letters = alphabet.chars;
const mouseDownVal = ref(0);
const mouseUpVal = ref(0);
const myLetter = ref("");
let timeoutID ;


function mouseDown() {
  mouseDownVal.value = Date.now();
}

function mouseUp() {
  mouseUpVal.value = Date.now();
  checkLength();
}
function checkLength() {
  const pressTime = mouseUpVal.value - mouseDownVal.value;

  signalCheck(pressTime);
}
function signalCheck(pressTime) {
  if (pressTime < 140 ) {
    myLetter.value += ".";
    // console.log(".")
  } else {
    myLetter.value += "-";
    // console.log("-")
  }
  console.log(myLetter.value,letters[0].A);
  if (letters[0].A.startsWith(myLetter.value)) {
    console.log("ok")
  } else {
    console.log("not ok")
  }
  clearTimeout(timeoutID);
  endCheck();
}
function endCheck() {
  timeoutID = setTimeout(() => {
    console.error("time up");
    // myLetter.value = "";
    if (myLetter.value === letters[0].A) {
      console.log("great success")
    } else {
      console.log("try again")
    }
  }, 2000);
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
    <p id="inputBox"> {{myLetter}}</p>
    <div>
      <button id="clicker" @mousedown="mouseDown" @mouseup="mouseUp" class="flex">Space</button>
    </div>
  </section>
  <!-- <section id="gameOver">

  </section> -->
</template>

<style scoped>

</style>
