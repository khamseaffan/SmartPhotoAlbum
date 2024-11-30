import json
import boto3
import logging
import os
from elasticsearch import Elasticsearch
import uuid

logger = logging.getLogger()
logger.setLevel("INFO")


def search_doc(labels):

    client = Elasticsearch(
        hosts=[{'host': os.environ.get("ES_HOST"), 'port': 443}],
        http_auth=["master", "Cloud@2024"],
        scheme="https",
        port=443    ,
        verify_certs=True,
    )
    
    # client = Elasticsearch(
    #     f"https://{os.environ.get('ES_HOST')}:443",
    #     basic_auth=(os.environ.get('ES_USERNAME'), os.environ.get('ES_PASSWORD')),
    #     verify_certs=True
    # )


    query_template = {
      "query": {
        "bool": {
          "must": [ {"match": {"labels": label}} for label in labels]
        }
      },
      "size": 1000
    }


    # query_template = {
    #     "query": {
    #         "match_all": {}
    #     },
    #     "size": 1000  # Limits the number of documents retrieved
    # }


    try:
        # Perform search query
        response = client.search(index=os.environ.get('ES_INDEX_NAME'),body=query_template)
        logger.info(response)
        hits = response['hits']['hits']
        return hits
    except Exception as err:
        logger.error(err)
        return []



def lambda_handler(event, context):
    logger.info(event)
    lex = boto3.client('lexv2-runtime')
    logger.info("Event")
    response = lex.recognize_text(
        botId=os.environ.get('BOT_ID'), 
        botAliasId='TSTALIASID',
        sessionId= str(uuid.uuid4()),
        localeId='en_US',  
        text = event['queryStringParameters']['q']
    )
    
    logger.info("received response frmo lex")
    logger.info(response)
    
    #check if keywords identified by the lex
    
    if response['sessionState']['intent']['name'] =='SearchIntent' and response['sessionState']['intent']['slots']:
        #call ES service to fetch the photos
        
        logger.info(response['sessionState']['intent']['slots'])
        keywords = [ keyword['value']['originalValue'] for keyword in response['sessionState']['intent']['slots'].values() if keyword and keyword['value']['originalValue'] ]
        
        if not keywords:
            return {
                'statusCode': 404,
                'headers': {
				"Access-Control-Allow-Origin": "*"
			},
                'body':
                    json.dumps({
                'message': "No valid keyword found for searching. Please retry with new keywords."
            })
            }
        
        search_results = search_doc(keywords)
        
        logger.info(search_results)
        if not search_results:
            #return empty response
            return {
                "statusCode": 202,
                "headers": {
                    "Access-Control-Allow-Origin" : "*"
                },
                "body": json.dumps({
                    "message": "We don't have any images with the keyword you searched. You can try to upload one!!!."
                })
            }
            
        
        image_urls = [ f"https://{result['_source']['bucket']}.s3.amazonaws.com/{result['_source']['objectKey']}" for result in search_results]
        
        logger.info(search_results)
        return {
            'statusCode': 200,
            'headers': {
				"Access-Control-Allow-Origin": "*"
			},
            'body':  json.dumps({
                    "images": image_urls
                })
        }

    #no keyword found by the Lex
    #send negative response
    return {
        'statusCode': 404,
        'headers': {
    	"Access-Control-Allow-Origin": "*"
    },
        'body':
            json.dumps({
        'message': "No valid keyword found for searching. Please retry with new keywords."
    })
    }