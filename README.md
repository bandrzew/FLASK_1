### Jak włączyć venv na Windows ###

## Instrukcja konfiguracji środowiska Python z Flask na Windows

### 1. Sprawdzenie instalacji Python

Najpierw upewnij się, że masz zainstalowany Python:
```bash
python --version
```
lub
```bash
python3 --version
```
lub 

```bash
py --version
```

Jeśli Python nie jest zainstalowany, pobierz go z [python.org](https://www.python.org/downloads/).

### 2. Tworzenie środowiska wirtualnego (venv)

**Zalecenie:** Użyj Command Prompt zamiast PowerShell dla łatwiejszej konfiguracji.

#### Wybieranie powłoki w VS Code:
Jeśli używasz VS Code, możesz wybrać odpowiednią powłokę z menu terminalowego:

![Wybieranie powłoki w VS Code](https://code.visualstudio.com/assets/docs/terminal/getting-started/open-terminal.png)

Otwórz Command Prompt lub PowerShell i przejdź do katalogu projektu:
```bash
cd ścieżka\do\twojego\projektu
```

Utwórz nowe środowisko wirtualne:
```bash
python -m venv .venv
```

### 3. Aktywacja środowiska wirtualnego

**W Command Prompt:**
```bash
.venv\Scripts\activate
```

**W PowerShell:**
```bash
.venv\Scripts\Activate.ps1
```

** Mac / Linux **
```bash
source .venv/bin/activate 
```

**Uwaga:** Jeśli w PowerShell pojawi się błąd związany z polityką wykonywania, uruchom:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Po aktywacji w wierszu poleceń pojawi się `(.venv)` na początku linii.

### 4. Instalacja Flask

Po aktywacji środowiska zainstaluj Flask:
```bash
pip install Flask
```

Opcjonalnie możesz zainstalować dodatkowe pakiety:
```bash
pip install Flask-WTF Flask-Login Flask-SQLAlchemy
```

### 5. Sprawdzenie instalacji

Utwórz prosty plik testowy `test_flask.py`:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask działa poprawnie!'

if __name__ == '__main__':
    app.run(debug=True)
```

Uruchom aplikację:
```bash
python test_flask.py
```

Aplikacja powinna być dostępna pod adresem: http://127.0.0.1:5000

### 6. Deaktywacja środowiska

Aby wyłączyć środowisko wirtualne, wpisz:
```bash
deactivate
```

### 7. Zapisywanie zależności

Aby zapisać listę zainstalowanych pakietów:
```bash
pip freeze > requirements.txt
```

Aby zainstalować zależności z pliku requirements.txt:
```bash
pip install -r requirements.txt
```

### Wskazówki:
- Zawsze aktywuj środowisko wirtualne przed pracą z projektem Flask
- Pamiętaj o dodaniu folderu `.venv/` do `.gitignore`
- Regularnie aktualizuj plik `requirements.txt`

Command Prompt operacje:
```
cd folder        :: wejście do folderu
cd ..            :: folder wyżej
cd \             :: katalog główny
cd /d D:\projekty :: zmiana dysku + katalogu

dir              :: odpowiednik ls (lista plików)```
