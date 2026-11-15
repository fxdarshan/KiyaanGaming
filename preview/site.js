// Contact page: pre-select the game from the address (contact.html?game=slug)
// and explain that the preview form is not connected yet.
(function () {
  var form = document.getElementById('enquiry-form');
  if (!form) return;

  var game = new URLSearchParams(window.location.search).get('game');
  var gameField = document.getElementById('game');
  var interest = document.getElementById('interest');
  if (game && gameField) {
    for (var i = 0; i < gameField.options.length; i++) {
      if (gameField.options[i].value === game) {
        gameField.value = game;
        if (interest) interest.value = 'game';
        break;
      }
    }
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    var status = document.getElementById('form-status');
    if (status) {
      status.hidden = false;
      status.focus();
    }
  });
})();
