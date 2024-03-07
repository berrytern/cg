import matplotlib.pyplot as plt

def inp_to_ndc(x, y, width, height):
    ndc_x = x / width
    ndc_y = y / height
    return ndc_x, ndc_y

def ndc_to_user(ndc_x, ndc_y, width, height):
    user_x = ndc_x * width
    user_y = ndc_y * height
    return user_x, user_y

def user_to_ndc(user_x, user_y, width, height):
    ndc_x = user_x / width
    ndc_y = user_y / height
    return ndc_x, ndc_y

def ndc_to_dc(ndc_x, ndc_y, dc_width, dc_height):
    dc_x = ndc_x * dc_width
    dc_y = ndc_y * dc_height
    return dc_x, dc_y

# Valores de entrada
input_x, input_y = 50, 30
input_width, input_height = 100, 60

# Transformação de coordenadas
ndc_coordinates = inp_to_ndc(input_x, input_y, input_width, input_height)
user_coordinates = ndc_to_user(*ndc_coordinates, input_width, input_height)
dc_coordinates = ndc_to_dc(*ndc_coordinates, dc_width=200, dc_height=120)

# Plotagem
plt.figure(figsize=(10, 4))

# Subplot 1: Coordenadas de entrada
plt.subplot(131)
plt.scatter(input_x, input_y, label='Input Coordinates')
plt.title('Input Coordinates')
plt.legend()

# Subplot 2: Coordenadas normalizadas (NDC)
plt.subplot(132)
plt.scatter(*ndc_coordinates, label='NDC Coordinates')
plt.title('NDC Coordinates')
plt.legend()

# Subplot 3: Coordenadas de dispositivo (DC)
plt.subplot(133)
plt.scatter(*dc_coordinates, label='DC Coordinates')
plt.title('DC Coordinates')
plt.legend()

plt.tight_layout()
plt.show()
