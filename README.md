# COGGOLF
CogGolf is a service for submitting and judging code challenges. The goal is to submit C code that solves the requested prompt, while using the least amount of non-whitespace characters.

## API
Although there is a webpage hosted for submitting code and viewing results, the same functionality is available via an HTTP (Restful-like) API.

### Submitting a file
```
POST 
Host: http://10.25.80.26:5000/api/upload
Content-Type: multipart/form-data

challenge=CHALLENGE&name=NAME
```

### View Scores
```
POST
Host: http://10.25.80.26:5000/api/viewscores
Content-Type: multipart/form-data

challenge=CHALLENGE
```
