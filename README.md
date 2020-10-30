# Projekt Aufgaben

In diesem Projekt "Mapping the weather" lernen wir, wie man Daten aus der Raspberry Pi Weather Station-Datenbank abruft und diese Daten auf einer grafischen Karte zeichnet, indem man die folgenden Funktionen ausführt:
* Daten mit einer RESTful-API abrufen
* Erstellen Sie eine Vielzahl von Karten mit der Python-Folium-Bibliothek
* Zeichnen Sie Datenpunkte auf einer Karte

# Schritte 1: Daten von Wetterstationen holen
Zunächst verwenden wir "thrinket" von Thonny, um Python zu schreiben. Einige von uns haben auch Pycharm benutzt.  

Dann installieren wir Folium Request, importieren *get*, *json*, *foilum*, *os*, *webbrowser* und *html*.

Hier wird die Anforderung verwendet, um JSON-Daten aus der Datenbank abzurufen. *JSON* ist zur Verarbeitung von JSON-Daten bedient. *Folium* ist ein Tool zur Visualisierung von Daten auf Karten in Python.

Verwenden wir die URL mit der verfügbaren API, um JSON-Daten abzurufen:
```stations=get(url).json()```

Endlich in der Shell werden wir sehen:
```{'weather_stn_id': 255541, 'weather_stn_name': 'Pi Towers Demo', 'weather_stn_lat': 52.213842, 'weather_stn_long': 0.110421}```

Zusätzlich, haben wir auch alle Wetterstationsnamen laufen lassen:

```lons = [station['weather_stn_long'] for station in stations['items']] ```

```lats = [station['weather_stn_lat'] for station in stations['items']]```

```wsnames = [html.escape(station['weather_stn_name']) for station in``` ```stations['items']] ```

```print(wsnames) ```

# Schritte 2:  Erstellen einer Karte und Plotten von Stationen
Wir setzen Lörrach (47 N, 7 E) als das Mittelpunkt in der Karte.

Die folgende Anweisung zum Hinzufügen des Standorts in allen Wetterstationen zeigt:

```for n in range(len(lons)):```
   ```folium.Marker([lats[n],```
                ```lons[n]]，```
                ```popup = wsnames[n]).add_to(map_ws) ```
                
Außerdem können wir auch die Farbe und den Stil von Markern ändern:

```icon = folium.Icon(icon = "cloud", color = "green")```

Gut ist, dass das Projekt zum Beispiel automatisch von pycharm in der lokalen Datei gespeichert wird:
```CWD=Users/melissa/PycharmProjects/pythonProject2```

Daher können wir endlich einfach Map-Dateien speichern und archivieren:

```webbrowser.open_new("file://"+CWD+"/"+"wsmap1.html") ```




