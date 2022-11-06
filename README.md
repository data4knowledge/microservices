# d4k Mcroservices

## Introduction
This read me identifies a set of microservices that implement a range of functionality that allows for the handling of clinical trial data in an automated manner. The use cases addressed are

1. Import of data held in a variety of data formats into study designs
3. Export of data in a number of formats

The microservices within the system are:

1. Controlled Terminology
2. Biomedical Concepts
3. SDTM
4. Forms
5. Study


## Port Numbers

### User Interface Services

| Microservice | Port |
| ------------- | ------------- |
| CT | 8000 |
| BC | 8001 |
| Study | 8002 |
| Form | 8003 |

### Data Services

| Microservice | Port |
| ------------- | ------------- |
| CT | 8010 |
| BC | 8011 |
| SDTM | 8011 |
| Form | 8011 |
| Study | 8011 |
| Study Import | 8011 |
| Study Data Import | 8011 |
| Studu Data Export | 8011 |
