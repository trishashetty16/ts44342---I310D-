def compute_volume_of_sphere(radius):
	pi = 3.14
	volume = pi * radius * radius * radius * (4/3)
	return volume

radius1 = 40
volume1 = compute_volume_of_sphere (radius1)
print(f"The area of circle with radius {radius1} is: {area1}")

radius2 = 60
volume2 = compute_volume_of_sphere(radius2)
print(f"The area of circle with radius {radius2} is: {area2}")
