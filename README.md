# cli_photo_rename
A simple CLI tool for renaming photos based on their EXIF data or file creation/modification metadata. 

## History (Unfortunately up to this point this is in german)

Alle Files, deren Name nicht mit "done" beginnt werden umbenannt. Der neue Name besteht aus: done_$Erstelldatum_$Uhrzeit_$lfdNr_00".

Damit kann man aus mehreren Kameras (iPhone, Lumix etc) die Files im Verzeichnis zusammenkopieren und mit main.py alle in eine chronologischen Reihenfolge bringen.

Files die man dann manuell durch Dateinamen-Umbenennung umsortiert haben bleiben von main.py unberührt (solange sie mit "done" beginnen). Das File main.py selbst ist auch von der Umbennung ausgeschlossen.

WICHTIG: main.py muss in dem Arbeitsverzeichnis liegen. Den Pfad muss man dennoch angeben in der Befehlszeile...
WICHTIG: im Terminal muss man sich aktuell auch im Arbeitsverzeichnis befinden

```python3 main.py "/path/to/folder"```

2021 08 04
Exifread hat gefehlt. Install der Lib mit:
pip3 install exifread
