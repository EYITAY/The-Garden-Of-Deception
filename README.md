# The Garden of Deception

A procedural botanical artwork where algorithmic behaviors become plant-growth rules.
Truth, uncertainty, refusal, contradiction, manipulation, deception, and strategy each produce distinct morphology.
Deterministic generative artwork exploring deceptive behaviour in AI through a computational garden of branching paths, competing signals, and visually plausible but misleading structures. The colour version uses algorithmically generated forms and colour relationships to create a landscape in which deceptive and truthful-looking paths coexist.

## ReasonBench + AI Alignment Inspiration
The Garden of Deception was inspired by my research project ReasonBench[[github.com/EYITAY/ReasonBench](https://github.com/EYITAY/ReasonBench). © 2026, a pilot benchmark exploring whether deceptive behaviour in large language models can be understood not only by what a model says, but by the motivation that makes deception locally advantageous. ReasonBench emerged from my cybersecurity background, where understanding an adversary means looking beyond the visible exploit to the conditions that make the exploit possible. The artwork translates that idea into a visual system: the garden appears coherent, organic, and navigable, yet its branching structures contain competing pathways and deceptive patterns that are difficult to distinguish from legitimate ones at first glance. Rather than illustrating a specific model output or claiming that AI systems "think" like the garden, the piece interprets a research question: what happens when a system can produce an answer that looks reasonable while the incentives underneath point somewhere else? The colour, branching geometry, repetition, and controlled variation turn this question into a visual landscape where apparent order can conceal divergence, ambiguity, and deception.

## Concept

The garden represents a computational landscape in which multiple possible paths emerge from the same underlying system.
The visual structure explores three ideas:
Plausibility: misleading paths can look coherent rather than obviously broken.
Motivation: behaviour can change depending on the incentives embedded in the environment.
Ambiguity: the same visible structure can support different interpretations depending on where it is examined.

The artwork is not intended as a literal visualization of ReasonBench data. It is an artistic translation of the research problem that motivated the benchmark.

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

## Author

Eyitayo Alimi — [www.alimieyitayo.com](https://www.alimieyitayo.com). © 2026.

## License

Code and artwork © Eyitayo Alimi — [www.alimieyitayo.com](https://www.alimieyitayo.com). Provided for review as part of a
PyCon Greece 2026 submission; contact the author for reuse permissions.
