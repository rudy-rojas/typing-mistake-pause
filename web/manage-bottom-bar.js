
function setIdsOnButtons() {
  var buttonsAns = $(
    'table#innertable tbody tr td#middle center table tbody tr td button'
  );

  var index = 1;
  buttonsAns.each(function () {
    $(this).attr('id', 'button' + index);
    index++;
  });
}

document.addEventListener('keydown', manageKeyboard);

function disableTempPanel() {
  var buttonsAns = $(
    'table#innertable tbody tr td#middle center table tbody tr td button'
  );

  // Keep the original color of each button
  var originalColors = [];
  //var index = 1;

  buttonsAns.each(function () {
    originalColors.push($(this).css('background-color'));
    //$(this).attr('id', 'button' + index);
    //index++;
  });


  // var valueDataEaseOriginals = [];
  // buttonsAns.each(function () {
  //   valueDataEaseOriginals.push($(this).attr('data-ease'));
  // });

  // Disable the buttonsAns and change the background opacity
  buttonsAns.prop('disabled', true).each(function (index) {
    var boton = $(this);
    boton.css({
      'background-color': function (index, value) {
        // Get the original color in RGBA format and change the opacity to 0.4.
        var rgbaColor = value
          .replace(')', ', 0.4)')
          .replace('rgb', 'rgba');
        return rgbaColor;
      },
    });
    // boton.removeAttr('data-ease');
  });


  // Re-enable the buttonsAns and restore the original styles
  // after `time_pause` (by default is 1200 milliseconds).
  setTimeout(function () {
    buttonsAns.prop('disabled', false).each(function (index) {
      var boton = $(this);
      boton.css('background-color', originalColors[index]);

    });
  }, time_pause); // 3000 milisegundos = 3 segundos
}
