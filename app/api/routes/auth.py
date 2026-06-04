from fastapi import APIRouter, HTTPException, Response, status

from app.api.deps import CurrentUser, DbSession
from app.core.security import create_access_token
from app.crud.users import authenticate_user, create_user, get_user_by_login
from app.schemas.user import LoginRequest, Token, UserCreate, UserRead

router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: DbSession) -> UserRead:
    existing = await get_user_by_login(db, user_in.username)
    if existing or await get_user_by_login(db, user_in.email):
        raise HTTPException(status_code=400, detail="User with this username or email already exists")
    return await create_user(db, user_in)


@router.post("/login", response_model=Token)
async def login(credentials: LoginRequest, response: Response, db: DbSession) -> Token:
    user = await authenticate_user(db, credentials.username, credentials.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = create_access_token(user.username)
    response.set_cookie("access_token", token, httponly=True, samesite="lax")
    return Token(access_token=token)


@router.get("/me", response_model=UserRead)
async def read_me(current_user: CurrentUser) -> UserRead:
    return current_user


@router.get("/private-note")
async def private_note(current_user: CurrentUser) -> dict[str, str]:
    return {"message": f"Hello, {current_user.username}. This route requires JWT authentication."}


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response) -> None:
    response.delete_cookie("access_token")
