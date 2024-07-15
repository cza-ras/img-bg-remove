import requests 
import shutil 

# Set your API key 
api_key = "YOUR_API_KEY" 


# Set the input and output file paths 
input_path = "Projects/img-bg-remove/sample_image.jpg" 
output_path = "Projects/img-bg-remove/sample_image_api.jpg" 


# Set the API endpoint URL 
url = "https://api.remove.bg/v1.0/removebg" 


# Set the API request headers and data 
headers = {"X-Api-Key": api_key} 
data = {"size": "auto"} 
files = {"image_file": open(input_path, "rb")} 

# Send the API request and save the output image 
response = requests.post(url, headers=headers, data=data, files=files, stream=True) 
with open(output_path, "wb") as out_file: shutil.copyfileobj(response.raw, out_file)