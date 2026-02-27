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
    # TODO: Paste in stubbed values when given
    pass
