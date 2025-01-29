document.getElementById("cta-button").addEventListener("click", function () {
    fetch("/pontos-coleta/")
        .then(response => response.json())
        .then(data => {
            let listaPontos = document.getElementById("lista-pontos");
            listaPontos.innerHTML = ""; // Limpa a lista antes de adicionar novos itens

            if (data.length === 0) {
                listaPontos.innerHTML = "<p>Nenhum ponto de coleta encontrado.</p>";
                return;
            }

            data.forEach(ponto => {
                let endereco = `${ponto.rua}, ${ponto.numero}, ${ponto.bairro}, ${ponto.cep}`;
                let googleMapsLink = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(endereco)}`;

                let item = document.createElement("li");
                item.innerHTML = `
                    <h3>${ponto.nome_empresa}</h3><br>
                    📍 <a href="${googleMapsLink}" target="_blank" style="color: #1C6CD3; text-decoration: none;">
                        ${ponto.rua}, ${ponto.numero} - ${ponto.bairro}, ${ponto.cep}
                    </a><br>
                    📞 ${ponto.telefone}
                `;
                listaPontos.appendChild(item);
            });

            // Rola suavemente até a lista de pontos de coleta
            document.getElementById("pontos-coleta").scrollIntoView({ behavior: "smooth" });
        })
        .catch(error => console.error("Erro ao carregar os pontos de coleta:", error));
});
