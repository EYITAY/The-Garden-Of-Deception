# The Garden of Deception

A procedural botanical artwork where algorithmic behaviors become plant-growth rules.

Truth, uncertainty, refusal, contradiction, manipulation, deception, and strategy each produce distinct morphology.

## Reproduce

```bash
python -m pip install -r requirements.txt
python generate.py --seed 20260823
```

Outputs are written to `output/`.


## Setup

Create a virtual environment and install dependencies locally to the project.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the generator:
```bash
python generate.py --seed 20260823
```

Deactivate when finished:
```bash
deactivate
```

### Troubleshooting (macOS / PEP 668)

- If `python` is not found, use `python3`. After activating the virtual environment, `python` resolves to the venv’s Python 3 interpreter.
- If you see:
  ```
  error: externally-managed-environment
  ```
  your Homebrew-managed Python is enforcing PEP 668 and blocking system-wide installs. Use the virtual environment workflow above to install packages locally to the project.

Optional convenience outside a venv:
```bash
# Make `python` map to `python3` in zsh
echo 'alias python=python3' >> ~/.zshrc && source ~/.zshrc
```

Alternatives (not recommended vs. venv):
```bash
# Per-user site-packages
python3 -m pip install --user -r requirements.txt

# Override PEP 668 (riskier for system/Homebrew envs)
python3 -m pip install --break-system-packages -r requirements.txt
```
