// Exemplo básico de JavaScript para exibir o mapa e outros efeitos
document.addEventListener('DOMContentLoaded', function() {
    const ctaButton = document.getElementById('cta-button');

    ctaButton.addEventListener('click', function() {
        // Ação quando o botão de CTA for clicado (pode ser expandido)
        alert('Mapa de pontos de coleta em breve!');
        scrollToSection('collection-points');
    });

    // Função para rolar suavemente até a seção de pontos de coleta
    function scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Mapa fictício por enquanto (substitua por API de mapas, como Google Maps)
    const map = document.getElementById('map');
    map.innerHTML = '<p style="text-align:center; padding-top: 150px;">Mapa de pontos de coleta em breve...</p>';
});
