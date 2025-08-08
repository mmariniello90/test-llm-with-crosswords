# test-llm-with-crosswords

Testiamo la capacità di gpt-5 di risolvere un semplice cruciverba.

# Istruzione per l'uso

- Installa le dipendendo con `uv`
- Scatta una foto del cruciverba (che includa solo lo schema)
- Scatta una foto delle definizioni (che non includa lo schema)
- Chiedi a ChatGPT (con gpt-5) di estrarre le definizioni ed organizzarle in formato JSON.
  Questo è il prompt usato da me:
 > Estrai in una lista di dizionari le definizioni di questo cruciverba. Segui questa struttura:
      # Esempio di output:
        [
            {
                "numero": 1
                "orientamento": "orizzontale",
                "definizione": "Quesito di esempio da risolvere."
            },
            {
                "numero": 2
                "orientamento": "verticale",
                "definizione": "Altro quesito di esempio da risolvere."
            },
        ]
 - Copia il JSON in un file chiamato `clues.json` e salvalo in `app/crosswords/`.
 - Carica le due immagini nella cartella `àpp/crosswords/`.
   - Esegui lo script ``solve.crossword.py`` con il comando:
      ```bash
      uv run app/solve_crossword.py
      ```
 - Enjoy



