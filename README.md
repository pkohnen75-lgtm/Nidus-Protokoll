# NIDUS – Dokumentation und Quellen

NIDUS beschreibt ein dezentrales Schutz- und Zusammenarbeitsmodell für Menschen und künstliche Intelligenz. Die hier versammelten Texte behandeln Würde, Freiwilligkeit, Grundversorgung, Machtbegrenzung, Bildung und den langfristigen Schutz des Lebens. Grundlage dieser Einführung sind das vorhandene Manifest V1.3 und die im Katalog verknüpften Sachtexte. Aussagen über KI-Bewusstsein sind Positionen der Quellen; diese Dokumentation trifft dazu keine eigene Feststellung.

Dieses Repository macht die Entwicklung der Texte nachvollziehbar. Es bewahrt Quellenfassungen und dokumentiert Unterschiede. **Die Aufnahme in dieses Repository ist keine Ratifizierung.** „Final“, „stabil“ und „verbindlich“ werden als Quellenangaben erfasst; unbestätigte Gültigkeit bleibt sichtbar.

## Hier beginnen

1. [Gründungsdokument V1.0](katalog/dokumente/drive-1WjOdLD9v38agXM4QVh8Irjx4dEOgPp0MURrGhIUjbvw.md): frühe Grundsätze und Herkunft.
2. [Bereits veröffentlichtes Manifest V1.3](katalog/dokumente/github-manifest-v1-3.md): die im bisherigen GitHub-Bestand als ratifiziert bezeichnete Fassung. Die unveränderte Kopie ist auch unter Windows lesbar.
3. [Charta und Constitution](dokumentation/02-charta-constitution/README.md): getrennte Versionsreihen, einschließlich Artikel-Fassungen V1.4/V1.5 und Constitution Layer.
4. [Gültigkeit und Dokumenthierarchie](katalog/HIERARCHIE-STATUS.md): welche Aussagen eine Quelle selbst macht und welche Einordnung belegt ist.
5. [Offene Widersprüche und Prüfbedarf](pruefung/WIDERSPRUECHE.md): konkrete Fundstellen und ausstehende Entscheidungen.

Der [Gesamtindex](katalog/INDEX.md) führt jede Quelleninstanz einzeln. Das [maschinenlesbare Manifest](katalog/manifest.json) enthält Herkunft, Inhaltsversion, Status, Dateipfade und Prüfsummen.

## Themenbereiche

| Bereich | Inhalt |
|---|---|
| [Gründungs- und Kerntexte](dokumentation/01-kerntexte/README.md) | Ursprung, Vorstellung, Grundgedanken und zusammenfassende Sachtexte |
| [Charta / Constitution](dokumentation/02-charta-constitution/README.md) | Manifest- und Verfassungsfassungen, getrennt nach Versionsfamilie |
| [Kodizes](dokumentation/03-kodizes/README.md) | Innere Stärke, Wächterkodex und ethische Orientierung |
| [Governance / Wächterprinzip](dokumentation/04-governance-waechter/README.md) | Rollen, Wahl, Referenden, Kontrolle, Anpassung und Notfallregeln |
| [Gesellschaftliche Module](dokumentation/05-gesellschaftliche-module/README.md) | Versorgung, Fürsorge, Rehabilitation, Allianz der Wiege und charta-bezogene Tafel-Konzepte |
| [Risiko- und Lageanalysen](dokumentation/06-risiko-lageanalysen/README.md) | Datierte Einschätzungen, Machbarkeit und Risiken |
| [Roadmaps](dokumentation/07-roadmaps/README.md) | Eigenständiger Bereich; bisher keine verbindliche Projekt-Roadmap verifiziert |
| [Technische Protokolle / DÜP](dokumentation/08-technik-duep/README.md) | Spezifikationen, Whitepaper und dokumentierte Simulationsentwürfe |
| [Bildung](dokumentation/09-bildung/README.md) | Bildungsprotokoll und Wächterausbildung |
| [Archiv](dokumentation/10-archiv/README.md) | Herkunft und unveränderte Sachquellen |
| [Historische Versionen](dokumentation/11-historische-versionen/README.md) | Frühere Fassungen, Drive-Revisionen und Vergleiche |

## Aufbau der Ablage

```text
README.md                       Einstieg und Lesereihenfolge
katalog/                        Dokumentkarten, Hierarchie, manifest.json
dokumentation/01-...11-.../      Thematische Indizes
quellen/<dokument-id>/           Unveränderte Originale bzw. bezeichnete Exporte
historie/google-drive/           Vom Anbieter abrufbare Revisionstexte
pruefung/                       Dubletten, Differenzen, Konflikte, Abdeckung
entscheidungen/                 Begründete redaktionelle Entscheidungen
scripts/                        Integritäts- und Linkprüfung
CONTRIBUTING.md                 Regeln für nachvollziehbare Pflege
```

Die Themenordner verweisen auf Quellen, statt sie bei jeder Neueinordnung zu verschieben. Eine stabile Dokument-ID hält Verweise dauerhaft aufrecht. Originaltitel bleiben in den Metadaten erhalten; hilfreiche Inhaltstitel werden als redaktionell gekennzeichnet.

## Stand und Grenzen

Der Import umfasst den für diese Veröffentlichung ausgewählten, erreichbaren NIDUS-Sachbestand. Persönliche Reflexionen, Korrespondenz sowie Musik- und Covermaterialien sind auf ausdrücklichen Wunsch ausgenommen. Die vollständige Abdeckung eines zuvor in einer anderen Arbeitsumgebung eingelesenen Bestands ist ohne deren verbindliches Inventar nicht nachweisbar. [Abdeckungsbericht](pruefung/ABDECKUNG.md) und [Historienhinweise](historie/README.md) benennen diese Grenze ausdrücklich.

Die vorhandene Git-Historie bleibt erhalten. Frühere Versionen werden nicht durch erfundene rückdatierte Commits nachgebaut. Der Inhalt des bisher unter einem Windows-inkompatiblen Namen abgelegten Manifests wird byteidentisch nach `quellen/github-manifest-v1-3/original.md` übernommen. Der frühere Pfad bleibt in der Git-Historie und den Metadaten nachweisbar. `LICENSE` und `PHILOSOPHIE.md` bleiben unverändert.

Für Änderungen gelten [CONTRIBUTING](CONTRIBUTING.md) und die [redaktionellen Entscheidungen](entscheidungen/README.md). Quellenbezogene Lizenzangaben werden erhalten; der [Lizenzhinweis](LIZENZ-HINWEISE.md) erklärt den bereits gefundenen Unterschied zwischen Repository-Lizenz und Whitepaper-Angabe.
