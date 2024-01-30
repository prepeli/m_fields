# m_fields Readme file
Playwright test automation scenario for m_fields

## .gitignore
Rename secrets_example.py to secrets.py and replace/insert credentials

## Running the basic test(s)
To run the test file, you can use the following command in your terminal:

pytest test_all.py


This command will execute all the tests in the test_all.py file. If you want to run a specific test, you can use the -k flag followed by the name of the test. For example, to run the test_open_page test, you can use the following command:

pytest test_all.py -k test_open_page

This command will only execute the test_open_page test.



## To enable debugging mode:
import os
os.environ['PWDEBUG'] = '1'