from quart import Quart, Request, Response, websocket
from controller import Controller

app = Quart(__name__)

@app.websocket('/ws/topic/<topic_id>/asset/<asset_id>')
async def ws(topic_id, asset_id):
    await Controller.handle_websocket(topic_id, asset_id, websocket)


@app.route('/topic')
async def topic_route():
    return await Controller.handle_topic_request(Request, Response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8765)
