const validpass1 = 'panditji';
const validpass2 = 'swami';
const validpass3 = 'prabhu';
const validpass4 = 'devta';

document.getElementById('id_val').addEventListener('submit', function(event) {
event.preventDefault();

const pass = document.getElementById('pass').value.toLowerCase();

// Validate the credentials
if (pass === validpass1 || pass === validpass2 || pass === validpass3 || pass === validpass4) {
    alert('You got it right');
    window.location.href = 'surprise_page.html';
} else {
    document.getElementById('error-message').style.display = 'block';
}
});
