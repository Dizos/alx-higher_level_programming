$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val().trim();
    if (langCode) {
      const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
      $.get(apiUrl, function (data) {
        $('#hello').text(data.hello);
      });
    }
  }

  // Trigger translation on button click
  $('#btn_translate').click(fetchTranslation);

  // Trigger translation on pressing Enter in the input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Check if Enter key (key code 13) is pressed
      fetchTranslation();
    }
  });
});

