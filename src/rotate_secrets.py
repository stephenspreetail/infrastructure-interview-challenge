import boto3

from mypy_boto3_iam.client import IAMClient
from secrets import print_secrets_store
from stubber import stub_client


def rotate_secrets(iam_client: IAMClient):
    """
    This is the function that you are required to implement during the interview. It should read
    all the secrets from the secret store, find any AWS access keys and rotate them. It should
    also write the new keys back to the secrets store.
    """
    # TODO: Implement me
    pass


if __name__ == "__main__":

    iam_client = boto3.client("iam")

    with stub_client(iam_client):
        rotate_secrets(iam_client)

        # We print out the secret store to check that we are setting the expected values
        print_secrets_store()
