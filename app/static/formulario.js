
const perguntas = [
    // sessao 1
  {
    tipo: "fechada",
    texto: "No dia-a-dia você sente necessidade de hidratar a sua pele?",
    opcoes: {
      A: "Preciso hidratar com cremes pesados ou óleos várias vezes ao dia.",
      B: "Faço 2x ao dia com hidratantes mais cremosos.",
      C: "Apenas 1x ao dia com hidratante mais leve OU não uso nada.",
      D: "Não sinto necessidade de hidratar, minha pele é muito oleosa."
    }
  },
  {
    tipo: "fechada",
    texto: "Qual opção descreve melhor sua pele do rosto?",
    opcoes: {
      A: "Muito seca, racha e descama às vezes.",
      B: "Seca, chega a ficar descamando.",
      C: "Oleosa, forma óleo ao longo do dia.",
      D: "Muito oleosa, dá pra fritar ovo em algumas áreas."
    }
  },
  {
    tipo: "fechada",
    texto: "A oleosidade da sua pele te incomoda?",
    opcoes: {
      A: "Nunca me incomodou.",
      B: "Raramente me incomoda.",
      C: "Me incomoda com frequência.",
      D: "Sempre, praticamente todo dia."
    }
  },
  {
    tipo: "fechada",
    texto: "O ressecamento da sua pele te incomoda?",
    opcoes: {
      A: "Sempre, até maquiagem fica ruim.",
      B: "Com frequência, até no verão.",
      C: "Quase não me incomoda.",
      D: "Nunca me incomodou."
    }
  },
  {
    tipo: "fechada",
    texto: "Você percebe seus poros muito dilatados?",
    opcoes: {
      A: "Não percebo que tenho, não me incomodam.",
      B: "Poucos poros pequenos na “zona T”.",
      C: "Poros bem aparentes no nariz ou outras áreas.",
      D: "Muitos poros grandes, me incomodam com cravos."
    }
  },
  //sessao 2
  {
    tipo: "fechada",
    texto: "Produtos para cuidado com a pele (incluindo sabonetes comuns, hidratantes, tônicos, protetor solar e maquiagem) causam irritação, coceira, vermelhidão, ardência ou “alergia” em sua pele?",
    opcoes: {
      A: "Nunca aconteceu.",
      B: "É muito raro!",
      C: "Acontece com alguma frequência OU Não sei, pois nunca uso nada disso.",
      D: "Sempre acontece ou geralmente nem testo, porque sei que vou ter problemas, já tive muitas vezes."
    }
  },
  {
    tipo: "fechada",
    texto: "Nas últimas 4 semanas, você apresentou alguma dessas questões na pele: espinha ou bolinhas inflamadas, ardência, irritação, vermelhidão, inchaço no rosto, pele quente ou coçando?",
    opcoes: {
      A: "Não tive nenhum desses.",
      B: "ive apenas um desses uma única vez.",
      C: "Tive alguns desses algumas vezes",
      D: "Tive quase todos esses várias vezes!."
    }
  },
  {
    tipo: "fechada",
    texto: " Você tem ou já teve diagnóstico de acne, rosácea, eczema ou dermatite atópica (inflamação ou erupções na pele) ou dermatite de contato (alergia por uso de bijuterias por exemplo)?",
    opcoes: {
      A: "Nunca tive nenhum desses.",
      B: "Tive apenas um desses OU Não sei dizer.",
      C: "Já tive 2 desses diagnósticos.",
      D: "Tive 3 ou mais desses diagnósticos."
    }
  },
  {
    tipo: "fechada",
    texto: "Você apresenta pápulas (bolinhas) vermelhas na pele, ou as pessoas dizem que seu rosto está sempre vermelho, mesmo sem pegar sol? Sua pele fica vermelha após exercícios físicos, uso de álcool, bebidas quentes, banho quente, ou alimentos apimentados?",
    opcoes: {
      A: "Nunca.",
      B: "Já aconteceu uma vez OU Não sei dizer.",
      C: "Sim, isso acontece e algumas vezes.",
      D: "Isso acontece com bastante frequência!"
    }
  },
  // sessao 3
  {
    tipo: "fechada",
    texto: "Se tiver uma pápula (“bolinha vermelha”), uma “espinha” um pelo encravado, ou mesmo um corte ou ferimento, no local fica uma mancha castanha ou um ponto mais escuro (NÃO é uma mancha avermelhada, é bem mais marrom escura mesmo)?",
    opcoes: {
      A: "Nunca.",
      B: "Raramente OU Não sei dizer.",
      C: "Com alguma frequência.",
      D: "Sempre."
    }
  },
  {
    tipo: "fechada",
    texto: "Quando a sua pele é exposta ao sol o que acontece? (Se estiver há muitos anos sem tomar sol; tente lembrar como reagia sua pele na infância).",
    opcoes: {
      A: "Ela fica vermelha, não bronzeia nada ou quase nada.",
      B: "Fica vermelha, depois até fica bem levemente bronzeada.",
      C: "Fica mais bronzeada ou morena.",
      D: "A minha pele é negra ou muito morena, por isso é até difícil avaliar se ela fica mais escura."
    }
  },
  {
    tipo: "fechada",
    texto: "Você tem ou ja teve diagnóstico de melasma, tem algum tipo de mancha escura no buço (pele sobre o lábio superior), bochechas abaixo dos olhos ou testa ou teve manchas escuras quando engravidou ou tomou anticoncepcional?",
    opcoes: {
      A: "Nunca tive.",
      B: "Acho que já tive, mas saiu sozinha OU Nunca percebi.",
      C: "Sim, já tive e acontece com alguma frequência (mesmo que trate e melhore, depois volta).",
      D: "Tenho muitas manchas que acabam piorando, não aguento mais!"
    }
  },
  {
    tipo: "fechada",
    texto: "A pigmentação da sua pele é irregular e você tem manchas escuras que pioram quando pega sol ou calor? O quanto isso te incomoda?",
    opcoes: {
      A: "Minha pigmentação é uniforme e eu não tenho nenhuma área escura que me incomoda.",
      B: "Eu tenho sardinhas ou manchinhas escuras, mas não pioram e não me incomodam.",
      C: "A pigmentação da minha pele é irregular, às vezes piora e me incomoda um pouco.",
      D: "Tenho muitas manchas, pigmentação irregular que piora e me incomoda bastante!"
    }
  },
  //sessao 4
  {
    tipo: "fechada",
    texto: " Você tem rugas no rosto?",
    opcoes: {
      A: "Não, mesmo quando faço expressões faciais (como sorrir ou franzir a testa).",
      B: "Somente ao sorrir, franzir a testa ou outras expressões faciais.",
      C: "Sim, ao fazer expressões faciais e algumas mesmo sem movimento.",
      D: "As rugas estão presentes mesmo quando não estou sorrindo, franzindo a testa ou fazendo outras expressões faciais."
    }
  },
  {
    tipo: "fechada",
    texto: "Você tem ou já teve o costume de se bronzear intencionalmente por mais de 2 semanas por ano (pegar sol nas férias por exemplo) ou já fez bronzeamento com luz artificial?",
    opcoes: {
      A: "Nunca fiz isso.",
      B: "Já tomei sol por mais de 2 semanas (ou fiz bronzeamento artificial), mas fiz isso menos de 5 vezes na vida.",
      C: "Fiquei pegando sol nas férias (ou fiz bronzeamento artificial) por volta de 5 a 10 vezes na vida.",
      D: "Já fiz um e/ou outro mais de 10 vezes na vida."
    }
  },
  {
    tipo: "fechada",
    texto: "Qual idade as pessoas dizem ou você acha que aparenta?",
    opcoes: {
      A: "De 1 a 5 anos mais nova que sua idade.",
      B: "Exatamente sua idade.",
      C: "De 1 a 5 anos a mais que sua idade.",
      D: "Mais de 5 anos a mais que sua idade."
    }
  },
  {
    tipo: "fechada",
    texto: "Durante a sua vida, quantos cigarros você já fumou (considerar também exposição passiva)?",
    opcoes: {
      A: "Nenhum",
      B: "Poucos maços OU Nunca fumei, mas  sempre estive exposto passivamente ao cigarro (“fumante passivo”).",
      C: "Muitos ou vários maços.",
      D: "Fumo todos os dias."
    }
  },
  {
    tipo: "fechada",
    texto: "Qual a cor natural de sua pele? (Considere pele as áreas cobertas e sem bronzeado, nem autobronzeamento).",
    opcoes: {
      A: "Negra.",
      B: "Morena.",
      C: "Clara.",
      D: "Muito clara."
    }
  },
  {
    tipo: "fechada",
    texto: "O quanto a questão do envelhecimento e rugas te incomodam?",
    opcoes: {
      A: "Definitivamente não me incomoda.",
      B: "Me incomoda um pouco, não é a minha questão principal.",
      C: "Me incomoda, é uma questão bem relevante pra mim!",
      D: "Me incomoda muito, é a minha queixa principal!"
    }
  },
  // sessao 3
  {
    tipo: "fechada",
    texto: "Atualmente quando você usa o seu sabonete comum, como a pele do seu rosto fica?",
    opcoes: {
      A: "Fica com uma sensação de repuxamento (tensionamento), craquelada.",
      B: "Fica bem adequada, confortável OU Não sei, não sinto nada."

    }
  },
  {
    tipo: "fechada",
    texto: "No dia-a-dia, caso você não aplique hidratante, como você sente a pele do rosto?",
    opcoes: {
      A: "Sinto minha pele opaca, sem viço, pode chegar até a ficar desconfortável repuxando e/ou sinto sim uma necessidade de usar o hidratante.",
      B: "Não sinto necessidade alguma de hidratante, fica bem equilibrada durante o dia OU Não sei, fica normal, não sinto nada."
    }
  },
  {
    tipo: "fechada",
    texto: "Em geral, você sente que sua pele fica tensionada, repuxando, opaca, sem viço? Isso te incomoda?",
    opcoes: {
      A: "Sinto com frequência, e por isso me incomoda sim!",
      B: "Não me incomoda, não costumo sentir isso."
    }
  },
  {
    tipo: "aberta",
    texto: "Você já cuida da sua pele? Há quanto tempo?",
  },
  {
    tipo: "aberta",
    texto: "O que você já faz de fato na sua rotina de skincare (tudo bem se não fizer nada!)? Quais os produtos você usa diariamente na sua rotina? Tire foto dos produtos que você já tem, usa e gosta e me envie, se possível separado pela rotina que você já faz e por categoria (ex: hidratantes, tenho esses aqui...). Vamos tentar aproveitar o máximo possível o que você já tem!",
  },
  {
    tipo: "aberta",
    texto: "Quais são suas queixas quando fala sobre pele? Pode listar tudo o que te incomoda aqui.",
  },
  {
    tipo: "aberta",
    texto: "Se pudesse escolher 1 só objetivo em relação a melhorar alguma das queixas acima, o que você escolheria? Ou seja, o que MAIS te incomoda atualmente?",
  },
  {
    tipo: "aberta",
    texto: "Você já fez algo ou usou / faz uso de algum produto ou medicamento para tratar alguma dessas suas queixas?",
  },
  {
    tipo: "aberta",
    texto: "No momento você está grávida ou amamentando? Pretende engravidar nesses próximos meses? *por gentileza avisar ao suporte se porventura descobrir que estiver grávida depois do início do tratamento para que possamos ajustar a rotina se necessário",
  },
    {
    tipo: "fechada",
    texto: "Qual dessas duas afirmações melhor te define?",
    opcoes: {
      A: "Gosto de estar sempre usando um produtinho diferente e variar a rotina com muitos produtos.",
      B: "Sou enxuta e pratica, gosto de rotina básica e efetiva com poucos passos."
    }
  },
{
    tipo: "aberta",
    texto: "Você tem preferência por alguma marca de skincare?",
  },
{
    tipo: "fechada",
    texto: "Você prefere:",
    opcoes: {
      A: "Ter muitas opções para decidir em conjunto.",
      B: " Ter poucas opções mais assertivas."
    }
  },
  {
    tipo: "aberta",
    texto: "Qual é a sua profissão? Em média, quanto tempo de exposição solar você tem no seu dia-a-dia (durante o trabalho ou no trajeto, por exemplo)?",
  },
  {
    tipo: "aberta",
    texto: "Como é a sua rotina no dia-a-dia? Vai à academia? Se sim, qual horário?",
  },

    {
    tipo: "aberta",
    texto: "Como é a sua alimentação? Tem alguma restrição ou alergia alimentar? Faz alguma suplementação?"
    },
    {
    tipo: "aberta",
    texto: "Já teve alguma alergia ou irritação por causa de algum produto ou ativo? Há algum produto que não gostou e não usaria de novo?"
    },
    {
    tipo: "aberta",
    texto: "Você tem algum diagnóstico prévio de alguma doença ou condição de pele?"
    },
    {
    tipo: "aberta",
    texto: "Você faz ou fez uso de algum medicamento que seja relevante informar?"
    },
    {
    tipo: "aberta",
    texto: "Você já acompanha ou acompanhou com algum dermatologista? Se algum outro profissional está te ajudando com a sua pele em conjunto nesse momento, me informe por gentileza o contato para que possamos trocar informações a fim de te ajudar"
    },
    {
    tipo: "aberta",
    texto: "Como está seu orçamento para compra de novos produtos?"
    },
{
    tipo: "fechada",
    texto: "Você prefere:",
    opcoes: {
      A: "Mais apertado, preciso gastar o mínimo possível.",
      B: "Consigo investir em novos produtos se de fato valerem a pena."
    }
  },
    {
    tipo: "aberta",
    texto: "Qual resultado você espera que você tenha ao final da consultoria para você dizer que valeu a pena?"
    }
];
// Seu array 'perguntas' aqui (copie as perguntas que você já tem)

