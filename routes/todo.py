from fastapi import APIRouter

# 라우터 생성
router = APIRouter(tags=['todos'])


# TODO 목록 불러오기
@router.get("/todos")
async def get_todos():
    return []

# 새 TODO 생성
@router.post("/todos")
async def add_todo():
    pass

# TODO 변경
@router.put("/todos/{todo_id}")
async def modify_todo():
    pass

# TODO 삭제
@router.delete("/todos/{todo_id")
async def delete_todo():
    pass