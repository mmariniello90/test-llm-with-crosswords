# test-llm-with-crosswords

Questo progetto testa la capacità di **GPT-5** di risolvere un semplice cruciverba.

## Istruzioni per l'uso

1. Installa le dipendenze con `uv`.
2. Scatta una foto del cruciverba (includendo solo lo schema).
3. Scatta una foto delle definizioni (senza includere lo schema).
4. Chiedi a ChatGPT (con GPT-5) di estrarre le definizioni e organizzarle in formato JSON.  
   Questo è il prompt che ho utilizzato:

   > Estrai in una lista di dizionari le definizioni di questo cruciverba. Segui questa struttura:  
   > **Esempio di output:**
   > ```json
   > [
   >     {
   >         "numero": 1,
   >         "orientamento": "orizzontale",
   >         "definizione": "Quesito di esempio da risolvere."
   >     },
   >     {
   >         "numero": 2,
   >         "orientamento": "verticale",
   >         "definizione": "Altro quesito di esempio da risolvere."
   >     }
   > ]
   > ```

5. Copia il JSON in un file chiamato `clues.json` e salvalo in `app/crosswords/`.
6. Carica le due immagini nella cartella `app/crosswords/`.
7. Esegui lo script `solve_crossword.py` con il comando:
   ```bash
   uv run app/solve_crossword.py
