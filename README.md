# Binary Eater // Cyber Edition 🎮

A cyberpunk-themed Pac-Man style game built with vanilla JavaScript and hosted on Streamlit.

![Game Preview](https://img.shields.io/badge/Game-Cyberpunk%20Pac--Man-ff00ff?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-Streamlit-00ffff?style=for-the-badge)

## 🎯 Features

- **Cyberpunk Aesthetic**: Neon colors, glowing effects, scanlines, and animated backgrounds
- **4 Ghost AI Entities**: Each with chase and scatter behaviors
- **Progressive Difficulty**: Game speeds up with each level
- **Power-Up System**: Eat power pellets to scare and consume ghosts
- **Combo Scoring**: Chain ghost kills for massive point multipliers (200→400→800→1600)
- **High Score Persistence**: Saves to localStorage
- **Sound Effects**: Retro-style synth sounds using Tone.js
- **Background Music**: Festive cyber-jingle loop
- **Mobile Support**: Touch controls for mobile devices
- **Responsive Design**: Works on various screen sizes

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Create a GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/binary-eater.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Set the main file path to `app.py`
   - Click "Deploy"

### Option 2: Local Development

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**
   ```bash
   streamlit run app.py
   ```

3. **Open in Browser**
   - Navigate to `http://localhost:8501`

### Option 3: Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t binary-eater .
docker run -p 8501:8501 binary-eater
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `W` / `↑` | Move Up |
| `A` / `←` | Move Left |
| `S` / `↓` | Move Down |
| `D` / `→` | Move Right |

**Mobile**: Use the on-screen touch controls

## 📊 Scoring

| Item | Points |
|------|--------|
| Binary Pellet (0/1) | 10 |
| Power Pellet | 50 |
| Ghost (1st in combo) | 200 |
| Ghost (2nd in combo) | 400 |
| Ghost (3rd in combo) | 800 |
| Ghost (4th in combo) | 1600 |

## 🛠 Project Structure

```
binary-eater/
├── app.py              # Streamlit application
├── game.html           # The game itself (vanilla JS)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎨 Game Improvements Over Original

1. **Visual Enhancements**
   - Animated gradient border on game container
   - Pulsing power pellets with inner glow
   - Ghost eyes that track Pac-Man's position
   - Wavy ghost animation
   - Floating ambient particles
   - Smoother wall edge glow effects
   - Better color palette with CSS variables

2. **Gameplay Improvements**
   - 4 ghosts instead of 3
   - Smarter ghost AI (chase vs scatter modes)
   - Ghost combo scoring system
   - Level progression with increasing speed
   - High score persistence
   - Brief invincibility after death
   - Power pellets in all 4 corners

3. **Audio Improvements**
   - Variable pellet eating sounds
   - Unique ghost eating sounds with pitch variation
   - Win level fanfare
   - Volume balancing

4. **UX Improvements**
   - Pac-Man icon lives display
   - Power mode indicator
   - Score padding for consistent display
   - Better overlay transitions
   - Touch controls for mobile
   - Keyboard shortcuts to start game

## 📜 License

MIT License - feel free to modify and redistribute!

---

Made with 💜 and lots of neon
