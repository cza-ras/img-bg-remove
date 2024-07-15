from rembg import remove


#image path
input_path="Projects/img-bg-remove/sample_image.jpg"
output_path="Projects/img-bg-remove/ready_image_rembg.jpg"


with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        original_image = i.read()
        output = remove(original_image)
        o.write(output)
