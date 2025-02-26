
API 

/apiV1/chat/ -- for querying
{
    "message": ""
}
Add header Authorization: Token<user token>
returns {'response': response_message}

/apiV1/load-data/ -- for loading data in vector db
Add header Authorization: Token<user token>
returns {
                    "message": "Data loaded successfully"
    }

/login/ -- for login
{
    "email": "",
    "password": ""
}
returns {
                    "message": "Login successful",
                    "token": ""
    }



/register/ -- for register
{
    "email": "",
    "username": "",
    "password": ""
}
returns {
                    "message": "User registered successfully",
                    "token": ""
    }

/logout/ -- for logout
Add header Authorization: Token <user token>
returns {
                    "message": "Logout successful"
    }
