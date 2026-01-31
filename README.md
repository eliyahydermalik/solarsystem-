# 🌌 Solar System Simulation (Python)

A real-time 2D Solar System simulation built using **Python** and **Pygame**, based on **Newton’s Law of Universal Gravitation**.  
Planets move in realistic orbits calculated using pure physics and mathematics — no animation tricks.

---

## 🚀 Features

- Realistic planetary motion using gravity  
- Newtonian physics calculated every frame  
- Multiple planets with real mass and velocity  
- Orbit trails showing motion history  
- Time-step based physics simulation  
- Built completely from scratch (no physics engine)

---

## 🧠 How It Works

Each planet is treated as an object with:
- Position (x, y)
- Mass
- Velocity (x and y)

For every frame:
1. Gravitational force is calculated between planets  
2. Acceleration is derived using **F = m × a**  
3. Velocity is updated using acceleration  
4. Position is updated using velocity  
5. Positions are stored to draw orbit paths  

This continuous update creates realistic elliptical orbits.

---

## 🛠️ Technologies Used

- Python 3
- Pygame
- Mathematics (Vectors & Trigonometry)

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install pygame
Run the simulation:

python solarsystem.py

📂 Project Structure
solarsystem.py   # Main simulation file
README.md        # Project documentation

🎥 Tutorial Video

This project is explained step-by-step in a YouTube video (Hinglish).
📺 Link: 
