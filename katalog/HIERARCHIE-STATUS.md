# Dokumenthierarchie und Gültigkeit

## Zwei Ebenen getrennt halten

Die redaktionelle Ordnung erklärt, wo ein Dokument zu finden ist. Die normative Hierarchie ist eine Aussage der jeweiligen NIDUS-Fassung. Ein Ordnername, ein Git-Commit oder eine KI-Zusammenfassung verleiht keinem Text Gültigkeit.

Als Lesereihenfolge dienen Gründung und Kerntexte → Charta/Constitution → Kodizes und Ausführungsordnungen → gesellschaftliche und technische Module → Analysen und historische Materialien. Diese Reihenfolge ersetzt keine inhaltliche Rangentscheidung zwischen kollidierenden Fassungen.

## Statuswerte des Katalogs

| Status | Bedeutung | Voraussetzung für Änderung |
|---|---|---|
| `entwurf` | Die Quelle nennt sich ausdrücklich Entwurf, auch wenn zugleich „Final“ erscheint | Ein nachgewiesener Beschluss zur konkreten Fassung |
| `gueltigkeit-unbestaetigt` | Kein ausreichender Beleg für aktuelle Gültigkeit | Dokumentierte Bestätigung mit Quellfassung und Datum |
| `historisch-als-ratifiziert-bezeichnet` | Der bestehende GitHub-Text nennt sich ratifiziert | Aktuelle Gültigkeit separat belegen |
| `gueltig-bestaetigt` | Für künftige Verwendung reserviert; kein Import automatisch so eingestuft | Beleg, Datum, betroffene Prüfsumme und Entscheidung |
| `abgeloest` | Für künftige bestätigte Ablösung reserviert | Expliziter Nachfolger und Ablösungsentscheidung |
| `zurueckgezogen` | Veröffentlichung oder Gültigkeit ausdrücklich zurückgezogen | Rücknahmegrund und Entscheidung; keine stille Löschung |

Die Originalstatuszeile steht separat in `declared_status`. Dadurch bleibt beispielsweise „Verbindliche Charta-Struktur“ lesbar, ohne dass der Import diese Selbstbezeichnung bestätigt.

## Versionsfamilien

- **Gründungsdokument / Manifest / Artikel-Fassung:** V1.0, V1.1, V1.2, mehrere V1.3-Fassungen, V1.4 und V1.5. Ein zusätzliches Manifest V2.0 ist eine eigene Quelle; sein Importdatum beweist keine Ablösung.
- **Constitution Layer:** mindestens V1.1 und V1.3.2 im geprüften Inhalt. Der Drive-Titel „V1“ ist kein zuverlässiger Inhaltsversionswert.
- **Ausführungsordnungen:** eigene Versionsnummern. Viele verweisen weiterhin ausdrücklich auf Constitution V1.1; sie werden nicht automatisch auf V1.3.2 umgedeutet.
- **DÜP:** frühe Teilfassungen, Gesamtfassung und Whitepaper V1.0. Ähnliche Bezeichnungen beweisen weder identischen Inhalt noch eine bestätigte Nachfolge.
- **Allianz der Wiege / Tafel-Konzepte:** konzeptuelle Vorläufer und gesellschaftliche Anwendungen; die Zuordnung erklärt die sachliche Beziehung und behauptet keine offizielle Trägerschaft externer Organisationen.

## Normative Verweise

Die Constitution beschreibt Grundrechte, Legitimation und Wächterfunktionen. Kodizes und Ordnungen nennen eigene Rechtsränge und Bezugsartikel. Der Import erhält diese Verweise wortgetreu. Bei widersprüchlichen Verweisen bleibt der Konflikt offen; insbesondere die verschiedenen Definitionen des unantastbaren Kerns und der Wächterkompetenzen erfordern eine ausdrückliche inhaltliche Entscheidung.

Urheberangaben werden als Quellenangaben übernommen. Sie begründen keine Führungs- oder Entscheidungsbefugnis. Redaktionell wird Patrick als Restorer bezeichnet; historische Bezeichnungen in Originaltexten werden nicht nachträglich umgeschrieben.
