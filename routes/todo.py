from fastapi import APIRouter
from fastapi import Path # Path Variable 객체
from fastapi import HTTPException

import schemas.todo as todo_schema
from schemas.todo import todos # 할 일 목록
from typing import List



# 라우터 생성
router = APIRouter(tags=['todos'])


# TODO 목록 불러오기
@router.get("/todos", response_model=List[todo_schema.Todo])
async def get_todos():
    return todos

# 새 TODO 생성
# 중복된 id가 있을 때 생성
# 중복된 id가 있을 때 생성하면 안됨 400 에러 발생
@router.post("/todos")
async def add_todo(todo: todo_schema.Todo):
    # 중복된 id가 있는지 확인
    for existing_todo in todos:
        if existing_todo.id == todo.id: # 이미 있다면
            raise HTTPException(
                status_code=400,
                detail="해당 id를 가진 todo가 이미 있습니다."
            )
    # 중복되는 Todo가 없으면 목록에 추가
    todos.append(todo) # 전달받은 Todo를 목록에 추가 
    return todo

# TODO 변경
@router.put("/todos/{todo_id}")
async def modify_todo(todo_id: int = Path(
    ..., # 필수 필드
    title="Todo Id",
    description="수정할 Todo 아이템의 ID",
    ge = 1, # 1이상
    le = 100 # 100이하
)):
    pass

# TODO 삭제
# 목록에서 todo_id를 가진 Todo항목이 있으면 삭제
#                                  없으면 404 에러
@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int = Path(
    ...,
    title="Todo ID",
    description="삭제할 Todo 아이템의 ID"
)):
    # 리스트에서 todo_id를 가진 항목을 찾기
    for index, todo in enumerate(todos):
        if todo.id == todo_id:  # 삭제할 아이디 찾으면
            # 리스트에서 항목 삭제
            delete_todo = todos.pop(index)
            return {"todo_id": todo.id,
                    "deleted_todo": delete_todo}
    # 삭제할 todo가 없을 때
    raise HTTPException(status_code=404,
                        detail="삭제할 Todo가 없습니다.")