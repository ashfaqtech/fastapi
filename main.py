from fastapi import FastAPI, HTTPException
import uvicorn  # 1. Import uvicorn
import helper

app = FastAPI()

# Create table on start
helper.create_table()


@app.post("/students")
def create_student(name: str, age: int):
    return helper.create_student(name, age)


@app.get("/students")
def get_students():
    return {"students": helper.get_students()}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = helper.get_student(student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Not found")

    return {"student": student}


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int):
    updated = helper.update_student(student_id, name, age)

    if updated == 0:
        raise HTTPException(status_code=404, detail="Not found")

    return {"message": "Updated"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    deleted = helper.delete_student(student_id)

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Not found")

    return {"message": "Deleted"}


# 2. Add this block at the very bottom of your file
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)