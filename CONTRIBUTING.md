# Beiträge und langfristige Pflege

## Neue Quelle aufnehmen

1. Sachliche Zugehörigkeit und Freigabeumfang prüfen. Persönliches, Korrespondenz und künstlerische Begleitmaterialien gehören nicht in diese Sammlung.
2. Stabile Quellen-ID anlegen. Google-Datei-ID, ursprünglichen Titel, MIME-Typ, Zeitstempel und Herkunft notieren. Lokale Herkunft über Quellwurzel-Bezeichnung und relativen Pfad dokumentieren.
3. Originaldatei unverändert sichern. Texte aus PDF, Word oder Drive als abgeleitete Darstellung kennzeichnen. Formatierung und Extraktionsverluste nicht als Textänderung verschweigen.
4. SHA-256 über die gespeicherten Bytes berechnen. Für den Vergleich zusätzlich eine ausschließlich leerraum-normalisierte Textprüfsumme führen.
5. Inhaltsversion und Originalstatus erfassen. Keine Gültigkeit aus Dateiname, Änderungsdatum oder Modellurteil ableiten.
6. Themenindex, Dokumentkarte und `katalog/manifest.json` ergänzen. Vorhandene Revisionen mit Anbieter-ID sichern, fehlende Revisionen als Lücke benennen.
7. Vergleiche und konkrete Konflikte mit Fundstellen ergänzen. Vorschläge bleiben von Quellen getrennt.
8. Integritätsprüfung ausführen und einen eigenen Branch mit nachvollziehbarer Änderung zur Prüfung bereitstellen.

## Bestehende Quelle korrigieren

Ein inhaltlich geänderter Text ist eine neue Fassung. Die frühere Fassung bleibt auffindbar. Jeder Vorschlag nennt alte und neue Fassung, Änderungsgrund, Auswirkungen und Status. Reine Katalogkorrekturen ändern keine Originaldateien.

Eine Korrektur fehlerhafter Extraktion ist ebenfalls zu protokollieren: ursprünglicher Extrakt, neuer Extrakt, Extraktionsverfahren und Prüfsummen. Die Originaldatei ist der Vergleichsbezug.

## Gültigkeit bestätigen

Bestätigung oder Ablösung wird in `entscheidungen/` als eigene Entscheidung festgehalten: betroffene Dokument-ID und Prüfsumme, vorheriger/nachheriger Status, Datum, Beleg, Begründung, Beziehungen zu anderen Fassungen und verbleibende Einwände. Eine Veröffentlichung oder ein Merge allein ist kein Ratifizierungsbeleg.

## Historie und Wiederherstellung

Normale Änderungen erfolgen additiv. Keine Force-Pushes, keine rückwirklich erfundene Entstehungsgeschichte, keine stillen Löschungen. Vor Löschungen oder irreversiblen Eingriffen ist Rücksprache erforderlich. Release-Tags erst auf einen geprüften Stand setzen; Quelloriginale, Metadaten und ein Git-Bundle separat sichern. Eine vollständige Wiederherstellung muss aus Git-Historie und den archivierten Quelldateien möglich sein.

## Regelmäßiger Pflegezyklus

Bei jedem Import: Manifest, Prüfsummen, Links und Konfliktregister aktualisieren. Vor einer inhaltlichen Veröffentlichung: offene Gültigkeitsfragen und Versionsbeziehungen prüfen. Bei einer neuen Quelle aus Drive: angebotene Revisionen erneut abfragen und Anbietergrenzen dokumentieren. Dieser Pflegeplan ist redaktionell; er führt keine NIDUS-Governance-Regel ein.

## Prüfung

```text
python scripts/verify_repository.py
```

Die Prüfung kontrolliert Dateien, Hashes, IDs und lokale Markdown-Links. Sie prüft keine gesellschaftliche Wirksamkeit, Rechtsgültigkeit oder technische Funktion der archivierten Konzepte. Archivierte Programme werden dabei nicht ausgeführt.
