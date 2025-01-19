// Add the right passwords for validation
const validpass1 = ' ';
const validpass2 = ' ';
const validpass3 = ' ';
const validpass4 = ' ';

document.getElementById('id_val').addEventListener('submit', function(event) {
event.preventDefault();

const pass = document.getElementById('pass').value.toLowerCase();

if (pass === validpass1 || pass === validpass2 || pass === validpass3 || pass === validpass4) {
    alert('You got it right');
    window.location.href = 'surprise_page.html';
} else {
    document.getElementById('error-message').style.display = 'block';
}
});


// If you want to remove the password's use 
// interchange the logic inside if and else block.
