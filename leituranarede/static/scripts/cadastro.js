document.getElementById('cadastroForm').addEventListener('submit', function(event) {
      var nome = document.getElementById('nome').value;
      var telefone = document.getElementById('telefone').value;
      var email = document.getElementById('email').value;
      var senha = document.getElementById('senha').value;
      var confirmarSenha = document.getElementById('confirmar_senha').value;

      var nomeError = document.getElementById('nomeError');
      var telefoneError = document.getElementById('telefoneError');
      var emailError = document.getElementById('emailError');
      var senhaRequisitos = document.getElementById('senhaRequisitos');
      var senhaError = document.getElementById('senhaError');

      var isValid = true;
  
      nomeError.style.display = 'none';
      telefoneError.style.display = 'none';
      emailError.style.display = 'none';
      senhaRequisitos.style.display = 'none';
      senhaError.style.display = 'none';

      if (!nome) {
        nomeError.style.display = 'block';
        isValid = false;
      }

      var telefoneValido = false;
      if (/^\d{10}$/.test(telefone) && /^[2-5]/.test(telefone.slice(2))) { // Fixed line
        telefone = telefone.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
        telefoneValido = true;
      } else if (/^\d{11}$/.test(telefone) && telefone[2] == '9') { // Mobile
        telefone = telefone.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
        telefoneValido = true;
      } else {
        telefoneValido = false;
      }

      if (!telefoneValido) {
        telefoneError.style.display = 'block';
        isValid = false;
      }

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

      if (senha !== confirmarSenha) {
        senhaError.style.display = 'block';
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

    document.getElementById('toggleConfirmarSenha').addEventListener('click', function() {
      showPasswordTemporarily('confirmar_senha', 'toggleConfirmarSenha');
    });