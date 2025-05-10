from jinja2 import Template

contenido = {
    "poema": [
        "Por el amor incondicional que brindáis,",
        "por ser refugio en la tempestad,",
        "por cada sacrificio callado,",
        "por ser nuestra eterna realidad.",
        "Hoy celebramos esa fuerza sin igual,",
        "que da vida, consuelo y verdad,",
        "¡Feliz día a todas las mamás del mundo,",
        "el mejor regalo de la humanidad!"
    ],
    "firma_autor": "Con cariño, Jesús Vega",
    "fecha": "10 de Mayo de 2024",
    "cancion": "audio/cancion_mama.mp3",  # Ruta relativa
    "flores": ["🌸", "💮", "🌺", "🌷", "🌼"]
}

html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feliz Día de las Madres 🌸</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Pacifico&display=swap" rel="stylesheet">
    <style>
        :root {
            --rosa-principal: #ff69b4;
            --rosa-claro: #ffb3d9;
            --degradado-fondo: linear-gradient(135deg, #ffb3d9, #ff99cc, #ff80b3);
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: var(--degradado-fondo);
            font-family: 'Pacifico', cursive;
            overflow: hidden;
            position: relative;
        }

        .contenedor {
            background: rgba(255, 255, 255, 0.97);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(0, 0, 0, 0.15);
            max-width: 700px;
            text-align: center;
            position: relative;
            margin: 20px;
            backdrop-filter: blur(5px);
            animation: aparecer 1.5s ease-out;
            z-index: 2;
        }

        @keyframes aparecer {
            from { opacity: 0; transform: translateY(50px) scale(0.9); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        .decoracion {
            position: absolute;
            font-size: 2rem;
            animation: flotar 4s infinite ease-in-out;
            opacity: 0.7;
            z-index: 1;
        }

        @keyframes flotar {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-30px) rotate(10deg); }
        }

        .estrella {
            position: absolute;
            width: 3px;
            height: 3px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: brillar 2s infinite;
        }

        @keyframes brillar {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }

        .reproductor {
            margin: 2em auto;
            width: 80%;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 30px;
            padding: 1em;
            box-shadow: 0 5px 15px rgba(255, 51, 102, 0.2);
        }

        .controles {
            display: flex;
            align-items: center;
            gap: 1em;
            justify-content: center;
        }

        .boton-reproducir {
            background: var(--rosa-principal);
            border: none;
            padding: 0.8em 1.5em;
            border-radius: 25px;
            color: white;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Pacifico', cursive;
        }

        .boton-reproducir:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px var(--rosa-principal);
        }

        .barra-progreso {
            flex-grow: 1;
            height: 5px;
            background: #ffe6f0;
            border-radius: 5px;
            cursor: pointer;
            position: relative;
        }

        .progreso {
            width: 0%;
            height: 100%;
            background: var(--rosa-principal);
            border-radius: 5px;
            transition: width 0.1s linear;
        }

        .poema p {
            opacity: 0;
            transform: translateY(20px);
            animation: entrada-texto 0.8s forwards;
            margin: 1em 0;
        }

        @keyframes entrada-texto {
            to { opacity: 1; transform: translateY(0); }
        }

        .firma {
            margin-top: 2em;
            animation: latido 2s infinite;
        }

        @keyframes latido {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        @media (max-width: 768px) {
            .contenedor { padding: 1rem; margin: 10px; }
            .reproductor { width: 95%; }
            .boton-reproducir { padding: 0.6em 1em; }
        }
    </style>
</head>
<body>
    <div class="decoracion" style="top: 10%; left: 5%; animation-delay: 0.5s">🌸</div>
    <div class="decoracion" style="top: 30%; right: 5%; animation-delay: 1s">🌺</div>
    <div class="decoracion" style="bottom: 20%; left: 15%; animation-delay: 1.5s">🌷</div>

    <div id="estrellas-container"></div>

    <div class="contenedor">
        <h1 style="color: var(--rosa-principal); margin-bottom: 1em;">¡Feliz Día de las Madres! 🌸</h1>
        
        <div class="poema">
            {% for linea in poema %}
            <p style="animation-delay: {{ loop.index * 0.3 }}s">{{ linea }}</p>
            {% endfor %}
        </div>

        <div class="reproductor">
            <div class="controles">
                <button class="boton-reproducir" id="playBtn">▶ Reproducir</button>
                <div class="barra-progreso" id="progressBar">
                    <div class="progreso" id="progress"></div>
                </div>
            </div>
            <audio id="audioPlayer" src="{{ cancion }}"></audio>
        </div>

        <div class="firma">
            <p style="color: var(--rosa-principal); margin: 1em 0;">{{ firma_autor }}</p>
            <small style="color: #666;">{{ fecha }}</small>
        </div>
    </div>

    <script>
        // Controlador de música
        const audio = document.getElementById('audioPlayer');
        const playBtn = document.getElementById('playBtn');
        const progress = document.getElementById('progress');

        let isPlaying = false;

        // Event listeners
        playBtn.addEventListener('click', () => {
            isPlaying = !isPlaying;
            playBtn.textContent = isPlaying ? '⏸ Pausar' : '▶ Reproducir';
            if(isPlaying) {
                audio.play().catch(error => {
                    console.error("Error al reproducir:", error);
                    alert("Haz clic en cualquier parte de la página primero");
                });
            } else {
                audio.pause();
            }
        });

        audio.addEventListener('timeupdate', () => {
            const porcentaje = (audio.currentTime / audio.duration) * 100;
            progress.style.width = `${porcentaje}%`;
        });

        document.getElementById('progressBar').addEventListener('click', (e) => {
            const rect = e.target.getBoundingClientRect();
            const pos = (e.clientX - rect.left) / rect.width;
            audio.currentTime = pos * audio.duration;
        });

        // Generar estrellas
        function crearEstrellas() {
            const container = document.getElementById('estrellas-container');
            for (let i = 0; i < 20; i++) {
                const estrella = document.createElement('div');
                estrella.className = 'estrella';
                estrella.style.left = `${Math.random() * 100}%`;
                estrella.style.top = `${Math.random() * 100}%`;
                estrella.style.animationDelay = `${Math.random() * 2}s`;
                container.appendChild(estrella);
            }
        }

        window.addEventListener('load', () => {
            crearEstrellas();
            document.querySelectorAll('.poema p').forEach((p, index) => {
                p.style.animationDelay = `${index * 0.3}s`;
            });
            
            // Permisos de audio
            document.body.addEventListener('click', () => {
                audio.play().then(() => audio.pause());
            }, { once: true });
        });
    </script>
</body>
</html>
"""

template = Template(html_template)
html_final = template.render(contenido)

with open("carta_madres.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("🎉 ¡Carta creada con éxito! Busca 'carta_madres.html'")