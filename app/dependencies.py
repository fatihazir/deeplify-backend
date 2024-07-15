from fastapi import HTTPException, Header, Depends

#Just to demonstrate any token based authentication, can be connected to firebase or any other auth service or db. 
def verify_token(token: str = Header(...)):
    if token != "deeplify-is-awesome-with-fatih-:)":
        raise HTTPException(status_code=401, detail="Unauthorized")
