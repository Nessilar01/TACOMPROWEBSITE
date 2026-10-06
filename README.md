# RAI Computer Programming Competition 2026 · Field clips

A single-page website: a rulebook index where every rule opens an animated clip on the real field photo, with English captions, voice narration and a live scoreboard.

- `index.html`: the finished site (self-contained, open it directly or host it with GitHub Pages)
- `src/`: page markup/CSS (`p1.html`) and the JavaScript parts (engine, clips, rule index)
- `assets/field.jpg`: the field photo used as the background
- `build.py`: rebuilds `index.html` from `src/` and `assets/`

Scoring values live in the `SCORE` table in `src/p2.js` .
