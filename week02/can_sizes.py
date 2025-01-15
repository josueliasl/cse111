import math

def main():
    # Can data: name, radius (cm), height (cm), cost per can (usd)
    cans_information = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#2 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8z Short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
    ]
    for can in cans_information:
        can['volume'] = compute_volume(can['radius'], can['height'])
        can['area'] = compute_area(can['radius'], can['height'])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        print(f"{can['name']:<15}{storage_efficiency:>20.2f}")
    return cans_information

def compute_volume(radius, height):
    return math.pi * (radius ** 2) * height

def compute_area(radius, height):
    return 2 * math.pi * (radius ** 2) + 2 * math.pi * radius * height

def compute_storage_efficiency(volume, surface_area):
    """Compute the storage efficiency of a can."""
    volume = compute_volume
    return volume / surface_area

cans_info = main()
for can in cans_info:
    print(f"{can['name']} - Volume: {can['volume']:.2f} cm³ - Area: {can['area']:.2f}")

print()