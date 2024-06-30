# PortfolioApi
PortfolioAPI is a RESTful service designed to seamlessly integrate with MongoDB, enabling efficient CRUD operations across various collections. It serves as the backbone for user interfaces that display comprehensive portfolio information, including work experiences and projects, tailored for individuals looking to showcase their professional journey. Unique to our API is the integration of a sophisticated Chatbot, powered by OpenAI's latest GPT-4o model, which acts as a personal assistant, enriching user interaction with instant, intelligent responses to inquiries.

## Getting Started

### Prerequisites
  - Python 3.10

## Installation
### Virtual Environment Set-up
1. Let's set-up a python virtual environment by running the command below:
   * python3.10 -m venv /path/to/new/virtual/environment
2. Activate your virtual environment.
   * source /path/to/new/virtual/environment/bin/activate
3. Run the following command to install all the packages inside the requirements.txt file:
   * pip install -r requirements.txt
   
### Environment Variables
Add the following environment variables to the project:
* ATLAS_ADMIN_USER
* ATLAS_ADMIN_PW
* ATLAS_CONN_STR
* ATLAS_DB_NAME
* ATLAS_VECTOR_COLLLECTION
* ATLAS_VECTOR_INDEX_NAME
* ATLAS_EMBEDDING_KEY
* OPENAI_API_KEY
* OPENAI_EMBEDDING_MODEL
* OPENAI_CHAT_MODEL
* LANGCHAIN_PROJECT
* LANGCHAIN_API_KEY

### Docker
If you are using docker, please follow the instructions below:
1. Run the following command to create a docker image:
   * docker build -t "image-name" .
2. Create a container:
   * docker run --name "container-name" --env-file "env-file" "name-of-your-docker-image"

### Atlas Collection Schema
```javascript
{
  "$jsonSchema": {
    "bsonType": "object",
    "required": [
      "_id",
      "type",
      "createdAt"
    ],
    "properties": {
      "_id": {
        "bsonType": "objectId"
      },
      "type": {
        "enum": [
          "user",
          "profile",
          "experience",
          "project",
          "achievement"
        ],
        "description": "The type field should be one of the following values: user, profile, experience, project, achievement"
      },
      "createdAt": {
        "bsonType": "date",
        "description": "The createdAt field must be a date field."
      },
      "userId": {
        "bsonType": "string",
        "description": "The userId field must a string that uniquely identifies a user."
      }
    },
    "additionalProperties": false,
    "dependencies": {
      "type": {
        "oneOf": [
          {
            "required": [
              "userId",
              "emailAddress"
            ],
            "properties": {
              "type": {
                "enum": [
                  "user"
                ]
              },
              "emailAddress": {
                "bsonType": "string",
                "description": "The emailAddress field must be a string."
              }
            }
          },
          {
            "required": [
              "userId",
              "firstName",
              "lastName",
              "shortBio"
            ],
            "properties": {
              "type": {
                "enum": [
                  "profile"
                ]
              },
              "firstName": {
                "bsonType": "string",
                "description": "The firstName field must be a str no longer than 150 characters.",
                "maxLength": 150
              },
              "lastName": {
                "bsonType": "string",
                "description": "The lastName field must be a str no longer than 250 characters.",
                "maxLength": 250
              },
              "dateOfBirth": {
                "bsonType": [
                  "date",
                  "null"
                ],
                "description": "The dateOfBirth field must be a date or null."
              },
              "hobbies": {
                "bsonType": "array",
                "items": {
                  "bsonType": "string",
                  "description": "The hobbies field must be an array of string."
                }
              },
              "skills": {
                "bsonType": "array",
                "items": {
                  "bsonType": "string",
                  "description": "The skills field must be an array of string or null"
                }
              },
              "shortBio": {
                "bsonType": "string",
                "description": "The shortBio field must be a string no longer than 1000 characters.",
                "maxLength": 1000
              },
              "bio": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The bio field must be null or a string no longer than 2000 characters.",
                "maxLength": 2000
              },
              "countryOfBirth": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The countryOfBirth field must be a string no longer than 100 characters or null."
              },
              "countryOfResidence": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The countryOfResidence field must be a string no longer than 100 characters or null."
              },
              "linkedInUrl": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The linkedInUrl field must be a string or null."
              },
              "gitHubUrl": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The gitHubUrl field must be a string or null."
              }
            }
          },
          {
            "required": [
              "userId",
              "name",
              "description"
            ],
            "properties": {
              "type": {
                "enum": [
                  "project"
                ]
              },
              "name": {
                "bsonType": "string",
                "description": "Project name should be a string no longer than 250 characters.",
                "maxLength": 250
              },
              "description": {
                "bsonType": "string",
                "description": "Project description should be a string no longer than 1000 characters",
                "maxLength": 1000
              },
              "badges": {
                "bsonType": "array",
                "items": {
                  "bsonType": "object",
                  "description": "Project badges should be an object with a name property and an url property.",
                  "required": [
                    "name",
                    "url"
                  ],
                  "properties": {
                    "name": {
                      "bsonType": "string",
                      "description": "Badge name should be a string no longer than 100 characters.",
                      "maxLength": 100
                    },
                    "url": {
                      "bsonType": "string",
                      "description": "Badge url should be a string."
                    }
                  }
                }
              },
              "images": {
                "bsonType": "array",
                "items": {
                  "bsonType": "string",
                  "description": "Project images should be an array of string."
                }
              }
            }
          },
          {
            "required": [
              "userId",
              "jobTitle",
              "company",
              "startDate"
            ],
            "properties": {
              "type": {
                "enum": [
                  "experience"
                ]
              },
              "jobTitle": {
                "bsonType": "string",
                "description": "The job title field must be a string no longer than 100 characters.",
                "maxLength": 100
              },
              "jobDescription": {
                "bsonType": [
                  "null",
                  "string"
                ],
                "description": "The job description field must be null or a string no longer than 1500 characters.",
                "maxLength": 1500
              },
              "company": {
                "bsonType": "string",
                "description": "The company field must be a string no longer than 100 characters.",
                "maxLength": 100
              },
              "startDate": {
                "bsonType": "date",
                "description": "The startDate field must be a date."
              },
              "endDate": {
                "bsonType": [
                  "null",
                  "date"
                ],
                "description": "The endDate field must be null or a date."
              }
            }
          },
          {
            "required": [
              "userId",
              "name",
              "eduEntity"
            ],
            "properties": {
              "type": {
                "enum": [
                  "achievement"
                ]
              },
              "name": {
                "bsonType": "string",
                "description": "The achievement name field must be a string no longer than 150 characters.",
                "maxLength": 150
              },
              "description": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The achievement description field must be null or a string no longer than 1000 characters.",
                "maxLength": 1000
              },
              "url": {
                "bsonType": [
                  "string",
                  "null"
                ],
                "description": "The achievement url field must be null or a string."
              },
              "eduEntity": {
                "bsonType": "string",
                "description": "The eduEntity field must be a string no longer than 150 characters.",
                "maxLength": 150
              }
            }
          }
        ]
      }
    }
  },
  "validationLevel": "strict"
}
```

