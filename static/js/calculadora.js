document.getElementById('calcForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // let porque é necessário substituir por 0 caso o campo esteja vazio
    let litros_combustivel = document.getElementById('litros_combustivel').value.trim(); // value.trim() remove espaços em branco no início e no final
    let energia_gasta = document.getElementById('energia_gasta').value.trim();
    let gas = document.getElementById('gas').value.trim();
    let etanol = document.getElementById('etanol').value.trim();
    let diesels10 = document.getElementById('diesels10').value.trim();
    let diesels500 = document.getElementById('diesels500').value.trim();
    let onibus = document.getElementById('onibus').value.trim();

      // Substitui valores vazios por zero
    litros_combustivel = litros_combustivel === '' ? 0 : parseFloat(litros_combustivel);
    energia_gasta = energia_gasta === '' ? 0 : parseFloat(energia_gasta);
    gas = gas === '' ? 0 : parseFloat(gas);
    etanol = etanol === '' ? 0 : parseFloat(etanol);
    diesels10 = diesels10 === '' ? 0 : parseFloat(diesels10);
    diesels500 = diesels500 === '' ? 0 : parseFloat(diesels500);
    onibus = onibus === '' ? 0 : parseFloat(onibus);


    console.log(`Enviando dados: litros_combustivel=${litros_combustivel}, energia_gasta=${energia_gasta}, gas=${gas}, etanol=${etanol}, diesels10=${diesels10}, diesels500=${diesels500}, onibus=${onibus}`);  //  depuração

    fetch('/calcular', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        litros_combustivel: litros_combustivel,
        energia_gasta: energia_gasta,
        gas: gas,
        etanol: etanol,
        diesels10: diesels10,
        diesels500: diesels500,
        onibus: onibus
    })
    })
      .then(response => {
        console.log('Resposta bruta recebida:', response);  // Adiciona uma mensagem de depuração
        return response.json();
      })
      .then(data => {
        console.log(`Resposta recebida: ${data.emissao} kg`); 
        console.log(`Resposta recebida: ${data.arvores} `);// Adiciona uma mensagem de depuração
        const emissao = data.emissao;
        const arvores = data.arvores;
        const derretimento = data.derretimento;
        const desmatamento = data.desmatamento;
        const km = data.km;
        const resultadoDiv = document.getElementById('resultado');

         // Limpa o conteúdo anterior
        resultadoDiv.innerHTML = '';
        // Adiciona o novo conteúdo
        resultadoDiv.innerHTML += `<h2>Sua emissão mensal de CO₂ é de aproximadamente ${emissao} kg.</h2> `;

        if( emissao <= 500){
          resultadoDiv.innerHTML += `
          <p>Sua pegada de carbono está abaixo da média nacional! Parabéns! 🎉 </p> 
          `;
        }
        if( emissao > 500 && emissao < 916){
          resultadoDiv.innerHTML += `
          <p>Você está dentro da média, mas ainda pode reduzir sua pegada de carbono. 🎯</p>
          `;
        }
        if( emissao >= 916){
          resultadoDiv.innerHTML += `
          <p>Alerta vermelho! 🚨 Suas emissões estão acima da média nacional.</p>
          `;
        }

        resultadoDiv.innerHTML +=  `  
                <p>🪴 Você precisaria plantar ${arvores} árvores para neutralizar sua pegada de carbono.</p>
                <p>❄️ Ela resulta no derretimento de ${derretimento} litros das calotas polares por mês.</p>
                <p>🚗 Equivale a dirigir ${km} km com um carro econômico a gasolina. </p>
                <p>🔥 A sua emissão equivale a ${desmatamento}m² de desamatamento florestal.</p>
                <p>Lembre-se, não são valores exatos, mas sim aproximados devido as variabilidades dos fatores cotidianos.</p>
                
      `;
      document.getElementById('shareButton').style.display = 'block';


    })
    .catch(error => console.error('Erro:', error));
  });
