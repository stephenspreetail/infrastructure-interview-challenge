# infrastructure-interview-programming-challenge

This repository contains the in-interview programming challenge for infrastructure engineers. Candidates will be given access to this repository prior to the interview and will be required to complete the missing parts of the program during the interview. Candidates will be able to use their own computer and are allowed to use the internet to look up documentation.

## Background

Secrets are an essential part of any connected software system. They are information that is typically used to ensure secure communications between other systems. It is imperative that this information remains secret. One strategy for keeping this information secret and for reducing the damage that can be done if the information is exposed, is to regularly rotate your secrets. This is done by generating a new secret and destroying the old one.

## The task

Your task is to implement a script that will read all the secrets from a secret store, find any AWS access keys and rotate them. Your script should also write the new keys back to the secrets store.

A scaffold for this script has already been provided for you in this repository. You will need to implement the missing functionality.

You are expected to use the AWS Python client library `boto3`. You may reference the documentation for the library which can be found here: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

We have implemented request stubbing in `boto3` so that you don't need to make any actual calls to AWS. Once you have written your solution we will provide you with the stubbed values to test against.

The secret store has been simulated in code and can be accessed by importing the `list_secrets`, `get_secret` and `set_secret` functions in `secrets.py`. You may assume that any applications using a secret instantly start using the new value when `set_secret` is called.

The format of the keys in the secret store is `<app-name>/<environment>/<secret-name>`. The AWS user name for each set of IAM access keys is `<app-name>/<environment>`.

## Getting started

**Install:**

1. Install the Python [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer/) tool. This will be used to install the dependencies into a virtualenv.
2. Clone this repository to your own machine.
3. Run `poetry install` inside the repository

**Code Changes:**

1. Modify the `rotate_secrets` function in `rotate_secrets.py` to implement your solution.
2. Once you have completed your implementation you will be given the stub values to test against. Place these in the `stub_responses` function in `stubber.py`
3. Run Your script with `poetry run python src/rotate_secrets.py`

## Things we’ll be looking for:

- Ability to read and interpret technical documentation
- Ability to reason through a problem and communicate through the solution
- Ability to debug issues as they arise
