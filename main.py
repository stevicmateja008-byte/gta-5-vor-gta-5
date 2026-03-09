from ursina import *
from vehicle import Vehicle
from weapon import Weapon

# Ursina App initialisieren
app = Ursina()
camera.position = (0, 15, -25)
camera.rotation_x = 45

# Sky/Hintergrund
sky_texture = load_texture('white_cube')
sky = Sky(texture=sky_texture)

# Spielwelt
player_vehicle = Vehicle(position=(0, 2, 0))
weapon_system = Weapon(player_vehicle)

# Gebäude/Hindernisse in der Umgebung
buildings = []

# Gebäude 1
building1 = box(pos=(20, 5, 30), size=(10, 10, 10), color=color.gray)
buildings.append(building1)

# Gebäude 2
building2 = box(pos=(-30, 5, -20), size=(15, 10, 10), color=color.dark_gray)
buildings.append(building2)

# Gebäude 3
building3 = box(pos=(40, 5, -40), size=(12, 8, 12), color=color.light_gray)
buildings.append(building3)

# Boden/Terrain
ground = box(pos=(0, -1, 0), size=(200, 1, 200), color=color.green)

# UI - Spieler-Info
info_text = Text(text='GTA-5 ähnliches Spiel v1.0', position=(-0.9, 0.45), scale=1)
controls_text = Text(
    text='WASD: Fahren | SPACE: Bremse | CLICK: Schießen',
    position=(-0.9, 0.35),
    scale=0.8
)

# Game Loop
def update():
    # Update Auto
    player_vehicle.update(dt)
    
    # Update Waffen
    weapon_system.update(dt)
    
    # Kamera folgt dem Auto
    camera.position = player_vehicle.get_position() + (0, 15, -25)
    camera.look_at(player_vehicle.entity)
    
    # Schießen mit Mausklick
    if mouse.left_pressed:
        weapon_system.shoot()
    
    # Collision Detection (einfach)
    weapon_system.check_collisions(buildings)
    
    # Rückgabe False verhindert weitere Event-Verarbeitung
    return False

# Starte Game Loop
app.run()