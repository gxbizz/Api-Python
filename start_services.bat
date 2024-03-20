uvicorn login_service:app --reload --port 8001
uvicorn produtos_service:app --reload --port 8002
uvicorn carrinho_service:app --reload --port 8003
uvicorn pedido_service:app --reload --port 8004