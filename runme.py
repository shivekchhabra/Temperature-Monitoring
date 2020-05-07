import flirimageextractor
import plotly.graph_objects as go
import os
import numpy as np


def temp_analysis(name):
    flir = flirimageextractor.FlirImageExtractor()
    flir.process_image(name)
    temp = flir.thermal_image_np.reshape((flir.thermal_image_np.size, 1))
    mean = np.sum(temp) / flir.thermal_image_np.size
    return mean


def line_plotting(x, y, mean_list):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Temperature'))
    fig.add_trace(go.Scatter(x=x, y=mean_list,
                             mode='lines+markers',
                             name='Mean Temperature'))
    fig.show()


def single_image(path):
    temperature = temp_analysis(path)
    return temperature


def multiple_images(folder_path):
    temp = []
    images = []
    mean_vals = []
    mean_list = []
    counter = 0

    for i in os.listdir(path_of_folder):
        counter = counter + 1
        temp = temp + [(temp_analysis(path_of_folder + i))]
        images = images + ['Image {}'.format(counter)]
        mean_vals.append(temp_analysis(path_of_folder + i))
    print('Highest temperature - ', np.max(mean_vals))
    print('Lowest temperature - ', np.min(mean_vals))
    print('Mean Temperature - ', np.mean(mean_vals))
    for i in range(len(images)):
        mean_list = mean_list + [np.mean(mean_vals)]
    line_plotting(images, temp, mean_list)


if __name__ == '__main__':
    # For single image testing
    print('-----------Single Image------------------------')
    temperature = single_image('sample.jpg')
    print('Temperature of Sample Image: ', temperature)

    # For multiple images in a folder
    print('-----------Multiple Images------------------------')
    path_of_folder = os.getcwd() + '/sample_images/'
    multiple_images(path_of_folder)
