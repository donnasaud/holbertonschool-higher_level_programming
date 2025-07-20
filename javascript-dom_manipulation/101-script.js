document.addEventListener('DOMContentLoaded', function () {
  const button = document.querySelector('#btn_translate');
  const select = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  button.addEventListener('click', function () {
    const lang = select.value;
    if (lang) {
      fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
        .then(response => response.json())
        .then(data => {
          helloDiv.textContent = data.hello;
        })
        .catch(error => {
          helloDiv.textContent = 'Error fetching translation';
        });
    } else {
      helloDiv.textContent = 'Please select a language';
    }
  });
});

