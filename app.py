"""
BINARY EATER // CYBER EDITION
A Cyberpunk Pac-Man style game hosted on Streamlit
"""

import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Binary Eater // Cyber Edition",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better presentation
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dark theme for the whole page */
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #0d1117 50%, #0a0a0f 100%);
    }
    
    /* Center the game iframe */
    .game-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    
    /* Style the iframe */
    iframe {
        border: 3px solid #00ffff;
        border-radius: 12px;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.3),
                    0 0 60px rgba(255, 0, 255, 0.2);
    }
    
    /* Title styling */
    .cyber-title {
        font-family: 'Courier New', monospace;
        text-align: center;
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff;
        margin-bottom: 20px;
    }
    
    /* Instructions panel */
    .instructions {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #ff00ff;
        border-radius: 8px;
        padding: 20px;
        margin: 20px auto;
        max-width: 600px;
        color: #00ff00;
        font-family: monospace;
    }
    
    .instructions h3 {
        color: #ff00ff;
        text-shadow: 0 0 5px #ff00ff;
    }
    
    .instructions ul {
        list-style-type: none;
        padding-left: 0;
    }
    
    .instructions li {
        padding: 5px 0;
    }
    
    .instructions li::before {
        content: "► ";
        color: #00ffff;
    }
    
    /* Key styling */
    .key {
        display: inline-block;
        background: #1a1a2e;
        border: 1px solid #00ffff;
        border-radius: 4px;
        padding: 2px 8px;
        margin: 0 2px;
        font-family: monospace;
        color: #00ffff;
    }
</style>
""", unsafe_allow_html=True)

def load_game_html():
    """Load the game HTML file"""
    game_path = Path(__file__).parent / "game.html"
    if game_path.exists():
        return game_path.read_text(encoding='utf-8')
    else:
        st.error("Game file not found!")
        return None

def main():
    # Load and display the game
    game_html = load_game_html()
    
    if game_html:
        # Create a container for the game
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Embed the game using components.html
        st.components.v1.html(game_html, height=700, scrolling=False)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Instructions section
        st.markdown("""
        <div class="instructions">
            <h3>// SYSTEM CONTROLS</h3>
            <ul>
                <li><span class="key">W</span> <span class="key">A</span> <span class="key">S</span> <span class="key">D</span> or <span class="key">↑</span> <span class="key">←</span> <span class="key">↓</span> <span class="key">→</span> — Navigate the maze</li>
                <li>Consume all binary data (0s and 1s) to clear the level</li>
                <li>Avoid rogue AI entities (ghosts) or they'll terminate your process</li>
                <li>Grab power pellets (magenta orbs) to temporarily scare ghosts</li>
                <li>Eat scared ghosts for bonus points (combo multiplier active!)</li>
            </ul>
            <h3>// SCORING MATRIX</h3>
            <ul>
                <li>Binary pellet: <span style="color: #00ff00">+10 pts</span></li>
                <li>Power pellet: <span style="color: #ff00ff">+50 pts</span></li>
                <li>Ghost (1st): <span style="color: #ffcc00">+200 pts</span></li>
                <li>Ghost (2nd): <span style="color: #ffcc00">+400 pts</span></li>
                <li>Ghost (3rd): <span style="color: #ffcc00">+800 pts</span></li>
                <li>Ghost (4th): <span style="color: #ffcc00">+1600 pts</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
        <div style="text-align: center; color: #444; font-family: monospace; margin-top: 30px; font-size: 12px;">
            BINARY EATER v2.0 // CYBER EDITION<br>
            Press any movement key or click INITIALIZE to start
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
