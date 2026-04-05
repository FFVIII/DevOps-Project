# 使用轻量级 Python 镜像
FROM python:3.13-slim

# 从 uv 镜像中拷贝二进制文件（加速包管理）
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 声明构建参数 (Build-time arguments)
# 我们只保留一个，因为你现在只有一个 Key
ARG SECRET_KEY

# 将构建参数转换为环境变量 (Runtime Environment Variables)
# 重要：变量名必须与 Python 代码中 Settings 类的字段名匹配（不区分大小写，但建议全大写）
ENV SECRET_KEY=${SECRET_KEY}

# 设置工作目录
WORKDIR /app

# 拷贝项目文件
COPY . /app

# 使用 uv 同步依赖，不生成缓存以减小镜像体积
RUN uv sync --frozen --no-cache

# 暴露端口（虽然是文档性质，但建议加上）
EXPOSE 8000

# 启动命令
CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]