from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

#dummy data
posts: list[dict] = [
    {
        "id": 1,
        "author": "Dennis Fang",
        "title": "FastAPI is Awesome",
        "content": "This is a good framework.",
        "date_posted": "March 24, 2026",
    },
    {
        "id": 2,
        "author": "Dennis Dennis",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development.",
        "date_posted": "March 24, 2026",
    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)

#reutrn HTML instead of JSON
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[1]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts