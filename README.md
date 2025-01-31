# DD2480, task 1: Launch-Interceptor-Program
This repo contains an implementation of a hypothetical anti-ballistic missile system, as described in "Launch Interceptor Program: Requirements Specification" by J. C. Knight and N. G. Leveson.

The program will print either "YES" or "NO" to standard output, depending on if the missile will be launched.

## Tech Stack
* This program is written in **Python 3.13**.
* Unit tests and integration tests are implemented using **Pytest 8.3.4**
* **GitHub Actions** is used to automate CI/CD workflows.

## Run and Test
First you need to install Python and navigate to the root directory:
```
% cd Launch-Interceptor-Program/
% pip install -r requirements.txt
```
To run all tests, you can use:
```
% pytest test/
```
To run the program (invoke decide() with hard-coded inputs), you can use:
```
% python -m src.main
```

## Contributions
* Oscar Hellgren
  * CMV, PUV, FUV, LAUNCH

* Anton Yderberg
  * LIC's 0, 3, 6, 9, 12
    
* Zubair Yousafzai
  * LIC's 1, 4, 7, 10, 13
    
* Shangxuan Tang
  * LIC's 2, 5, 8, 11, 14
