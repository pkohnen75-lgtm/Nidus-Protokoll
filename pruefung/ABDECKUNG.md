# Abdeckung des Imports vom 9. September 2026

## Gesicherter Umfang

| Bestand | Quelleninstanzen / Darstellungen |
|---|---:|
| Google Drive, ausgewählte NIDUS-Sachdokumente | 46 |
| Lokale Sachdateien, einschließlich Handybackup | 55 |
| Bereits veröffentlichte GitHub-Sachtexte | 2 |
| Summe der katalogisierten Quelleninstanzen | 103 |
| Native Google-Docs-Strukturen, jeweils ein Tab | 44 |
| Vom Anbieter angebotene und abgerufene Drive-Revisionen | 69 |
| Lokale byteidentische Originalkopien | 55 |
| Byteidentische Kopien der bestehenden GitHub-Sachtexte | 2 |

Quelleninstanzen sind keine Zahl einzigartiger Werke. Separate Dateien, Exportformate und Dubletten werden absichtlich einzeln erfasst. Das [Manifest](../katalog/manifest.json) ist die vollständige Aufzählung dieses Imports.

## Such- und Auswahlverfahren

Google Drive wurde mit `NIDUS` sowie einer erweiterten Suche nach Nidus, Wächter, Charta und DÜP durchsucht. Die erweiterte Suche wurde bis zum Ende der angebotenen Folgeseiten abgearbeitet. Insgesamt wurden 128 unterschiedliche Dokumentkandidaten inhaltlich gesichtet. Aufgenommen wurden 46 sachlich zugehörige Quellen, darunter auch sachliche Vorläufer unter „Allianz der Wiege“ und ausdrücklich charta-bezogene gesellschaftliche Konzepte. Die bloße Erwähnung eines Suchworts führte nicht zur Veröffentlichung.

Die lokale Suche erfasste die Dokumente im Quellordner `Nidus-Verbund/dokumente`, die NIDUS-Dokumente im Wurzelordner und die NIDUS-Dateien im Handybackup `HANDYBACKUP/070926`. Persönliche und künstlerische Materialien sowie gemischte Zusammenfassungen mit persönlichen Passagen wurden nicht aufgenommen. Allgemeine fremde oder thematisch angrenzende Handbücher sind kein Beleg einer NIDUS-Nachfolge und wurden nicht pauschal importiert.

Das bestehende GitHub-Repository wurde einschließlich seiner drei erreichbaren Vorgänger-Commits eingelesen. Deren Inhalte und Herkunft bleiben erhalten.

## Verifikation

- Alle 55 lokalen Originaldateien wurden kopiert und anschließend gegen die erreichbare Quelle per SHA-256 verglichen: keine Abweichung.
- Für 44 native Google Docs wurden die strukturierten Inhalte mit den Textextrakten verglichen. Die gefundenen Unterschiede bestehen aus von der Exportdarstellung ergänzten Listenzeichen, Nummerierungen, Trennlinien und Leerraum. Quelltext und native Struktur sind getrennt erhalten.
- Alle 69 angebotenen Revisionen wurden als Text abgerufen, einschließlich leerer Anfangs- und Endstände.
- Bei einer aktuell leeren Constitution-Datei wurde die frühere V1.1 aus Revision 2 gesichert. Die zweite leere Notfall-Datei lieferte auch in ihren angebotenen Revisionen keinen Sachtext.
- Die lokale PDF-Fassung „Vorstellung in Ultra Leichter Sprache“ ist als Originaldatei gesichert. Die beiden Drive-PDFs liegen zusätzlich als Textextrakte und Revisionstexte vor. Gleiche Dateigröße und gleicher Text belegen keine Byteidentität der Drive-PDFs mit der lokalen Datei.
- Die Repository-Prüfung kontrolliert manifestierte Dateien, Prüfsummen, Dokument-IDs und redaktionelle lokale Links. Sie führt archivierten Quellcode nicht aus.

## Verbleibende Grenzen

1. **Früherer Work-Bestand:** Ein verbindliches Inventar des in einer anderen Arbeitsumgebung zuvor eingelesenen Bestands lag nicht vor. Dieser Import rekonstruiert den aktuell erreichbaren Sachbestand; er behauptet keine bewiesene Übereinstimmung mit jenem früheren Inventar.
2. **Nicht angebotene Revisionen:** Drive zeigt teilweise Sprünge zwischen Revisions-IDs. Nicht gelieferte Zwischenstände sind nicht wiederhergestellt. Die 69 gesicherten Revisionen sind alle angebotenen, nicht nachweislich alle je vorhandenen Bearbeitungsstände.
3. **Native Medien und Kommentare:** Google-Docs-Struktur und Texte sind gesichert. Eingebettete Medienbytes, externe verknüpfte Ressourcen, Kommentare und Vorschlagsverläufe sind kein vollständig exportiertes Dokumentarchiv. Die zwei Drive-PDF-Binärdateien wurden nicht als separat verifizierte Remote-Originale in das Dateipaket materialisiert.
4. **Archive mit gemischtem Inhalt:** ZIP-/Gesprächsexporte wurden nicht als Ganzes veröffentlicht. Das würde die ausdrücklich ausgeschlossenen persönlichen Materialien einschließen. Aus solchen Archiven möglicherweise zusätzlich rekonstruierbare Sachfassungen sind eine offene Abdeckungslücke.
5. **Gültigkeit:** Kein Importstatus ersetzt eine Ratifizierung. Datierte Analysen wurden nicht als aktuelle Tatsachenprüfung behandelt. Quellmarker und technische Zusicherungen bleiben entsprechend gekennzeichnet.
6. **Roadmap:** Eine eigenständige, verbindliche Projekt-Roadmap wurde nicht verifiziert. Der Bereich ist angelegt und benennt diese Lücke.

Die Sammlung erfüllt die nachvollziehbare Ablage des hier geprüften Bestands. Eine Behauptung lückenloser Vollständigkeit seit Entstehung von NIDUS wäre anhand dieser Quellen nicht gerechtfertigt.
