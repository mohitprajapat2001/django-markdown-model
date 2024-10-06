/*Theme Toggle */
const body = document.querySelector("body");
const themeSelect = document.getElementById("themeSelect");

$(document).ready(() => {
  $("#themeSelect").change((event) => {
    event.preventDefault();
    const currentTheme = event.target.value;
    updateTheme(currentTheme);
    updateThemeLocalStorage(currentTheme);
  });
});

function loadTheme() {
  currentTheme = window.localStorage.getItem("theme");
  updateTheme(currentTheme);
  themeSelect.value = currentTheme;
}
function updateTheme(currentTheme) {
  body.setAttribute("data-theme", currentTheme);
}
function updateThemeLocalStorage(currentTheme) {
  window.localStorage.theme = currentTheme;
}
loadTheme();
