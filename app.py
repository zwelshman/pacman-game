"""
BINARY EATER // CHRISTMAS CYBER EDITION
A Christmas-themed Cyberpunk Pac-Man style game hosted on Streamlit
"""

import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="🎄 Binary Eater // Christmas Edition",
    page_icon="🎅",
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
    
    /* Dark Christmas theme */
    .stApp {
        background: linear-gradient(180deg, #0a1628 0%, #1a0a28 50%, #0d1a0d 100%);
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
        border: 4px solid;
        border-image: linear-gradient(45deg, #ff0040, #00ff40, #ffd700, #ff0040) 1;
        border-radius: 12px;
        box-shadow: 0 0 40px rgba(255, 0, 64, 0.3), 0 0 80px rgba(0, 255, 64, 0.2);
    }
    
    /* Instructions panel - Christmas themed */
    .instructions {
        background: linear-gradient(180deg, rgba(13, 26, 13, 0.9) 0%, rgba(26, 10, 10, 0.9) 100%);
        border: 2px solid;
        border-image: linear-gradient(45deg, #ff0040, #00ff40, #ffd700) 1;
        border-radius: 8px;
        padding: 24px;
        margin: 20px auto;
        max-width: 650px;
        color: #00ff40;
        font-family: monospace;
    }
    
    .instructions h3 {
        color: #ffd700;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        font-family: 'Georgia', serif;
        margin-bottom: 12px;
    }
    
    .instructions ul {
        list-style-type: none;
        padding-left: 0;
    }
    
    .instructions li {
        padding: 6px 0;
        color: #ffffff;
    }
    
    .instructions li::before {
        content: "🎁 ";
    }
    
    /* Key styling */
    .key {
        display: inline-block;
        background: linear-gradient(180deg, #1a0a0a, #0d1a0d);
        border: 1px solid #ff0040;
        border-radius: 4px;
        padding: 2px 8px;
        margin: 0 2px;
        font-family: monospace;
        color: #ff0040;
    }
    
    /* Score colors */
    .score-red { color: #ff0040; }
    .score-green { color: #00ff40; }
    .score-gold { color: #ffd700; }
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
        
        # Instructions section - Christmas themed
        st.markdown("""
        <div class="instructions">
            <h3>🎄 SANTA'S CONTROLS 🎄</h3>
            <ul>
                <li><span class="key">W</span> <span class="key">A</span> <span class="key">S</span> <span class="key">D</span> or <span class="key">↑</span> <span class="key">←</span> <span class="key">↓</span> <span class="key">→</span> — Guide Santa through the maze</li>
                <li>Collect all binary presents (0s and 1s) to save Christmas!</li>
                <li>Avoid the Grinch bots — they want to steal Christmas!</li>
                <li>Grab the Christmas Stars ⭐ to gain Christmas Spirit power</li>
                <li>With Christmas Spirit, you can defeat the Grinch bots!</li>
            </ul>
            <h3>🎁 PRESENT VALUES 🎁</h3>
            <ul>
                <li>Binary present: <span class="score-green">+10 pts</span></li>
                <li>Christmas Star: <span class="score-gold">+50 pts</span></li>
                <li>Grinch (1st): <span class="score-red">+200 pts</span></li>
                <li>Grinch (2nd): <span class="score-red">+400 pts</span></li>
                <li>Grinch (3rd): <span class="score-red">+800 pts</span></li>
                <li>Grinch (4th): <span class="score-gold">+1600 pts</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
        <div style="text-align: center; color: #ffd700; font-family: 'Georgia', serif; margin-top: 30px; font-size: 14px;">
            🎄 BINARY EATER // CHRISTMAS CYBER EDITION 🎄<br>
            <span style="color: #888; font-size: 12px;">Press any movement key or click START CHRISTMAS to play!</span>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
