document.getElementById("cta-button").addEventListener("click", function () {
    fetch("/pontos-coleta/")
        .then(response => response.json())
        .then(data => {
            let listaPontos = document.getElementById("lista-pontos");
            listaPontos.innerHTML = ""; // Limpa antes de adicionar novos itens

            if (data.length === 0) {
                listaPontos.innerHTML = "<p>Nenhum ponto de coleta encontrado.</p>";
                return;
            }

            data.forEach(ponto => {
                let item = document.createElement("li");
                item.innerHTML = `<strong>${ponto.nome_empresa}</strong><br>
                                  📍 ${ponto.rua}, ${ponto.numero} - ${ponto.bairro}, ${ponto.cep}<br>
                                  📞 ${ponto.telefone}`;
                listaPontos.appendChild(item);
            });
        })
        .catch(error => console.error("Erro ao carregar os pontos de coleta:", error));
});
