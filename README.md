# Smart Photo Album

## Overview

The Smart Photo Album is a web application that allows users to upload, store, and search photos using natural language queries. This project leverages several AWS services, including ElasticSearch, S3, Lambda, Rekognition, Lex, API Gateway, and CodePipeline. The application provides an intelligent search layer to query photos for people, objects, actions, landmarks, and more.

## Features

1. **Photo Upload and Indexing:**
   - Users can upload photos to an S3 bucket.
   - Photos are automatically indexed with labels detected using AWS Rekognition.
   - Custom labels can be added during upload.

2. **Natural Language Search:**
   - Users can search for photos using natural language queries.
   - An Amazon Lex bot handles search queries and disambiguation.
   - The search results are fetched from an ElasticSearch index.

3. **API Integration:**
   - API Gateway provides endpoints for photo upload and search.
   - A frontend application interacts with the backend APIs.

4. **Continuous Deployment:**
   - AWS CodePipeline automates the build and deployment processes for both frontend and backend code.
   - AWS CloudFormation template sets up the necessary infrastructure and permissions.

## Architecture

![image](https://github.com/moinkhan3012/Smart-Photo-Album/assets/35172739/5a4f235d-dd6a-4be4-95b1-3cc0d76b378c)


## Components

### 1. ElasticSearch Instance
- **Service:** AWS ElasticSearch
- **Domain:** photos

### 2. S3 Buckets
- **Photo Storage Bucket:** Stores uploaded photos.
- **Frontend Bucket:** Hosts the frontend application.

### 3. Lambda Functions
- **Index-Photos:** Triggered by S3 PUT events to index photos.
- **Search-Photos:** Handles search queries from the Lex bot and queries ElasticSearch.

### 4. Amazon Lex
- **Bot Name:** Searchy
- **Intent:** SearchIntent
- **Utterances:** "show me photos of {label}", "find pictures of {label}", "photos with {label}", etc.

### 5. API Gateway
- **Endpoints:**
  - **PUT /photos:** Upload photos with optional custom labels.
  - **GET /search?q={query text}:** Search photos using natural language text.

### 6. AWS CodePipeline
- **Pipeline for Backend:** Builds and deploys Lambda functions.
- **Pipeline for Frontend:** Builds and deploys the frontend application to S3.

### 7. AWS CloudFormation
- **Template:** Sets up S3 buckets, Lambda functions, API Gateway, and IAM roles.

## Getting Started

### Prerequisites

- AWS Account
- AWS CLI configured
- Node.js and npm installed
- GitHub repository: [Smart-Photo-Album](https://github.com/moinkhan3012/Smart-Photo-Album)

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/moinkhan3012/Smart-Photo-Album.git
   cd Smart-Photo-Album
   ```

2. **Launch ElasticSearch Instance:**
   - Navigate to AWS ElasticSearch Service and create a new domain called "photos".

3. **Create S3 Buckets:**
   - Create a bucket (e.g., `photo-storage-bucket`) for storing photos.
   - Create another bucket (e.g., `frontend-bucket`) for hosting the frontend application.

4. **Deploy Lambda Functions:**
   - Create a Lambda function called `index-photos`.
   - Set up a PUT event trigger on the photo storage bucket to invoke `index-photos`.
   - Create a Lambda function called `search-photos`.

5. **Configure Amazon Lex:**
   - Create a Lex bot with an intent named `SearchIntent` or you can import the bot from the `serchy-bot.zip`.
   - Add training utterances for keyword and sentence searches.

6. **Set Up API Gateway:**
   - Create an API with endpoints for uploading photos and searching photos.
   - Connect the endpoints to the respective Lambda functions.

7. **Deploy Frontend:**
   - Build the frontend application and upload the files to the frontend S3 bucket.
   - Enable static website hosting for the frontend bucket.

8. **Set Up AWS CodePipeline:**
   - Define pipelines for deploying Lambda functions and frontend code.
   - Integrate with GitHub for continuous deployment.

9. **CloudFormation Template:**
   - Use the provided CloudFormation template to set up the required resources and permissions.

### Usage

- **Uploading Photos:**
  - Use the frontend application to upload photos and specify custom labels if needed.
  - Photos will be indexed automatically.

- **Searching Photos:**
  - Enter natural language queries in the frontend search bar.
  - The Lex bot will handle the query and fetch relevant photos from ElasticSearch.

