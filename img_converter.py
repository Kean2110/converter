import os
import imageio
import rawpy
from rich.progress import track


input_dir = "input/"
output_dir = "output/"
output_format = ".jpg"


input_files = os.listdir(input_dir)
for file in track(input_files):
    file_name, file_extension = os.path.splitext(file)
    img = os.path.join(input_dir, file)
    with rawpy.imread(str(img)) as raw:
        # for deeper dive into params visit the RawPy documentation
        rgb = raw.postprocess(rawpy.Params(use_camera_wb=True))
    new_location = os.path.join(output_dir, file_name + output_format)
    imageio.imsave(new_location, rgb)