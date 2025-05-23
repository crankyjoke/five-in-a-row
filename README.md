
# Five‑in‑a‑Row (Gomoku)

**Five‑in‑a‑Row** is a lightweight Python implementation of Gomoku (also known as Omok or Gobang) featuring:

* **Two game modes** – _Single‑player_ (human vs **AI**) and _Two‑player_ (human vs human)  
* **Minimax AI with α‑β pruning** – configurable search depth for difficulty tuningciteturn8view0  
* **Tkinter GUI** – simple drag‑free interface; no external dependencies besides the Python standard libraryciteturn9view0  
* **Configurable board** – defaults to **8 × 8**, but you can change the size in code in secondsciteturn8view0  

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/crankyjoke/five-in-a-row.git
cd five-in-a-row

# (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Launch the game
python main.py
```

When the **Mode Selection** window appears:

1. Choose **Single Player** to face the built‑in AI or **Two Players** for hot‑seat.  
2. Adjust **Step Depth** (0–2 recommended). Bigger numbers make the AI stronger but slower.  
3. Click **Start Game**.

![Screenshot](docs/screenshot.png) <!-- _Add your own screenshot if desired_ -->

---

## Controls

| Action | How |
|--------|-----|
| Place a mark | **Left‑click** a square |
| Restart game | Click _Play Again_ in the pop‑up after a win/draw |
| Quit         | Close the window |

---

## File Overview

| File | Purpose |
|------|---------|
| `game_logic.py` | Core rules, board evaluation, and Minimax search |
| `ui.py` | Tkinter UI layer, mode selector, and event callbacks |
| `main.py` | Tiny bootstrap that launches the mode‑selection UIciteturn10view0 |

---

## Customisation

* **Board size** – open `game_logic.py` and change `board_size` in `__init__`.  
* **AI strength** – default `step_depth=1`; increase in the Mode Selection screen or hard‑code a different default.  
* **GUI scaling** – each cell’s width/height is calculated from the board size; tweak in `ui.py`.

---

## Dependencies

* **Python 3.9+** (earlier 3.x likely works)  
* **Tkinter** – already bundled with the official Python distributions.  
  *Linux users*: install `python3-tk` via your package manager if the import fails.

No third‑party packages required!

---

## License

Released under the **MIT License** – see [`LICENSE`](LICENSE) for details.
