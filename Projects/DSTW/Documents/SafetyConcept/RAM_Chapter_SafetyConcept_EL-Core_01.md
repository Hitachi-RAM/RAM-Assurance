# RAM_Chapter_SafetyConcept_EL-Core_01

Die gelb markierten DIL-Texte im [Safety Concept ELEKTRA Core](./SafetyConcept_ELEKTRA_Core_3BU_17300_XXXX_DUAPC_Ed01_Pd01.docx) würde ich **vollständig durch die folgende subsystembezogene Fassung ersetzen**. ECMUX, IFC und OC werden dabei nur als angebundene Subsysteme betrachtet, nicht hinsichtlich ihrer eigenen Redundanz beschrieben.

## 3.4 Zuverlässigkeitskonzept

Die Zuverlässigkeit und Verfügbarkeit des Subsystems ELEKTRA Core werden durch die redundante Ausführung seiner Anwendungen, die Überwachung ihrer Funktion und Kommunikation sowie definierte Wiederherstellungsmechanismen unterstützt.

- **Redundanz:** Die Anwendungen CC, RCU und DGP werden auf der redundanten TAS-Plattform im Hot-Hot-Betrieb ausgeführt. Die Basisvariante verwendet eine 2x2oo2-Architektur; für die georedundante Variante ist eine 4x2oo2-Architektur vorgesehen. Die beiden diversitären Softwarekanäle dienen der sicheren Verarbeitung und Fehlererkennung. Die zusätzlichen redundanten Einheiten ermöglichen die Fortführung der Betriebsfunktion bei den durch die Architektur abgedeckten Ausfällen.
- **Fehlererkennung und Diagnose:** Die Vergleichs-, Lebenstakt- und Reaktivitätsüberwachungen unterstützen die Erkennung von Fehlern und Kommunikationsstörungen. Erkannte Fehler und der Verlust von Redundanz sind über die vorgesehenen Diagnosefunktionen zu melden. Ausfälle der Diagnosekomponente DGP sind hinsichtlich ihrer Auswirkungen auf Fehlererkennung, Störungsanalyse und Wiederherstellung zu bewerten.
- **Wiederherstellung:** Die Übernahme durch verbleibende Einheiten sowie Neustart, Zustandssynchronisation und Reintegration ausgefallener Einheiten erfolgen unter Beibehaltung der erforderlichen Daten- und Anwendungskonsistenz. Die Wiederherstellung der Betriebsfunktion und die Wiederherstellung der vollständigen Redundanz sind getrennt zu betrachten. Für den zwischenzeitlichen Betrieb mit reduzierter Redundanz sind die zulässigen Bedingungen und Wiederherstellungszeiten festzulegen.

Die Redundanzwirkung setzt eine geeignete Verteilung der Anwendungen auf physische Server und Verfügbarkeitszonen sowie ausreichende Ressourcen nach einem Ausfall voraus. Abhängigkeiten von IPS, Kommunikationsnetzen und weiteren erforderlichen Plattformdiensten sind ebenso zu berücksichtigen wie gemeinsame Software-, Konfigurations- und Wartungsfehler. Die Auswirkungen von Neustarts und Aktualisierungen auf CC, RCU und DGP sowie auf die angebundenen Schnittstellen sind zu bewerten.

Für die georedundante Variante ist das Verhalten bei Standortausfall, Netzpartition und Reintegration festzulegen und nachzuweisen. Dabei sind eine eindeutige Master-Auswahl und die Vermeidung konkurrierender aktiver Instanzen sicherzustellen. Eine unterbrechungsfreie Betriebsfortführung gilt nur für die nachgewiesenen Fehlerfälle und Randbedingungen.

Die dem ELEKTRA Core zugeordneten RAM-Anforderungen und die zugehörige Nachweisführung werden im Rahmen der RAM-Planung und RAM-Analysen des VIL behandelt. Der Beitrag des ELEKTRA Core zur VIL-Verfügbarkeit ist unter Berücksichtigung seiner Schnittstellen und Infrastrukturabhängigkeiten zu bewerten. Die Wirksamkeit der Redundanz- und Wiederherstellungsmechanismen ist durch Analysen und geeignete Fehlerfalltests nachzuweisen. Ein sicherheitsgerichteter Ausfall kann dabei weiterhin eine betriebliche Nichtverfügbarkeit verursachen.

---

**Abgrenzung:** Der Vorschlag übernimmt keine VIL- oder DIL-CU-Verfügbarkeitskennzahl als eigenständiges Core-Ziel und setzt keine noch nicht freigegebene Recovery-Zeit voraus.

## Applied Skills

Document Review, Railway-RAM, REQ-Review und RAM-Metrics.
