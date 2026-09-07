# Motor de Recomendación por Grupos

Consiste en desarrollar un script que represente a diferentes usuarios y sus intereses mediante conjuntos. Cada usuario tendrá un conjunto de amigos, intereses, películas, productos u otros elementos relacionados. El algoritmo utilizará operaciones de conjuntos como intersección, unión y diferencia para analizar las coincidencias entre los usuarios y generar recomendaciones.

Por ejemplo, si dos usuarios tienen varios amigos en común, el sistema puede identificar esas coincidencias y sugerir que se conecten. De la misma manera, si varios usuarios comparten intereses similares, el programa puede recomendar productos, películas, videojuegos u otros contenidos que podrían ser de su interés.

## Requisitos

- [Python](https://www.python.org/) 3.10 o superior
- pip (incluido con Python)

## Instalación

1. Clona el repositorio:

```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
```

2. Instala las dependencias:

```bash
   pip install -r requirements.txt
```

## Uso

Ejecuta el script base por consola (versión sin interfaz gráfica):

```bash
python Ejemplo1.py
```

Ejecuta la interfaz gráfica con Streamlit:

```bash
streamlit run app_streamlit.py
```

Esto último abre automáticamente el navegador en `http://localhost:8501`.

## Estructura del proyecto

```text
.
├── Ejemplo1.py         # Script base: lógica de conjuntos y motor de recomendación
├── app_streamlit.py    # Interfaz gráfica del motor de recomendación
├── requirements.txt    # Dependencias del proyecto
├── .gitignore
└── README.md
```

## Cómo funciona

- Cada usuario se representa como un **conjunto (`set`)** de intereses.
- **Intersección (`&`)**: calcula los intereses o amigos en común entre dos usuarios.
- **Unión (`|`)**: combina todos los intereses de un grupo sin duplicados.
- **Diferencia (`-`)**: identifica qué le falta a un usuario respecto a otro, usado para generar sugerencias.

## Contribución

1. Crea una rama para tu cambio (`git checkout -b nombre-tarea`).
2. Realiza el cambio y pruébalo localmente antes de subirlo.
3. Sube tu rama y abre un Pull Request hacia `main` describiendo el cambio.
4. Espera revisión del equipo antes de hacer merge.

## Integrantes del grupo

- (agregar los 6 nombres del equipo aquí)

## Licencia

Uso académico — Universidad Mariano Gálvez, Matemática Discreta.