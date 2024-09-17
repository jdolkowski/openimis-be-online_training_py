# openIMIS Backend Online Training Reference Module

In this task, you will be working with a Django-based GraphQL module to add and query encrypted messages. Your goal is to use a mutation to add a new `EncryptedMessage` and verify the results by querying the database to ensure that the message has been correctly added and decrypted.

## Objective

1. **Add a New EncryptedMessage**: Use a GraphQL mutation to add an encrypted message to the database.
2. **Query and Verify**: Query the database to confirm that the new message has been added and correctly decrypted.

## Tasks

### 1. Generate Translations

- **Objective**: Generate translations for the module.
- **Instructions**: If you need guidance, refer to the instructions in the backend assembly README.

### 2. Get Familiar with the Files

- **Objective**: Review and understand the files within the module.
- **Instructions**: Explore the module’s files to get a sense of its structure and functionality.

### 3. Uncomment and Complete the Query Class

- **Objective**: Implement the `Query` class based on other modules.
- **Instructions**: Uncomment the `Query` class and refer to other modules for guidance on completing the code. Ensure it can handle queries for encrypted messages.

### 4. Inspect API GraphQL Endpoint

- **Objective**: Check if there are existing entries in the database.
- **Instructions**: Visit the `api/graphql` endpoint to see if there are any existing encrypted messages. Note that the messages will be encrypted, but this will be adjusted later to display decrypted content.

### 5. Uncomment and Complete the Mutation Class

- **Objective**: Implement the `Mutation` class for adding new messages.
- **Instructions**: Uncomment the `Mutation` class and complete the code to handle mutations that add new encrypted messages to the database.

### 6. Modify Code to Encode Messages

- **Objective**: Ensure the message sent by the mutation is properly encoded.
- **Instructions**: Review the mutation/service code to understand how to encode the message before storing it in the database. Modify the code as needed to ensure proper encoding.

### 7. Decode and Verify Messages

- **Objective**: Ensure that messages are correctly decoded upon querying.
- **Instructions**: Adjust the code to ensure that encrypted messages are decrypted when queried. Verify that you can see both your message and the one left for you, confirming that the encoding and decoding processes are functioning correctly.

## Useful Information

- **`utils.py`**: Provides functions for encoding and decoding messages.

### Example Query

Here is an example GraphQL query:

```graphql
{
  benefitPlan(isDeleted: false, first: 10, orderBy: ["code"]) {
    edges {
      node {
        uuid
        id
        isDeleted
        dateCreated
        dateUpdated
        version
        dateValidFrom
        dateValidTo
        description
        replacementUuid
        code
        name
        type
        maxBeneficiaries
        ceilingPerBeneficiary
        beneficiaryDataSchema
        jsonExt
      }
    }
  }
}

```
### Example Mutation

Here is an example GraphQL mutation:

```graphql
mutation {
  createBenefitPlan(
    input: {name: "test", code: "test", type: INDIVIDUAL, dateValidFrom: "2024-09-01", dateValidTo: "2024-09-30"}
  ) {
    clientMutationId
    internalId
  }
}
```
