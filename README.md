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
| SDTM | 8004 |

### Data Services

| Microservice | Port |
| ------------- | ------------- |
| RA | 8010 |
| CRM | 8011 |
| CT | 8012 |
| BC | 8013 |
| Study | 8014 |
| Study Import | 8015 |
| Form | 8016 |
| SDTM | 8017 |
| Study Data Import | 8018 |
