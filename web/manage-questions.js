function setEscapeTypeCorrect(typeCorrect) {
    setTimeout(function() {
        var el = document.querySelector('#typeans .typeGood');
        if (el) {
            el.innerText = typeCorrect;
        }
    }, 100);
}


function keydownHandler(event) {
 
  if (event.key === again_option) {
    pycmd("ease1");
    document.removeEventListener("keydown", keydownHandler);
    // disableKeydownHandler();
  } else if (event.key === hard_option) {
    pycmd("ease2");
    document.removeEventListener("keydown", keydownHandler);
    // disableKeydownHandler();
  } else if (event.key === good_option) {
    pycmd("ease3");
    document.removeEventListener("keydown", keydownHandler);
    // disableKeydownHandler();
  } else if (event.key === easy_option) {
    pycmd("ease4");
    document.removeEventListener("keydown", keydownHandler);
    // disableKeydownHandler();
  }
}

function disableTempKeydownHandler() {
  document.removeEventListener("keydown", keydownHandler);
  setTimeout(function () {
    document.addEventListener("keydown", keydownHandler);
  }, time_pause); // 3000 milisegundos = 3 segundos
}

