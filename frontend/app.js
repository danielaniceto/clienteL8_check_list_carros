document.getElementById('loginForm').addEventListener('submit', async (event) => {
    event.preventDefault();
  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    const response = await fetch('http://localhost:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });
  
    if (response.ok) {
      const data = await response.json();
      alert(data.message);
      //redirecionamento
      window.location.href = "/checklist.html";
    } else {
      alert("Invalid credentials");
    }
  });  