let indice = 0;
let respostas = {};
let respostaAtual = null;

const questionText = document.getElementById("questionText");
const optionsContainer = document.getElementById("optionsContainer");
const nextBtn = document.getElementById("nextBtn");
const progressFill = document.getElementById("progressFill");

function renderizarPergunta() {
  const atual = perguntas[indice];
  questionText.textContent = `${indice + 1}) ${atual.texto}`;
  optionsContainer.innerHTML = "";
  respostaAtual = null;

  if (atual.tipo === "fechada") {
    for (let letra in atual.opcoes) {
      const btn = document.createElement("button");
      btn.textContent = `${letra}) ${atual.opcoes[letra]}`;
      btn.addEventListener("click", () => {
        respostaAtual = letra;
        document.querySelectorAll(".options button").forEach(b => b.classList.remove("selected"));
        btn.classList.add("selected");
        nextBtn.disabled = false;
      });
      optionsContainer.appendChild(btn);
    }
  } else if (atual.tipo === "aberta") {
    const textarea = document.createElement("textarea");
    textarea.rows = 4;
    textarea.style.width = "100%";
    textarea.placeholder = "Digite sua resposta aqui...";
    textarea.addEventListener("input", () => {
      respostaAtual = textarea.value.trim();
      nextBtn.disabled = respostaAtual.length === 0;
    });
    optionsContainer.appendChild(textarea);
  }

  let progresso = (indice / perguntas.length) * 100;
  progressFill.style.width = progresso + "%";
  nextBtn.disabled = true;
}

