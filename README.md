# Walkthrough

## 1. Create S3 buckets
Create two S3 buckets, one for raw images and one for edited images.
<img width="1068" height="296" alt="image" src="https://github.com/user-attachments/assets/02c5d0ae-e24a-4a65-a2c8-fbf67a79684c" />


## 2. Create new Lambda function
### 2.1 
Download pillow-layer.zip
### 2.2 
Upload the pillow-layer zip folder as a Lambda layer
<img width="1601" height="135" alt="image" src="https://github.com/user-attachments/assets/d361e1be-6fe2-42f7-8c92-14422e5108a7" />

### 2.3 
Update Lambda code
<img width="1598" height="751" alt="image" src="https://github.com/user-attachments/assets/100c55d2-d7c7-4efa-9bab-168590043329" />

### 2.4
Add the output bucket as an environmental variable
<img width="1334" height="215" alt="image" src="https://github.com/user-attachments/assets/f2c51f03-8e74-4f1e-9a13-a796a8afc1a2" />

## 3. Create State Machine
### 3.1 
Place the Lambda function as the first item in the chain
### 3.2
Place a choice state after the Lambda finishes running
### 3.3
Return success if the Lambda succeeds, otherwise return failure
<img width="1361" height="826" alt="image" src="https://github.com/user-attachments/assets/2ee3d849-e9f0-4c86-b8d3-cc4e9811be2d" />

## 4. Create new REST API Gateway
### 4.1 
Create POST method
<img width="292" height="254" alt="image" src="https://github.com/user-attachments/assets/5815a424-3bc3-4c21-84d3-ab3ff10a17f4" />

### 4.2
Provide mapping template in Integration Request
<img width="952" height="274" alt="image" src="https://github.com/user-attachments/assets/22ced635-5d4c-4125-9ffc-35422fccff8f" />

## 5. Run the link through Postman
## 5.1
Provide the variables in the body
<img width="1386" height="393" alt="image" src="https://github.com/user-attachments/assets/b8dee46c-bcda-4084-b43f-f3173e85be32" />

