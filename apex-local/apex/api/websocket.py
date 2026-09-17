from fastapi import WebSocket
async def stream(websocket:WebSocket):
 await websocket.accept();await websocket.send_json({'status':'connected','service':'APEX Local'});await websocket.close()
