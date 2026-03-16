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

    # Create new access key for app1/production
    stubber.add_response(
        "create_access_key",
        {
            "AccessKey": {
                "UserName": "app1/production",
                "AccessKeyId": "PRODNEW999999EXAMPLE",
                "Status": "Active",
                "SecretAccessKey": "production_new_secret_987654321",
                "CreateDate": datetime(2024, 2, 1, 0, 0, 0),
            }
        },
        expected_params={"UserName": "app1/production"},
    )

    # Delete old access key for app1/production
    stubber.add_response(
        "delete_access_key", {}, expected_params={"UserName": "app1/production", "AccessKeyId": "PROD111111111EXAMPLE"}
    )

    # ===== app1/staging =====

    # List existing access keys for app1/staging
    stubber.add_response(
        "list_access_keys",
        {
            "AccessKeyMetadata": [
                {
                    "UserName": "app1/staging",
                    "AccessKeyId": "STAGE22222222EXAMPLE",
                    "Status": "Active",
                    "CreateDate": datetime(2024, 1, 1, 0, 0, 0),
                }
            ]
        },
        expected_params={"UserName": "app1/staging"},
    )

    # Create new access key for app1/staging
    stubber.add_response(
        "create_access_key",
        {
            "AccessKey": {
                "UserName": "app1/staging",
                "AccessKeyId": "STAGENEW88888EXAMPLE",
                "Status": "Active",
                "SecretAccessKey": "staging_new_secret_987654321",
                "CreateDate": datetime(2024, 2, 1, 0, 0, 0),
            }
        },
        expected_params={"UserName": "app1/staging"},
    )

    # Delete old access key for app1/staging
    stubber.add_response(
        "delete_access_key", {}, expected_params={"UserName": "app1/staging", "AccessKeyId": "STAGE22222222EXAMPLE"}
    )

    stubber.activate()
