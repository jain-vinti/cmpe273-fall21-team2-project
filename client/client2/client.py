import requests

# Set up url for send request to
# In this case the url is of proxy server,
# That acts a load balancer to 
# Distribute jobs to worker nodes

url = 'http://localhost:8081'

# opening a test file with python code inside 
# Ready to be executed


with open('test.py', 'rb') as f:
    output = requests.post(url, data=f)

#print the output recieved from the server
print(output.text)
