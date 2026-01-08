# Workflow di Sviluppo

> **IMPORTANTE**: Questo workflow DEVE essere seguito per ogni task di sviluppo.
> Non è opzionale - garantisce qualità, trasparenza e manutenibilità del codice.

## 1. Inizio Task - Analisi delle Decisioni

**All'inizio di OGNI task**, elenca sempre:

- **Decisioni da prendere insieme**: aspetti che richiedono input dell'utente
- **Decisioni autonome**: scelte che prenderesti in autonomia con la relativa motivazione

Questo permette all'utente di chiarire i propri intenti prima dell'implementazione.

### Esempio
```
## Decisioni da prendere insieme
1. Quale formato preferisci per l'output? (JSON, CSV, XML)
2. Il timeout deve essere configurabile o fisso?

## Decisioni autonome
1. Userò asyncio per le chiamate API (motivazione: performance migliori)
2. Aggiungerò retry con exponential backoff (motivazione: resilienza)
```

---

## 2. Implementazione

Durante l'implementazione:

- Segui le convenzioni esistenti nel codice
- Usa type hints Python
- Mantieni la compatibilità con Python 3.10+
- Scrivi codice leggibile e manutenibile

---

## 3. Fine Implementazione - Testing Obbligatorio

**Alla fine di OGNI implementazione**, crea sempre:

### Unit Test
Test isolati per le singole componenti
- Testano funzioni/classi in isolamento
- Usano mock per dipendenze esterne
- Verificano edge cases

### Integration Test
Test end-to-end che verificano il funzionamento completo
- Testano il flusso completo
- Verificano l'integrazione tra componenti
- Simulano scenari reali

**Esegui entrambi i tipi di test** quando possibile per verificare che passino.

---

## 4. Fine Task - Riassunto per Review

**Alla fine del task**, fornisci sempre un riassunto che includa:

### Sviluppi fatti
Cosa è stato implementato/modificato

### Decisioni prese
Scelte tecniche e motivazioni

### Test creati
Quali test sono stati aggiunti e il loro esito

### Note per la review
Eventuali punti di attenzione

---

## 5. Fine Task - Review per Semplificazione

**Dopo il riassunto**, rivedi sempre la soluzione implementata per identificare possibili semplificazioni:

1. **Analizza il codice**: cerca complessità non necessaria, astrazioni premature o duplicazioni
2. **Mantieni le funzionalità**: qualsiasi semplificazione deve preservare tutte le feature richieste
3. **Implementa le semplificazioni**: se trovi miglioramenti, applicali direttamente
4. **Documenta i cambiamenti**: spiega brevemente cosa è stato semplificato e perché

---

## Checklist Rapida

Prima di considerare un task completato, verifica:

- [ ] Ho elencato le decisioni all'inizio?
- [ ] Ho seguito le convenzioni del progetto?
- [ ] Ho creato unit test?
- [ ] Ho creato integration test?
- [ ] Ho eseguito i test?
- [ ] Ho fornito il riassunto completo?
- [ ] Ho rivisto il codice per semplificazioni?

---

## Perché Questo Workflow?

- **Trasparenza**: l'utente sa sempre cosa stai per fare
- **Qualità**: test sistematici = meno bug
- **Manutenibilità**: codice semplice = facile da modificare
- **Collaborazione**: decisioni esplicite = meno incomprensioni
