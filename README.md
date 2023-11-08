# flask_6_api_management
HHA504 / Cloud Computing / Assignment 6 / API Management

This repo aims to develop and document APIs using Flask, and manage them with Azure API Management.

## This repo contains the following: 
+ **LocalFunctionProj** folder: contains information for creating a function in Azure
+ **recordings** folder: contains video recordings showcasing the functionality of the Flask and Azure API endpoints
+ **screenshots** folder: contains screenshots of the Flask and Azure API endpoints and Swagger API docs
+ **README.md** file: contains an overview of the repo
+ **app.py** file: contains script to run the Flask API endpoint

# Documentation
### 1. Flask-based RESTful API w/ Swagger
Used Flask to develop an endpoint to handle a simple GET request. The endpoint created will take in a first name and a last name and returns and a json message of: ```message: Hello, <first name> <last name>!```. The Flask app also includes Swagger/OpenAPI documentation using the ```flasgger``` package. Swagger docstring documentations are included in the script. When run, the Flask app will first return a home/main page. To go to the created endpoint, I inputted ```hello?first=susan&last=chen``` after the forward slash (/) in the URL. To get to the Swagger documentation, input ```apidocs``` instead. The following links to the endpoints are included below. The highlighted parts of the link can be edited to reach the endpoints: 
+ **Main Page**: https://5000-cs-1039191608401-default.cs-us-east1-pkhd.cloudshell.dev/?authuser=0
+ **Name Endpoint**: https://5000-cs-1039191608401-default.cs-us-east1-pkhd.cloudshell.dev/**hello?first=susan&last=chen**
+ **Swagger Documentation Endpoint**: https://5000-cs-1039191608401-default.cs-us-east1-pkhd.cloudshell.dev/**apidocs**

### 2. Azure API deployment
Link: https://flaskfunction.azurewebsites.net/api/hello  

To create a function in Azure and deploy the API endpoint, the following steps were done: 
1. In the google shell terminal, intall Azure CLI with: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```.Run ```az``` in the terminal to confirm it is installed. 
2. Login to to your Azure account using ```az login --use-device-code``` and follow the directions from the output.
3. Install the Azure Core Tools package using ```sudo apt-get install azure-functions-core-tools-4```.
4. Once the package is installed, run ```func init LocalFunctionProj --python -m V2``` to create a local function. A **LocalFunctionProj** folder will appear containing files to create the function in Azure.
5. In the **LocalFunctionProj** folder, go to the ```local.settings.json``` file and change the script to: 
```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true"
  }
}
```

6. In the terminal, Install azure.functions with ```pip install azure-functions```
7. In the ```function_app.py``` folder, change the code to create an endpoint.
8. To deploy the app, the following are required: resource group, storage account, and a function app.
  + To create a resource group, run:
```az group create --name <creeate resource group name>-rg --location <REGION>```
  + To create a storage account, run:
```az storage account create --name <create a storage account name> --location <REGION> --resource-group <resource group name> --sku Standard_LRS```
  + To create a function app, run:
```az functionapp create --resource-group <esource group name>-rg --consumption-plan-location <REGION> --runtime python --runtime-version 3.9 --functions-version 4 --name <create a name for the function app> --os-type linux --storage-account <storage account name>```
9. Deploy the app with: ```func azure functionapp publish <function app name>```
10. To update the app settings, run: ```az functionapp config appsettings set --name <FUNCTION_APP_NAME> --resource-group <RESOURCE_GROUP_NAME> --settings AzureWebJobsFeatureFlags=EnableWorkerIndexing```

