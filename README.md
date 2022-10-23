# Twitter Clone
Simple twitter clone with FastAPI

## Getting Started
1. Enter project root
```zsh
cd fastapi-twitter-like
```
2. Install dependencies
```zsh
pip install -r requirements.txt
```
3. Start FastAPI process
```zsh
uvicorn app.main:app --reload
```
4. Open local API docs [http://localhost:8000/docs](http://localhost:5000/docs)

## Tests
1. Enter project root
```zsh
cd fastapi-twitter-like
```
2. Run PyTest
```zsh
pytest
```

## Todo
- [x] Basic logic, endpoints and structure
- [ ] Better db choice, superuser, readme and dockerfile
- [ ] Auth roles and more endpoints
- [ ] Better endpoint logic for post management (only creator can change/delete)
- [ ] More tests