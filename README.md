# Smart Photo Album

## Overview

The Smart Photo Album is a web application that allows users to upload, store, and search photos using natural language queries. This project uses several AWS services, including ElasticSearch, S3, Lambda, Rekognition, Lex, CodePipeline, and API Gateway. 

## Features

1. **Photo Upload and Indexing**

2. **Natural Language Search**
  
3. **Continuous Deployment Using AWS CodePipeline**
   - AWS CodePipeline automates the build and deployment 

## Components

### 1. ElasticSearch Instance
- **Service:** AWS ElasticSearch

### 2. S3 Buckets
- **Photo Storage Bucket** 
- **Frontend Bucket** 

### 3. Lambda Functions
- **L1** Triggered by S3 PUT events to index photos.
- **L2:** Handles search queries from the Lex bot and queries ElasticSearch.

### 4. Amazon Lex Bot


### 5. API Gateway
- **Endpoints:**
  - **PUT /photos:** Upload photos with optional custom labels.
  - **GET /search?q={query text}:** Search photos using natural language text.

### 6. AWS CodePipeline
- Pipeline for Backend
- Pipeline for Frontend

### 7. AWS CloudFormation Template
- Sets up S3 buckets, Lambda functions, API Gateway, and IAM roles.

