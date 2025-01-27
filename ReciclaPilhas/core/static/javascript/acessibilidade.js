window.addEventListener('load', () => {
    const aumentarFonte = document.getElementById('aumentar-fonte');
    const diminuirFonte = document.getElementById('diminuir-fonte');
    const normalizarFonte = document.getElementById('normalizar-fonte');
    const contraste = document.getElementById('contraste');
    //const vlibrasButton = document.getElementById('vlibras-button');  // Certifique-se de que esta linha está presente

    let fontSize = 1;

    if (aumentarFonte) {
        aumentarFonte.addEventListener('click', function () {
            if (fontSize <= 1.4) {
                fontSize += 0.1;
                document.body.style.fontSize = fontSize + 'em';
            }
        });
    }

    if (diminuirFonte) {
        diminuirFonte.addEventListener('click', function () {
            if (fontSize > 0.8) {
                fontSize -= 0.1;
                document.body.style.fontSize = fontSize + 'em';
            }
        });
    }

    if (normalizarFonte) {
        normalizarFonte.addEventListener('click', function () {
            fontSize = 1;
            document.body.style.fontSize = '1em';
        });
    }

    if (contraste) {
        contraste.addEventListener('click', function () {
            document.body.classList.toggle('alto-contraste');
        });
    }

    
});
