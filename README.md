# End - to - End Text-Summarizer


# Workflows
1. Update config.yaml file
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

# How to run?
### Steps:

Clone the Repository

``` bash
https://github.com/DeekshaMalviya/Text-Summarizer
```

### Step 1: Create a conda environment after opening the repository

```bash
conda create -n summary python=3.11.11 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```
Now,
```bash
open up you local host and port
```

```bash
Author: Deeksha Malviya
Email: deekshamalviyacp@gmail.com
```


# AWS-CI/CD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

# 3. Create ECR repo to store/save docker image

# 4. Create EC2 machine (Ubuntu)

# 5. Open EC2 and Install docker in EC2 Machine

# 6. Configure EC2 as self-hosted runner
 
# 7. Setup github secrets
