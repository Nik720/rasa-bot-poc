# Rasa based Menu Driven Workflow 
## Prerequisites: 
Technology need to be installed 
    - Rasa - 2.5.0
    - Python - 3.7.0
    - Node - 12+

### Follow below commands to train rasa and run rasa servers
``` 
- rasa train
- rasa run actions
- rasa run -p 5005 --enable-api --cors * -vv
```

### Run router service 
```
- Goto /route directory
- Install node dependencies (npm install)
- node appRest.js
```

#### curl commands for portal bot and whatsApp bot
```
curl --location --request POST 'http://localhost:8000/bot' \
--header ': application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "Body": "Hi",
    "userId": "449c94833e1caa71aaadfe2567bea945",
    "appId": "prod.diksha.portal",
    "channel": "505c7c48ac6dc1edc9b08f21db5a571d",
    "From": "449c94833e1caa71aaadfe2567bea945",
    "context": null
}'
```

```
curl --location --request POST 'http://localhost:8000/whatsapp?client_key=secretkey' \
--header 'Content-Type: application/json' \
--data-raw '{
    "incoming_message": [{
        "from": "919611654628",
        "text_type": {
            "text": "Hi"
        }
    }]
}'
```