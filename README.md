## Vanity Number Backend API (Flask)


Backend API implemented with Flask, which uses [vanitynumber](https://github.com/sreenivasanac/vanitynumber/) python package, and exposes functionalities as REST API endpoints

Deployed at Heroku [https://vanitynumber-backend-api.herokuapp.com/](https://vanitynumber-backend-api.herokuapp.com/)

[/validate?phone_number=%2B1-123-456-7890](https://vanitynumber-backend-api.herokuapp.com/validate?phone_number=%2B1-123-456-7890)

[/vanitynumbers?phone_number=1-866-266-5233](https://vanitynumber-backend-api.herokuapp.com/vanitynumbers?phone_number=1-866-266-5233)

#### Usage

- Clone the repo:
```
git clone https://github.com/sreenivasanac/vanitynumber-backend-api
cd vanitynumber-backend-api
```

- Create virtualenv:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

- Run the sample server
```
export FLASK_APP=api/server.py
flask run
```

#### Try the endpoints:

- Validation `/validate`

```
curl -X GET \
'http://127.0.0.1:5000/validate?phone_number=1-866-386-6481' \
-H 'content-type: multipart/form-data' \
-F phone_number=1-866-386-6481
```

Output
```
{"is_valid":true,"phone_number":"1-866-386-6481","success":true}
```

- Generating Vanity Numbers for a Phone Number `vanitynumbers`

```
curl -X GET \
'http://127.0.0.1:5000/vanitynumbers?phone_number=1-866-386-6481'
-H 'content-type: multipart/form-data' \
-F phone_number=1-866-386-6481
```

Output

```
{
    "phone_number": "1-866-386-6481",
    "success": true,
    "vanitynumbers": [
        "1-866-EVOMIT1",
        "1-866-FUNMIT1",
        ....
    ]
}
```


- Get Phone Number from Vanity Number
```
curl -X GET \
  'http://127.0.0.1:5000/phonenumber?vanity_number=1-866-FUNMIT1' \
  -H 'Content-Type: multipart/form-data' \
  -H 'Host: 127.0.0.1:5000' \
  -F phone_number=1-866-386-6481
```

Output

```
{"phone_number":"1-866-386-6481","success":true,"vanity_number":"1-866-FUNMIT1"}
```
