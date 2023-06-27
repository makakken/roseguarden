---
title: Installation
---

# Setup Roseguarden-Server

Es gibt mehrere Wege den Roseguarden-Server zum laufen zu bekommen:

## 1. Docker for Development (empfohlen)

Das Github-Repository kommt mit einer docker-compose.yml. Ist Docker Desktop und Docker-Compose installiert, kann Roseguarden einfach mit den folgenden Befehlen ausgeführt werden:

- Führe im Roseguarden Verzeichniss folgenden Befehel aus: `docker-compose up -d`
- Stelle sicher dass in frontend/nuxt.config.js folgenden Einträge gesetzt sind:

```
proxy: {
    '/api/v1/log': {
      target: 'http://backend:5000',
      ws: true,
      secure: true,
      changeOrigin: true
    },
    '/api/v1': {
      target: 'http://backend:5000',
      ws: true,
      secure: false,
      changeOrigin: true
    },
  },
```

- Um die Benutzeroberfläche aufzurufen kannst du in deinem Webbrowser nun die Seite unter http://localhost:3000 aufrufen.
- Solltest du direkte API-Aufrufe testen möchten, kannst du das Backend unter localhost:8002 erreichen

:boom: **Note:** Docker-Compose startet einen Frontend build mit `npm install` in ein Docker-Volume. Solltest du irgendwelche Änderungen an der package.json durchführen, musst du den frontend-Container erneut erstellen.

## 2. Release Packages

- Downloade und entpacke `roseguarden-X.Y.Z` [here](https://gitlab.com/roseguarden/roseguarden/-/releases)
- Geh in den entpackten Ordner und führe folgende Befehle aus:
  - Alle Abhängigkeiten installieren mit `pip3 -r requirements.txt`
  - Erstelle eine `config.ini` entsprechend deiner gewünschten Einstellungen (siehe `config.template`)
  - Führe 'flask run' aus

## 3. Github-Repository auschecken

- Git-Clone https://gitlab.com/roseguarden/roseguarden
- Wirf einen Blick in den `backend` und `frontend` Ordner, um herauszufinden wie du deine Entwicklungsumgebung gestartet bekommst. Siehe 3.1 für Hinweise, wie du das Backend installiert bekommst.
- Um das `backend` oder `frontend` zu starten führe folgende Kommandos aus:
  - Starte das Backend mit `flask run` nachdem du in den `backend` Ordner gewechselt hast
  - Starte das Frontend mit `npm run dev` nachdem du in den `frontend` Ordner gewechselt hast

:boom: **Note:** Alternativ kannst du das `script/pack.py`-Script nutzen um dir ein eigenes Paket zu bauen und es mit einem HTTP-Server zu hosten.

### 3.1. Das Backend installieren nach Clone aus dem Github-Repository

- `cd backend`
- `python3 -m venv .venv`
- `. venv/bin/activate`
- (venv) `pip install Flask`
- (venv) `pip install -r requirements.txt`
- (venv) `run flask`
