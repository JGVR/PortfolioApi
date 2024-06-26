# PortfolioApi
PortfolioAPI is a RESTful service designed to seamlessly integrate with MongoDB, enabling efficient CRUD operations across various collections. It serves as the backbone for user interfaces that display comprehensive portfolio information, including work experiences and projects, tailored for individuals looking to showcase their professional journey. Unique to our API is the integration of a sophisticated Chatbot, powered by OpenAI's latest GPT-4o model, which acts as a personal assistant, enriching user interaction with instant, intelligent responses to inquiries. Developed with **django, pymongo, django channels, djnagorestframework, pydantic, langchain**, this API offers an unparalleled blend of functionality and user engagement.

## Getting Started

### Prerequisites

### Installation
Run the following commands to install the appropriate packages:
* pip install pydantic
* pip install pymongo
* pip install Django
* pip install djangorestframework
* pip install 'channels[daphne]'
* pip install langchain-openai
* pip install langchain-core
* pip install langchain-community
* pip install langchain-mongodb

# Data Design

This section provides a detailed overview of the data design, including the database schema, entity relationships, and security measures implemented to protect the data.

## Overview

The Portfolio API utilizes two main types of databases to store and manage data efficiently: MongoDB Atlas, a NoSQL database for storing portfolio information, and Pinecone Vector Database, a specialized database for managing vector data to enhance chatbot functionalities.

### Diagrams

#### Model Data Classes UML 
![Data Classes drawio (1)](https://github.com/JGVR/PortfolioApi/assets/54122915/646a116e-2415-413d-aad9-d1a4769cda18)

#### Collection Classes UML 
![Collection Classes - UML drawio (2)](https://github.com/JGVR/PortfolioApi/assets/54122915/b4cc0f94-ea3d-409e-9fab-49c6955d4fd5)

#### ChatBot Classes UML 
![ChatBot (1)](https://github.com/JGVR/PortfolioApi/assets/54122915/a1276fd5-f9d7-4a3a-a309-c1033931494e)

## Entities

### Users

- **Description**: Contains information about the individual, including personal details and professional achievements.
- **Fields**:
  - `id`: Unique identifier for the user.
  - `first_Name`: The person’s first name.
  - `last_Name`: The person’s last name.
  - `date_of_birth`: The date the person was born.
  - `hobbies`: A list of hobbies the person engages in.
  - `short_bio`: A short biography of the person.
  - `bio`: A full biography of the person.
  - `country_of_birth`: The country where the person was born.
  - `country_of_residence`: The country where the person resides.
  - `email_address`: The person’s email address.
  - `linkedIn_url`: The URL to the person’s LinkedIn profile.
  - `gitHub)_url`: The URL to the person’s GitHub profile.
- **Relationships**:
  - One-to-Many with Projects, Experience, and Achievements.

### Projects

- **Description**: Represents projects the individual has worked on.
- **Fields**:
  - `id`: Unique identifier for the project.
  - `user_id`: Unique identifier for the user the project belongs to.
  - `description`: Detailed description of the project.
  - `skills`: Technologies used in the project.
  - `images`: URLs to images related to the project.
  - `url`: Link to the project, if available.
- **Relationships**:
  - Many-to-One with Users.

### Experience

- **Description**: Work experience records of the individual.
- **Fields**:
  - `id`: Unique identifier for the job experience.
  - `user_id`: Unique identifier for the user the experience belongs to.
  - `project_ids`: A list of project ids.
  - `company`: The company's name.
  - `job_title`: The title of the job.
  - `job_description`: Description of the job role.
  - `start_date`: The start date of the position.
  - `end_date`: The end date of the position, if applicable.
- **Relationships**:
  - Many-to-One with Users and Projects.

### Achievements

- **Description**: Academic and professional achievements of the individual.
- **Fields**:
  - `id`: Unique identifier for the achievement.
  - `user_id`: Unique identifier for the user the achievement belongs to.
  - `certificates`: Certificates earned by the individual.
  - `degrees`: Academic degrees earned by the individual.
- **Relationships**:
  - Many-to-One with Users.

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
    - `text`: inherited from Message class. This field will hold the chatbot answer to the user's question.
    - `question`: A Question object. Represents the user's question.
    - `chat_history`: Langchain ChatMessageHistory object. This field will hold the history of the conversation.
    - `completed`: A bool object. This field represents if the answered is completed.
   - **Methods**:
    - `from_chunks(cls, chunks: List[str], question: Question, chat_history: ChatMessageHistory) -> Answer`: Creates an answer object from chunks of text.
    - `serialize(self) -> Dict[str, Any]`: Converts the Answer object to a Dictionary.
  ### RelevantDoc
   - **Fields**:
    - content: str. This field contain the content of the relevant docs that the chatbot will use as context to answer the user's question.
   - **Methods**:
    - `serialize(self) -> Dict[str, Any]`: Converts the RelevantDoc object to a Dictionary.
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
