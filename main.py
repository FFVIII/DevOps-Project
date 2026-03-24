from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

#import templates
templates = Jinja2Templates(directory="templates")

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

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):                                                
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )

@app.get("/api/posts")
def get_posts():
    return posts