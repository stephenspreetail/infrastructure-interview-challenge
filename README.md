## Background

- **Secrets** are an essential part of any connected software system.
- It is imperative that secrets remain **protected**.
- One protection strategy is to **rotate your secrets**.
- This is done by **generating a new secret** and **destroying the old one**.

## Your task

Your task is to implement a script that will read all the secrets from a secret store, find any AWS access keys and rotate them. Your script should also write the new keys back to the secrets store.

> You need to **implement the missing functionality** in the scaffold in `rotate_secrets.py` to:

1. Read all the secrets from the secret store
2. Find any AWS access keys (use the AWS IAM Client from `boto3`)
3. Rotate the AWS access keys
4. Write the new keys back to the secrets store

### Secret Store

- The secret store is simulated in `secrets.py` and can be accessed by importing the `list_secrets`, `get_secret` and `set_secret`
- The format of the keys in the secret store is `<app-name>/<environment>/<secret-name>`
- The AWS user name for each set of IAM access keys is `<app-name>/<environment>`

### AWS IAM Client (boto3) Stubbing

- We have implemented request stubbing in `boto3` so that you don't make actual calls to AWS
- Once you have written your solution, we will provide you with the stubbed calls and response values to test against in `stubber.py`
- Use the following documentation to determine which Access Key `boto3` calls you will make
- The `list_access_keys` stubbed call has been given to you for the `app1/production` user

> https://docs.aws.amazon.com/boto3/latest/reference/services/iam.html

## Getting started

**Install:**

1. Install the Python [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer/) tool
2. Clone this repository to your own machine
3. Run `poetry install` inside the repository - this will install the dependencies into a virtualenv

**Code Changes:**

1. Modify the `rotate_secrets` function in `rotate_secrets.py` to implement your solution
2. Once you have completed your implementation you will be given the rest of the stub functions and responses to test against
3. Run Your script with `poetry run python src/rotate_secrets.py`

## Things we’ll be looking for:

- Ability to read and interpret technical documentation
- Ability to reason through a problem and communicate through the solution
- Ability to debug issues as they arise
