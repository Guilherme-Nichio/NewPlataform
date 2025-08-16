
  const inputPesquisa = document.getElementById("pesquisaNome");
  const linhas = document.querySelectorAll("tbody tr");

  inputPesquisa.addEventListener("keyup", function() {
    const valor = this.value.toLowerCase();

    linhas.forEach(linha => {
      const email = linha.querySelector("td[data-label='Email']").textContent.toLowerCase();

      if (email.includes(valor)) {
        linha.style.display = "";  // mostra a linha
      } else {
        linha.style.display = "none"; // esconde
      }
    });
  });
