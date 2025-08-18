document.addEventListener('DOMContentLoaded', () => {
  const btnCopiar = document.getElementById('btnCopiarLink');
  const btnWhatsApp = document.getElementById('btnWhatsAppLink');
  const inputPesquisa = document.getElementById('pesquisaNome');
  const listaRespostas = document.getElementById('listaRespostas');

  // Botão de copiar link
  if (btnCopiar) {
    btnCopiar.addEventListener('click', copiarLink);
  }

  // Botão de compartilhar no WhatsApp
  if (btnWhatsApp) {
    btnWhatsApp.addEventListener('click', compartilharWhatsApp);
  }

  // Inicia todas as respostas recolhidas
  listaRespostas?.querySelectorAll('.card-body').forEach(body => {
    body.style.display = 'none';
  });

  // Toggle expandir/recolher
  listaRespostas?.querySelectorAll('.card-header').forEach(header => {
    header.addEventListener('click', () => {
      const card = header.parentElement;
      const body = card.querySelector('.card-body');
      const seta = header.querySelector('.seta');

      if (body.style.display === 'block') {
        body.style.display = 'none';
        seta.style.transform = 'rotate(0deg)';
      } else {
        body.style.display = 'block';
        seta.style.transform = 'rotate(90deg)';
      }
    });
  });

  // Filtro por nome
  inputPesquisa?.addEventListener('input', () => {
    const filtro = inputPesquisa.value.toLowerCase();
    listaRespostas?.querySelectorAll('.resposta-card').forEach(card => {
      const nome = card.getAttribute('data-nome');
      if (nome.includes(filtro)) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

function copiarLink() {
  fetch('/api/gerar-link', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(data.link)
          .then(() => alert("Link copiado para a área de transferência!"))
          .catch(() => fallbackCopiar(data.link));
      } else {
        fallbackCopiar(data.link);
      }
    })
    .catch(error => {
      alert("Erro ao gerar o link: " + error);
    });
}

// Função fallback para copiar link (para navegadores que não suportam navigator.clipboard)
function fallbackCopiar(texto) {
  const inputTemp = document.createElement("textarea");
  inputTemp.value = texto;
  document.body.appendChild(inputTemp);
  inputTemp.select();
  document.execCommand("copy");
  document.body.removeChild(inputTemp);
  alert("Link copiado para a área de transferência!");
}

// Função para gerar link e compartilhar no WhatsApp
function compartilharWhatsApp() {
  fetch('/api/gerar-link', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
      // Certifique-se de que o link tem https://
      const link = data.link.startsWith("http") ? data.link : "https://" + data.link;
      const mensagem = encodeURIComponent("Confira este formulário: " + link);
      const urlWhatsApp = `https://api.whatsapp.com/send?text=${mensagem}`;
      window.location.href = urlWhatsApp; // abre direto no app WhatsApp
    })
    .catch(error => {
      alert("Erro ao gerar o link: " + error);
    });

}
