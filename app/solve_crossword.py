import json
import base64
import io
from PIL import Image
from openai import OpenAI
from rich.markdown import Markdown
from rich.panel import Panel
from rich.console import Console
from dotenv import load_dotenv
from string import Template

console = Console()
load_dotenv()
client = OpenAI()

context = Template("""
Aiutami a risolvere questo cruciverba in italiano.

Vedrai l'immagine del cruciverba così potrai capire la lunghezza delle parole da inserire.

Avrai in input un JSON con le seguenti informazioni:

- numero della cella
- orientamento
- definizione

Ad esmpio:

```json
[
    {
        "numero": 1,
        "orientamento": "orizzontale",
        "definizione": "Manifestazioni sismiche."
    },
    {
        "numero": 6,
        "orientamento": "orizzontale",
        "definizione": "I valori delle valute."
    },
    ...
    ...
]
```

Di seguito il JSON dove troverai le definizioni:

 ## JSON:
 $json
 
 Il tuo obiettivo è quello di trovare le risposte corrette.
Per ogni risposta che provi a risolvere, crea una struttura che faciliti la mia lettura, ad esempio:
- Numero di cella
- Orientamento
- Definizione
- Numero di celle (queste le vedi dall'immagine)

""")


def open_image(image_path: str) -> Image.Image:
    return Image.open(image_path)


def encode_image(image: Image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


clues_image_path = "app/crosswords/cruciverba.jpeg"

crossword_img = open_image(image_path=clues_image_path)
b64_crossword_img = encode_image(image=crossword_img)


with open("app/crosswords/clues.json", "r") as file:
    data = json.load(file)

json_text = str(json.dumps(data))


response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": f"{context.substitute({'json': json_text})}",
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{b64_crossword_img}",
                },
            ],
        }
    ],
)


console.print(
    Panel(
        Markdown(response.output_text),
        title="[deep_sky_blue1]AI[/deep_sky_blue1]",
        title_align="left",
        border_style="#12a0d7",
    )
)

print(f"TOTAL TOKEN: {response}")
