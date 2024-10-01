document.getElementById('loginForm').addEventListener('submit', function(event) {
  var email = document.getElementById('email').value;
  var senha = document.getElementById('senha').value;

  var emailError = document.getElementById('emailError');
  var senhaRequisitos = document.getElementById('senhaRequisitos');

  var isValid = true;

  emailError.style.display = 'none';
  senhaRequisitos.style.display = 'none';

  var emailValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  if (!emailValido) {
    emailError.style.display = 'block';
    isValid = false;
  }

  var senhaValida = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/.test(senha);
  if (!senhaValida) {
    senhaRequisitos.style.display = 'block';
    isValid = false;
  }

  if (!isValid) {
    event.preventDefault();
  }
});

function showPasswordTemporarily(inputId, iconId) {
  var input = document.getElementById(inputId);
  var icon = document.getElementById(iconId);
  input.setAttribute('type', 'text');
  icon.classList.toggle('fa-eye');
  icon.classList.toggle('fa-eye-slash');
  setTimeout(function() {
    input.setAttribute('type', 'password');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
  }, 1000);
}

document.getElementById('toggleSenha').addEventListener('click', function() {
  showPasswordTemporarily('senha', 'toggleSenha');
});