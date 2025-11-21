# CCMPFinal

# Walkthrough

## 1. Create S3 buckets
Create two S3 buckets, one for raw images and one for edited images.

## 2. Create new Lambda function
### 2.1 
Download pillow-layer.zip
### 2.2 
Upload the pillow-layer zip folder as a Lambda layer
### 2.3 
Update Lambda code
### 2.4
Add the output bucket as an environmental variable

## 3. Create State Machine
### 3.1 
Place the Lambda function as the first item in the chain
### 3.2
Place a choice state after the Lambda finishes running
### 3.3
Return success if the Lambda succeeds, otherwise return failure

## 4. Create new REST API Gateway
### 4.1 
Create POST method
### 4.2
Provide mapping template in Integration Request

## 5. Run the link through Postman
## 5.1
Provide the variables in the body