# Data Design

This section provides a detailed overview of the data design, including the database schema, entity relationships, and security measures implemented to protect the data.

## Overview

The Portfolio API utilizes two main types of databases to store and manage data efficiently: MongoDB Atlas, a NoSQL database for storing portfolio information, and Pinecone Vector Database, a specialized database for managing vector data to enhance chatbot functionalities.

### Diagrams

#### Model Data Classes UML 
<img width="3936" alt="Portfolio Dataclasses (1)" src="https://github.com/JGVR/PortfolioApi/assets/54122915/a3ecddeb-4625-4256-b6cd-1397705456c4">

#### ChatBot Classes UML 
![ChatBot (1)](https://github.com/JGVR/PortfolioApi/assets/54122915/a1276fd5-f9d7-4a3a-a309-c1033931494e)

## Chatbot
- **Description**: A Chatbot that will act as your "Assistance" to answer questions only about you.
 ### Data Classes:
  ### Message(ABC)
   - **Fields**:
     - `text`: str
  ### Question(Message)
   - **Fields**:
     - `text`: inherited from Message class. This field will hold the user's question.
  ### Answer(Message)
   - **Fields**:
     -  `text`: inherited from Message class. This field will hold the chatbot answer to the user's question.
     -  `question`: A Question object. Represents the user's question.
     -  `chat_history`: Langchain ChatMessageHistory object. This field will hold the history of the conversation.
     -  `completed`: A bool object. This field represents if the answered is completed.
   - **Methods**:
     -  `from_chunks(cls, chunks: List[str], question: Question, chat_history: ChatMessageHistory) -> Answer`: Creates an answer object from chunks of text.
     -   `serialize(self) -> Dict[str, Any]`: Converts the Answer object to a Dictionary.
  ### RelevantDoc
   - **Fields**:
     -  `content`: str. This field contain the content of the relevant docs that the chatbot will use as context to answer the user's question.
   - **Methods**:
     -  `serialize(self) -> Dict[str, Any]`: Converts the RelevantDoc object to a Dictionary.
  ### DocRetriever
   - **Fields**:
     - `vector_store`: Langchain MongoDBAtlasVectorSearch object. This will be used to extract the appropriate relevant docs from Atlas.
     - `k`: int. This property will control the amount of relevant documents that will be extracted from Atlas.
   - **Methods**:
     - `call(self, question: Question) -> List[RelevantDoc]`: method used to call the service class which will extract the relevant docs from Atlas.
  ### FollowUpQuestionBuilder
   - **Fields**:
     - `llm`: Langchain ChatOpenAI Object. This will be used to call the appropriate OpenAI llm.
   - **Methods**:
     - `call(self, question: Question, chat_history_summary: str) -> Question`: method used to call the service class which will reconstruct the user's question taking into account the conversation's history.
  ### ChatHistorySummarizer
   - **Fields**:
     - `llm`: Langchain ChatOpenAI Object. This will be used to call the appropriate OpenAI llm.
   - **Methods**:
     - `call(self, chat_history: ChatMessageHistory) -> str`: method used to call the service class which will summarize the conversation.
  ### ChatBot
   - **Fields**:
     - `llm`: Langchain ChatOpenAI Object. This will be used to call the appropriate OpenAI llm.
   - **Methods**:
     - `call(self, question: Question, chat_history_summary: str, relevant_docs: List[RelevantDoc]) -> str`: method used to call the service class which stream the chatbot response.

## Data Security
- Access to read and write data is strictly controlled through role-based access control (RBAC). Two different user roles are defined: one for reading data and another for both reading and writing data.
- The admin user has exclusive write access to the databases, ensuring that only authorized changes can be made.

# Deployment Strategy
- The API will be deployed in Azure as container apps. 
- CD/CI will be set-up for both API so that any changes to the prod branch in the GitHub repo are automatically deployed to Azure.
