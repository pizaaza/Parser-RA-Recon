# Installation & Troubleshooting Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git
- Terminal/Command Prompt access

### Check Python Version

**Windows**:
```powershell
python --version
```

**Linux/macOS**:
```bash
python3 --version
```

You should see `Python 3.9.x` or higher.

---

## Step-by-Step Installation

### Windows (PowerShell)

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/pizaaza/Parser-RA-Recon.git
   cd Parser-RA-Recon
   ```

2. **Create virtual environment**:
   ```powershell
   python -m venv .venv
   ```

3. **Activate virtual environment**:
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   (If you get an execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)

4. **Install dependencies**:
   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Run the app**:
   ```powershell
   python app.py
   ```

### Windows (Command Prompt)

1-2. Same as PowerShell

3. **Activate virtual environment**:
   ```cmd
   .venv\Scripts\activate.bat
   ```

4-5. Same as PowerShell

### Linux / macOS

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pizaaza/Parser-RA-Recon.git
   cd Parser-RA-Recon
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate virtual environment**:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Run the app**:
   ```bash
   python app.py
   ```

---

## Common Issues & Solutions

### Issue 1: "Python is not recognized as an internal or external command"

**Cause**: Python is not in your PATH.

**Solution**:

1. Reinstall Python from https://www.python.org/
2. **Check "Add Python to PATH"** during installation
3. Restart your terminal/PowerShell
4. Verify: `python --version`

### Issue 2: "No module named 'rich'" or "No module named 'requests'"

**Cause**: Dependencies not installed.

**Solution**:

1. Make sure your virtual environment is activated
2. Run: `pip install -r requirements.txt`
3. Verify: `pip list`

You should see:
- `requests` (2.31.0+)
- `rich` (13.7.0+)

### Issue 3: "Permission denied" on Linux/macOS

**Cause**: The app.py file lacks execute permissions.

**Solution**:

```bash
chmod +x app.py
python app.py  # Still use python, don't do ./app.py
```

### Issue 4: Virtual environment won't activate on Windows

**Cause**: PowerShell execution policy blocks scripts.

**Solution**:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activation again:
.venv\Scripts\Activate.ps1
```

Or use Command Prompt instead:
```cmd
.venv\Scripts\activate.bat
```

### Issue 5: "ModuleNotFoundError: No module named 'parser_ra_recon'"

**Cause**: Not running from the project root directory.

**Solution**:

1. Confirm you're in the `Parser-RA-Recon` directory
2. Check with: `ls` (Linux/macOS) or `dir` (Windows)
3. You should see `app.py`, `requirements.txt`, `parser_ra_recon/` folder
4. Then run: `python app.py`

### Issue 6: "Requests/Rich won't install"

**Cause**: pip version is old, or network issues.

**Solution**:

1. Upgrade pip:
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

2. Clear pip cache:
   ```bash
   pip cache purge
   ```

3. Try installing again:
   ```bash
   pip install -r requirements.txt
   ```

If still failing, install packages individually:

```bash
pip install requests==2.31.0
pip install rich==13.7.0
```

### Issue 7: Terminal output looks garbled or colors don't show

**Cause**: Terminal doesn't support ANSI colors.

**Solution**:

- **Windows**: Use Windows Terminal (free from Microsoft Store) instead of old Command Prompt
- **Linux/macOS**: Use a modern terminal (iTerm2, GNOME Terminal, etc.)
- **Fallback**: Disable colors in `rich` by modifying `parser_ra_recon/logging_utils.py`

### Issue 8: "Connection refused" or "Timeout" errors when scanning

**Cause**: Network connectivity issues or services being rate-limited.

**Solution**:

1. Check your internet connection
2. Try again later (some services have daily limits)
3. Increase request delays in `parser_ra_recon/config.py`:
   ```python
   min_delay: float = 3.0
   max_delay: float = 8.0
   ```

### Issue 9: Reports folder doesn't exist or can't create files

**Cause**: Permissions issue or path is invalid.

**Solution**:

1. Create the folder manually:
   ```bash
   mkdir reports  # Linux/macOS
   mkdir reports  # Windows (PowerShell or CMD)
   ```

2. Or change export path in `parser_ra_recon/config.py`:
   ```python
   export_dir: str = "./local_reports"  # Relative path
   ```

### Issue 10: "UnicodeDecodeError" when reading/writing files

**Cause**: Character encoding issue (especially on Windows).

**Solution**:

1. Use UTF-8 encoding explicitly
2. Or change the default encoding in `parser_ra_recon/modules/reporting.py`:
   ```python
   with open(filepath, "w", encoding="utf-8") as f:
   ```

---

## Verification Checklist

After installation, verify everything works:

- [ ] Virtual environment is activated
- [ ] `pip list` shows `requests` and `rich`
- [ ] `python --version` shows 3.9+
- [ ] Running `python app.py` shows the banner and menu
- [ ] You can navigate the TUI without errors
- [ ] Reports folder is created on first export

---

## Getting Help

If you encounter issues:

1. Check this troubleshooting guide
2. Review the error message carefully (scroll up in terminal if needed)
3. Search for the error message online
4. Check GitHub Issues (if applicable)
5. Verify all prerequisites are installed

---

For more information, see [README.md](README.md) and [QUICKSTART.md](QUICKSTART.md)
