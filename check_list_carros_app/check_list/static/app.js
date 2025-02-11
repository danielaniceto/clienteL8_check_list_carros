document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Impede o envio tradicional do formulário

  // Captura os valores dos campos do formulário
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;

  // Envia os dados para a API usando fetch
  fetch('/api/login/', { // Substitua com o URL correto da sua API
      method: 'POST',
      headers: {
          'Content-Type': 'application/json', // Indica que estamos enviando JSON
      },
      body: JSON.stringify({ // Converte os dados para o formato JSON
          username: username,
          password: password
      })
  })
  .then(response => response.json()) // Recebe a resposta da API em formato JSON
  .then(data => {
      console.log(data); // Aqui você pode tratar a resposta da API
      if (data.success) {
          window.location.href = "/dashboard"; // Redireciona após login bem-sucedido
      } else {
          alert("Login falhou: " + data.message);
      }
  })
  .catch(error => {
      console.error("Erro ao fazer login:", error);
      alert("Erro de conexão com a API.");
  });
});