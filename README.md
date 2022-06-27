# CRM API

Customer relationship manager

- It manages all your company's relationships and interactions with customers and potential customers.
- It is used to manage customer relationships across the entire customer lifecycle, spanning marketing, sales, presales, operations and customer service interactions

## Manual Installation

Clone the repo:

```bash
git clone --depth 1 https://github.com/neo945/CRM CRM
```

Create Virtual Environment:

```bash
pip install virtualenv
python -m virtualenv venv
```

Activate Virtual Environment:

Windows:

```bash
.\venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Table of Contents

- [CRM api](#crm-api)
  - [Manual Installation](#manual-installation)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Commands](#commands)
  - [Environment Variables](#environment-variables)
  - [Project Structure](#project-structure)
  - [API Documentation](#api-documentation)
    - [API Endpoints](#api-endpoints)

## Technologies

- **SQL database**: [SQLite3](https://www.mongodb.com) object data modeling using [Django ORM](https://mongoosejs.com)
- **Authentication and authorization**: using [Django Session](http://www.passportjs.org) and [Cookie Storage](https://www.npmjs.com/package/jsonwebtoken)
- **Logging**: using [Django Loggings](https://github.com/winstonjs/winston) and [morgan](https://github.com/expressjs/morgan)
- **Testing**: using [PostMan](https://jestjs.io)
- **Process management**: advanced production process management using [PM2](https://pm2.keymetrics.io)
- **Environment variables**: using [dotenv](https://github.com/motdotla/dotenv) and [cross-env](https://github.com/kentcdodds/cross-env#readme)
- **CORS**: Cross-Origin Resource-Sharing enabled using [django-cors-headers](https://github.com/expressjs/cors)
  - **CI/CD**: continuous integration with [GitHub Actions](https://travis-ci.org)
- **Docker support**

## Commands

Running locally:

```bash
python manage.py runserver
```

Testing:

```bash
python manage.py test
```

## Environment Variables

The environment variables can be found and modified in the `.env` file. They come with these default values:

```bash
# Ḍjango secret key
SECRET_KEY=<SECRET_KEY>

# Email SMTP server to send email
EMAIL_SERVICE=<EMAIL_SERVICE>

# User email to send email from
USER_EMAIL=<USER_EMAIL>

# User email passeword
USER_PASSWORD=<USER_PASSWORD>

# Linkedin email
LINKEDIN_EMAIL=<LINKEDIN_EMAIL>
# Linkedin email
LINKEDIN_PASSWORD=<LINKEDIN_PASSWORD>

# Encryption key
KEY=<KEY>

# AWS IAM access key to S3 bucket
AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
AWS_STORAGE_BUCKET_NAME=<AWS_STORAGE_BUCKET_NAME>
AWS_S3_REGION_NAME=<AWS_S3_REGION_NAME>
```

## Project Structure

```
 .\
 |--crm\                # Main Django application directory
 |--accounts\           # Account application directory (Login and registration)
 |--customers\          # Customer application directory (Customer and client)
 |--leads\              # Customer application directory (Main business leads)
 |--logs\               # Logged data
 |--cmrcss\             # CMRCSS application directory (Customer feedback)
 |--forntend\           # React Js Frontend
 |--requirements.txt\   # Dependencies
