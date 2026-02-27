from datetime import datetime  # noqa (fixed when values are pasted in)
from botocore.stub import Stubber


def stub_client(client) -> Stubber:
    """
    Stubs the given AWS client so that it does not make actual calls to AWS.
    """
    stubber = Stubber(client)
    stub_responses(stubber)
    return stubber


def stub_responses(stubber) -> None:
    """
    Defines the responses that will be returned by the stubbed AWS client. These values will be
    given to you after you have completed you implementation of the rotate_secrets function.
    """

    # ===== app1/production =====

    # List existing access keys for app1/production
    stubber.add_response(
        "list_access_keys",
        {
            "AccessKeyMetadata": [
                {
                    "UserName": "app1/production",
                    "AccessKeyId": "PROD111111111EXAMPLE",
                    "Status": "Active",
                    "CreateDate": datetime(2024, 1, 1, 0, 0, 0),
                }
            ]
        },
        expected_params={"UserName": "app1/production"},
    )

    # TODO:
    #
    # We will give you the rest of the stubbed function calls and responses after you have
    # completed your implementation of the rotate_secrets function.
    #
    # You can implement the first part of the function using the above stubbed response, and
    # then paste in the rest of the stubbed responses once we give them to you.
    #
    # The expectation is that your rotate_secrets function will make the same calls to the AWS
    # client with the same parameters as defined in the stubbed responses, and that it will
    # correctly handle the responses to rotate the secrets in the secret store.

    stubber.activate()
