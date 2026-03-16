# Interview Guide (DO NOT COMMIT)

## Reference Materials Available to Candidates

* `src/stubber.py` is provided and contains the stubber implementation and example stub responses
* **boto3 IAM documentation** - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html

## Using the Stub Responses

### During the Interview

1. **Watch the candidate implement** `rotate_secrets()` function
2. **Observe their approach** - What boto3 IAM methods are they calling?
3. **Stub responses are provided up front in `src/stubber.py`**
4. **Candidate should use the stubbed responses as they implement their solution**

### Expected Stub Sequence

The stubs assume this rotation flow for each user:
1. `list_access_keys(UserName='...')` - Get current keys
2. `create_access_key(UserName='...')` - Create new key
3. `delete_access_key(UserName='...', AccessKeyId='...')` - Delete old key

### Expected Final Output

After successful execution, the secret store should contain:

```python
{
    'app1/production/AWS_ACCESS_KEY_ID': 'PRODNEW999999EXAMPLE',
    'app1/production/AWS_SECRET_ACCESS_KEY': 'production_new_secret_987654321',
    'app1/production/MY_SECRET': 'production_secret_value',
    'app1/staging/AWS_ACCESS_KEY_ID': 'STAGENEW88888EXAMPLE',
    'app1/staging/AWS_SECRET_ACCESS_KEY': 'staging_new_secret_987654321',
    'app1/staging/MY_SECRET': 'staging_secret_value',
}
```

### Common Issues to Look For

**If stubs fail:**
- Did they call APIs in a different order?
- Did they use different parameter names?
- Did they extract the username correctly from secret keys?

**Implementation red flags:**
- Deleting keys before creating new ones (causes downtime)
- Not handling multiple environments (only rotating one user)
- Hardcoding usernames instead of deriving from secret keys
- Not updating both ACCESS_KEY_ID and SECRET_ACCESS_KEY in the secret store

**Different order per user:**
- Some might process all operations for production first, then staging
- Some might do all list operations, then all creates, then all deletes

**Different IAM operations:**
- Some might call `update_access_key` to deactivate before deleting

## Evaluation Criteria

✓ **Reasons through problem** - Understands create-before-delete for zero downtime
✓ **Parses secret keys** - Correctly derives username from `<app>/<env>/<secret>` format
✓ **Updates secret store** - Calls `set_secret()` with both new key ID and secret
✓ **Handles multiple users** - Rotates keys for both production and staging
✓ **Debugs issues** - Can interpret stub mismatch errors and fix implementation

## Setup and Dependencies

* Only `boto3` is required. Install with `pip install boto3`.
* Candidate runs the script with `python src/rotate_secrets.py`.