```

### API Endpoints

List of available routes:

**Account routes**:

`POST /api/v1/accounts/register/` - Register a new user\
`POST /api/v1/accounts/login/` - Login a user\
`POST /api/v1/accounts/update/password/` - Update password of a user\
`GET /api/v1/accounts/logout/` - Logout a user\
`GET /api/v1/accounts/get/` - Get logged user\

_Company routes_:

`POST /api/v1/accounts/create/company/` - Create a new company\
`GET /api/v1/accounts/company/<int:company_id>` - Get a company by id\
`GET /api/v1/accounts/search/company?str=search_string` - Search companies by name\

_Job routes_:

`POST /api/v1/accounts/create/job/` - Create a job\
`GET /api/v1/accounts/job/<int:job_id>` - Get a job by id\
`GET /api/v1/accounts/search/job?str=search_string` - Search job by name\

**Feedback routes**:

`POST /api/v1/cmrcss/feedback/<str:token>` - User feedback\

**Customer routes**:

`POST /api/v1/customer/create/customer` - Create a customer\
`GET /api/v1/customer/get/<int:customerid>` - Get a customer by id\
`GET /api/v1/customer/add/customer/<int:customerid>/job/<int:jobid>` - Add a customer to a job\
`GET /api/v1/customer/get/job/<int:jobid>` - Get a customer by job id\

_Customer routes_:

`GET /api/v1/customer/get/client/job/<int:jobid>` - Get a client by job id\
`GET /api/v1/customer/get/client/<int:clientid>` - Get a customer by id\

**Leads routes**:

`GET /api/v1/leads/create/lead/customer/<int:customerid>` - Create a leads\
`GET /api/v1/leads/lead/<int:leadsid>` - Get a lead by id\
`GET /api/v1/leads/lead/job/<int:jobid>` - Get all leads by job id\
`GET /api/v1/leads/lead/moved/job/<int:jobid>` - Get all checked leads by job id\
`GET /api/v1/leads/lead/not/moved/job/<int:jobid>` - Get all unchecked leads by job id\

_Marketing leads routes_:

`POST /api/v1/create/market/<int:leadid>` - Create a marketing leads\
`POST /api/v1/create/market/` - Create all marketing leads\
`GET /api/v1/leads/market/<int:marketingleadid>` - Get marketing lead by id\
`POST /api/v1/leads/market/` - Get all marketing lead by id\
`POST /api/v1/leads/market/` - Get all marketing lead by id\
`POST /api/v1/leads/market/moved/` - Get all checked marketing lead by id\
`POST /api/v1/leads/market/not/moved/` - Get all unchecked marketing lead by id\
`GET /api/v1/leads/market/job/<int:jobid>` - Get all marketing leads by job id\
`GET /api/v1/leads/market/moved/job/<int:jobid>` - Get all checked marketing leads by job id\
`GET /api/v1/leads/market/not/moved/job/<int:jobid>` - Get all unchecked marketing leads by job id\

_Sales leads routes_:

`POST /api/v1/leads/create/sales/<int:marketingleadid>` - Create a sales leads\
`POST /api/v1/leads/create/sales/` - Create all sales leads\
`GET /api/v1/leads/sales/<int:salesleadid>` - Get sales lead by id\
`POST /api/v1/leads/sales/` - Get all sales lead by id\
`POST /api/v1/leads/sales/moved/` - Get all checked sales lead by id\
`POST /api/v1/leads/sales/not/moved/` - Get all unchecked sales lead by id\
`GET /api/v1/leads/sales/job/<int:jobid>` - Get all sales leads by job id\
`GET /api/v1/leads/sales/moved/job/<int:jobid>` - Get all checked sales leads by job id\
`GET /api/v1/leads/sales/not/moved/job/<int:jobid>` - Get all unchecked sales leads by job id\

_Presales leads routes_:

`POST /api/v1/create/presales/<int:salesleadid>` - Create a presales leads\
`POST /api/v1/create/presales/` - Create all presales leads\
`GET /api/v1/leads/presales/<int:presalesleadid>` - Get presales lead by id\
`POST /api/v1/leads/presales/` - Get all presales lead by id\
`POST /api/v1/leads/presales/moved/` - Get all checked presales lead by id\
`POST /api/v1/leads/presales/not/moved/` - Get all unchecked presales lead by id\
`GET /api/v1/leads/presales/job/<int:jobid>` - Get all presales leads by job id\
`GET /api/v1/leads/presales/moved/job/<int:jobid>` - Get all checked presales leads by job id\
`GET /api/v1/leads/presales/not/moved/job/<int:jobid>` - Get all unchecked presales leads by job id\

_Operations leads routes_:

`POST /api/v1/create/operation/<int:presalesleadid>` - Create a operation leads\
`POST /api/v1/create/operation/` - Create all operation leads\
`GET /api/v1/leads/operation/<int:operationsleadid>` - Get operation lead by id\
`POST /api/v1/leads/operation/` - Get all operation lead by id\
`POST /api/v1/leads/operation/moved/` - Get all checked operation lead by id\
`POST /api/v1/leads/operation/not/moved/` - Get all unchecked operation lead by id\
`GET /api/v1/leads/operation/job/<int:jobid>` - Get all operation leads by job id\
`GET /api/v1/leads/operation/moved/job/<int:jobid>` - Get all checked operation leads by job id\
`GET /api/v1/leads/operation/not/moved/job/<int:jobid>` - Get all unchecked operation leads by job id\

_Clients leads routes_:

`GET /api/v1/leads/create/client/operation/<int:operationsleadid>/job/<int:jobid>` - Create client from operations lead\
`GET /api/v1/leads/create/client/job/<int:jobid>` - Create all client from operations lead\

Feel free to contribute
