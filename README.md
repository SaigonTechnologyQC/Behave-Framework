# BEHAVE FRAMEWORK
Test Automation Framework Using Python and Behave BDD to test REST services and API

Swagger For Demo: http://petstore.swagger.io/

## Installation
- Create virtual environment directory: ` python -m venv .env` to 
- Activate the virtual environment: `env/Script/activate` or  ` source env/bin/activate`
- Install library dependency: ` pip -r install requirements.txt`

## Project Structure
- Overall structure is followed as:
```
+-- requirements.txt //store the library dependencies
+-- behave_rest/
    +-- environment.py //contain common actions related to scenarios
+-- features/
    +-- config.yaml //store project config (urls, global variables, etc.)
    +-- environment.py //context setup steps (e.g. load from config.yaml)
    +-- steps/
        +-- base_steps.py // defines common steps
        +-- init_test_conditions.py //init test data before executing the TCs
        +-- *_steps.py // steps related to corresponding feature 
    +-- testcase/
        +-- *.feature //test cases to verify the APIs
    
+-- resources/
    -- *.json // test data

+-- reports
    +-- *.xls // test report utilized to import into Azure DevOps

 +-- utilities/
    +-- *_utilities.py //define a utility library 
```

## Run Tets
```bash

# choose testing environment (e.g., qa environment)
export env=qa

# set client_id value
export client_id=client_id_of_env

# set client_secret value
export client_secret=secret_id_of_env

#set baseURL and endpoing
export baseURL=base_url

# execute all feature files without using the shell script (all tests)
behave

# execture specific feature without using the shell script
behave features/regression_test/sample.feature

# show the printed output without using the shell script
behave --no-capture

# run features with specific tag without using the shell script
behave --tags=smoke

# run features with specific tags without using the shell script
behave --tags=us_6485,us_6486,us_6487

# skip printing the unwanted tags in the console without using the shell script
behave --no-skipped

# run features with specific tags in parallel
behavex --tags=parallel-test --no-capture --parallel-processes 2 --parallel-scheme scenario

# run features with specific tags and generate the allure report by using the shell script
sh shell_script/demo_executation.sh

```