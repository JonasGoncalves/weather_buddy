[![Linkedin Badge](https://img.shields.io/badge/-Antonio%20Jonas-0282d0?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/antonio-jonas-gonçalves-de-oliveira-7a3830191/)](https://www.linkedin.com/in/antonio-jonas-gonçalves-de-oliveira-7a3830191/)

## Introduction
<p>
    Repository of a API developed to the DevGrid Assessment Challenge. The API goal is to use notions of Python and Flask to consume the Open Weather API, collect the data and than caches it for configurable period of time.
</p>

## Endpoints
<p>
    In this API it was use only the <b>get</b> requisition for the both endpoints developed.
</p>

### Data Query (GET requisitions)

#### **/weather/<city_name>**
<p>
    Uses the cache data for the specified <b>city_name</b> searched, if the cache is clean, than uses de Open Weather API to fetch the data and caches.
</p>
 
 #### **/weather**
<p>
    Get all the cached cities, up to the latest n entries or the specified <b>max_number</b>.
</p>

## Tests
<p>
    A unit test should test the behaviour of a unit of work: for a given input, it expects an end result that can be any of the above.
</p>

<p>
    It was use Pytest with the pytest-flask extension to create the follow types of unit tests.
</p>

### Unit Tests

#### **test_no_cached_cities**
<p>
  In this test, we call the /weather endpoint without search for a city, so the return must be not found (404)
</p>

#### **test_city**
<p>
  In this test, we call the /weather/<city_name> endpoint and search for a city, so the return must be success (200) and the data can't be None
</p>

#### **test_existing_cached_cities**
<p>
  In this test, we call the /weather/ endpoint after we search for a city, so the return must be success (200) and the data with the cache cities can't be None
</p>

#### **test_no_existing_city**
<p>
  In this test, we call the /weather/<city_name> endpoint and search for a fake city, so the return must be not found (404) and the data need to be None.
</p>

## Instructions
<p>
  In this section will be explain how to start the project and use of Swagger.
</p>

### Dockerfile and Docker-Compose
<p>
    The project has a Dockerfile to create a image using the 'docker build -t --image' and 'docker container run --name' commands or more simply using 'docker-compose up' command for using the dokcer-compose option.
</p>

### Local Run 
<p>
    Testing the project local is also simple, first enter the src folder (cd src) and than execute on the terminal the follow command: 'python -m flask run'.
</p>

### Swagger
<p>
    Using the Flask Restx lib, the application automatically generates the Swagger Documentation, which can be very helpful to test the endpoints in the project, it can be use usually opening the broswer and going to 'http://localhost:5000/'.
</p>
