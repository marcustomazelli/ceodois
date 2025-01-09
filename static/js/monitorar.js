// Inicializa o mapa usando a biblioteca Leaflet
const map = L.map('map').setView([-14.2350, -51.9253], 4); // Centralizado no Brasil
// Adiciona uma camada de tiles ( ruas, cidades e outros detalhes) do OpenStreetMap ao mapa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

 // Buscar os dados do backend
fetch('/api/queimadas')// Faz uma requisição para a URL do backend que fornece os dados das queimadas
    .then(response => response.json())  // Converte a resposta para JSON
    .then(data => {
         // Adicionar os pontos no mapa
        data.forEach(fire => {  // Para cada ponto de queimada no conjunto de dados
            L.circleMarker([fire.latitude, fire.longitude], { // Cria um marcador circular no mapa
                color: 'red',
                radius: 5,
                fillOpacity: 0.7
            })
            .addTo(map) // Adiciona o marcador ao mapa
            .bindPopup(() => {
                const brilho = fire.brightness !== undefined ? fire.brightness : 'N/A';
                const confianca = fire.confidence !== undefined ? fire.confidence : 'N/A';
                return `<b>Brilho:</b> ${brilho}<br><b>Confiança:</b> ${confianca}`;
            }); 
        });
    })
    .catch(error => console.error('Erro ao buscar os dados:', error)); // Captura e exibe erros na requisição


    
    