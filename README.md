# graphql-python-example
Example project for a GraphQL API...

Create and activate the virtual environment...
```
virtualenv --python=python3.8 .venv
source .venv/bin/activate
```

Install dependencies...
```
pip install --upgrade pip
pip install -r requirements.txt
```

Start the servers...
```
python server.py 
```

Query examples...
```
{
  __schema {
    queryType {
      name
      fields {
        name
        description
      }
    }
    mutationType {
      name
      description
      fields {
        name
        description
      }
    }
  }
}

{  
  __type(name: "Ticket") {
    name
    fields {
      name
      description
      type{
        name
      }
    }
  }
}

mutation {
  create_ticket (name: "T-0001", description: "...", storyPoints: 5) {
    expectedDateline
  }
}

query {
  health
  ticket(name: "x") {
    name,
    description,
    storyPoints
  }
}

mutation {
  add_person (fullName: "Alejandro", age: 36) {
    person {
      uuid
      fullName
      age
    }
  }
}

query {
  person (uid: "9b00471d-d8f6-4b46-84b8-71836dcbf446") {
    uuid
    fullName
    age
  }
}

query {
  people {
    uuid
    fullName
    age
  }
}

query {
  people (limit: 2, offset: 2) {
    uuid
    fullName
    age
  }
}

mutation {
  remove_person (uid: "28470c78-2084-4bf4-9ae8-1006e91e418a") {
    person {
      uuid
      fullName
      age
    }
  }
}
```
