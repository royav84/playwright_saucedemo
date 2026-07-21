login_error_cases = [ 
    ("standard_user_wrongUN", "secret_sauce_wrongPW","Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce","Epic sadface: Sorry, this user has been locked out."),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user","", "Epic sadface: Password is required")
                                       ]
