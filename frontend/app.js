const app = document.getElementById("app");

const formHTML = `
    <form id="login-form">
        <h2>Login</h2>
        <label>Usuário:</label><br>
        <input type="text" id="username" placeholder="Digite seu usuário"><br><br>
        <label>Senha:</label><br>
        <input type="password" id="password" placeholder="Digite sua senha"><br><br>
        <button type="button" id="login-btn">Entrar</button>
    </form>
`;

app.innerHTML = formHTML;

document.getElementById("login-btn").addEventListener("click", async () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        const response = await fetch("http://localhost:8000/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            alert("Login feito com sucesso!");
        } else {
            alert("Credenciais inválidas!");
        }
    } else {
        alert("Preencha os campos!");
    }
});