nextBtn.addEventListener("click", () => {
  respostas[(indice + 1).toString()] = respostaAtual;
  indice++;

  if (indice < perguntas.length) {
    renderizarPergunta();
  } else {
    enviarRespostas();
  }
});

function enviarRespostas() {
  questionText.textContent = "Enviando respostas...";
  optionsContainer.innerHTML = "";
  nextBtn.style.display = "none";
  progressFill.style.width = "100%";

  fetch(`/formulario/${form_id}/Skin`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(respostas)
  })
    .then(response => response.json())
    .then(data => {
      questionText.textContent = "Quiz finalizado!";

      if (data.resultado) {
        const r = data.resultado;
        const resultadoTexto = `
          <h3>Resultado da sua pele:</h3>
          <ul>
            <li><strong>Oleosidade:</strong> ${r["O x D"]}</li>
            <li><strong>Sensibilidade:</strong> ${r["S x R"]}</li>
            <li><strong>Pigmentação:</strong> ${r["P x N"]}</li>
            <li><strong>Firmeza:</strong> ${r["W x T"]}</li>
            <li><strong>Hidratação:</strong> ${r["Hidratação"]}</li>
            <li><strong>Código final:</strong> <span style="font-weight:bold">${r["Tipo_de_pele"]}</span></li>
          </ul>
        `;

        optionsContainer.innerHTML = resultadoTexto;
      } else {
        optionsContainer.innerHTML = `<p>${data.mensagem}</p>`;
      }
    })
    .catch(err => {
      questionText.textContent = "Erro ao enviar.";
      optionsContainer.innerHTML = `<p>Ocorreu um erro. Tente novamente.</p>`;
      console.error(err);
    });
}

// codigo para teste
document.getElementById("autoFillBtn").addEventListener("click", () => {
  respostas = {};
  indice = 0;

  function responderAutomaticamente() {
    if (indice >= perguntas.length) {
      enviarRespostas();
      return;
    }

    const atual = perguntas[indice];

    if (atual.tipo === "fechada") {
      const letras = Object.keys(atual.opcoes);
      respostaAtual = letras[Math.floor(Math.random() * letras.length)];
    } else {
      respostaAtual = "teste automático";
    }

    respostas[(indice + 1).toString()] = respostaAtual;
    indice++;
    renderizarPergunta();

    setTimeout(responderAutomaticamente, 100);
  }


  responderAutomaticamente();
});

renderizarPergunta();


