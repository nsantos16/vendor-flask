# Vend-O-Matic API

## Getting Started
1. Clone the repository
2. Install dependencies with pipenv: `pipenv install`
3. Create Postgres Databases for production and testing enviornments
4. Create and export the next enviornment varaibles:

| Variable               | Description                  | Default value |
|------------------------|------------------------------|---------------|
| DATABASE_USER          | Postgres DB user             | postgres      |
| DATABASE_PASSWORD      | Postgres DB password         | postgres      |
| DATABASE_NAME          | Name of the Postgres DB      | vend_o_matic  |
| DATABASE_HOST          | Postgres DB Host             | 127.0.0.1     |
| TEST_DATABASE_USER     | Postgres DB user test        | postgres      |
| TEST_DATABASE_PASSWORD | Postgres DB password test    | postgres      |
| TEST_DATABASE_NAME     | Name of the Postgres test DB | vend_testing  |
| TEST_DATABASE_HOST     | Postgres Test DB Host        | 127.0.0.1     |

5. Run `invoke seed-db`
6. Run `invoke run`

## Commands
- For initialize the DB schema `invoke init-db`
- For drop all the information `invoke drop-all`

## API Docs
You can access to API documentation on `/docs`
