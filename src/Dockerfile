# 使用 Python 3.10 作為基底映像
FROM python:3.10-slim

# 設置工作目錄
WORKDIR /app

# 複製應用程式和依賴文件到容器中
COPY app.py .
COPY formulas.py .
COPY requirements.txt .

# 安裝必要的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 指定 Streamlit 預設埠
EXPOSE 8501

# 運行 Streamlit 應用
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
