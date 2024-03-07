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

input_x, input_y = 50, 30
input_width, input_height = 100, 60

ndc_coordinates = inp_to_ndc(input_x, input_y, input_width, input_height)
user_coordinates = ndc_to_user(*ndc_coordinates, input_width, input_height)
dc_coordinates = ndc_to_dc(*ndc_coordinates, dc_width=200, dc_height=120)

fig, axs = plt.subplots(1, 3, figsize=(10, 4))

axs[0].scatter(input_x, input_y, label='Input Coordinates')
axs[0].set_title('Input Coordinates')

axs[1].scatter(*ndc_coordinates, label='NDC Coordinates')
axs[1].set_title('NDC Coordinates')

axs[2].scatter(*dc_coordinates, label='DC Coordinates')
axs[2].set_title('DC Coordinates')

plt.tight_layout()

def on_move(event):
    if event.inaxes is not None:
        x, y = event.xdata, event.ydata
        print(f"Mouse position: x={x}, y={y}")

fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
