# A* Path Finding Algorithm Visualization

This is an interactive visualization of the A* pathfinding algorithm using Streamlit and Pygame.

## Features

- Interactive grid where you can place start point, end point, barriers, and weighted nodes
- Real-time visualization of the A* algorithm
- Adjustable animation speed
- Clear grid functionality
- Support for diagonal movement
- Weighted nodes that increase path cost

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Controls:
- Left click to place:
  - Start point (orange)
  - End point (turquoise)
  - Barriers (black)
  - Hold Shift + Left click to place weighted nodes (grey)
- Right click to remove nodes
- Press Space to start the algorithm
- Use the sidebar to adjust animation speed
- Click "Clear Grid" to reset the grid

## Color Legend

- Orange: Start point
- Turquoise: End point
- Black: Barriers
- Grey: Weighted nodes (5x cost)
- Red: Closed nodes
- Green: Open nodes
- Purple: Final path 